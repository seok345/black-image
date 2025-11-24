import os
import numpy as np
import cv2
from flask import Flask, request, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
import logging
from PIL import Image
import warnings
import torch

# --- [강력한 해결책] PyTorch 보안 검사 우회 ---
# DeOldify 모델은 옛날 방식(pickle)으로 저장되어 있어 최신 PyTorch(2.6+)에서
# 보안 에러가 계속 발생합니다. 하나씩 허용하는 대신, torch.load 함수를
# 수정하여 weights_only=False 옵션을 강제로 적용합니다.
_original_load = torch.load


def _force_legacy_load(*args, **kwargs):
    # 'weights_only' 인자가 없으면 강제로 False로 설정 (보안 검사 해제)
    # 이렇게 하면 옛날 모델 파일도 문제없이 열립니다.
    if 'weights_only' not in kwargs:
        kwargs['weights_only'] = False
    return _original_load(*args, **kwargs)


# torch.load 함수를 우리가 만든 함수로 교체 (Monkey Patching)
torch.load = _force_legacy_load
# ------------------------------------------------

# --- DeOldify (최신 모델) 라이브러리 임포트 ---
try:
    from deoldify.visualize import get_image_colorizer, ModelImageVisualizer
except ImportError:
    print("=" * 80)
    print("DeOldify 라이브러리를 찾을 수 없습니다.")
    print("터미널에서 'pip install deoldify fastai'를 실행하여 설치해주세요.")
    print("=" * 80)
    exit()

# --- 로깅 및 경고 설정 ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
warnings.filterwarnings("ignore", category=UserWarning, message=".*?torch.nn.utils.spectral_norm.*?")
warnings.filterwarnings("ignore", category=FutureWarning)

# --- 1. 설정 및 초기화 ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# --- 2. DeOldify 모델 로드 ---
colorizer = None
model_load_error = None

try:
    logging.info("DeOldify 모델 로드를 시작합니다...")

    # GPU가 있으면 GPU 사용
    if torch.cuda.is_available():
        logging.info("✅ GPU 발견! GPU 모드로 실행합니다.")
        torch.backends.cudnn.benchmark = True
    else:
        logging.info("⚠️ GPU를 찾을 수 없습니다. CPU 모드로 실행합니다 (속도가 느릴 수 있습니다).")

    # 'artistic' 모델이 고화질 사진에 가장 적합합니다.
    colorizer = get_image_colorizer(artistic=True)

    logging.info("✅ DeOldify 모델 로드 성공!")

except Exception as e:
    model_load_error = f"❌ DeOldify 모델 로드 실패: {e}"
    logging.error(model_load_error, exc_info=True)


# --- 3. 파일 확장자 확인 ---
def allowed_file(filename):
    """업로드된 파일이 허용된 확장자인지 확인합니다."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# --- 4. 흑백 → 컬러 변환 (DeOldify) ---
def colorize_image_deoldify(image_path, result_path):
    """DeOldify 모델을 사용하여 이미지를 컬러화하고 저장합니다."""
    if colorizer is None:
        logging.error("모델이 로드되지 않아 컬러화 할 수 없습니다.")
        return False

    try:
        logging.info(f"컬러화 시작: {image_path}")

        # render_factor는 이미지 품질을 결정합니다. (35~40 추천)
        result_pil_image = colorizer.get_transformed_image(
            path=image_path,
            render_factor=35,
            watermarked=False
        )

        # PIL 이미지를 OpenCV(BGR) 형식으로 변환하여 저장
        result_cv_image = cv2.cvtColor(np.array(result_pil_image), cv2.COLOR_RGB2BGR)
        cv2.imwrite(result_path, result_cv_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

        logging.info(f"✅ 변환 완료: {result_path}")
        return True

    except Exception as e:
        logging.error(f"컬러화 처리 중 오류: {e}", exc_info=True)
        return False


# --- 5. Flask 라우트 ---
@app.route('/', methods=['GET', 'POST'])
def upload_file_route():
    status = "활성화 (DeOldify)" if colorizer is not None else "비활성화 (모델 로드 실패)"
    error = model_load_error

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='파일이 없습니다.', model_status=status)

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='파일을 선택해주세요.', model_status=status)

        if file and allowed_file(file.filename):
            try:
                ext = file.filename.rsplit('.', 1)[1].lower()
                uid = os.urandom(8).hex()
                original_filename = f"original_{uid}.{ext}"
                colorized_filename = f"colorized_{uid}.{ext}"

                original_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
                colorized_path = os.path.join(app.config['UPLOAD_FOLDER'], colorized_filename)

                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(original_path)

                # DeOldify 컬러화 함수 호출
                success = colorize_image_deoldify(original_path, colorized_path)

                if not success:
                    raise RuntimeError("컬러화 함수 실행 중 오류 발생")

                return render_template('index.html',
                                       original_file=original_filename,
                                       colorized_file=colorized_filename,
                                       model_status=status)

            except Exception as e:
                logging.error(f"처리 중 오류: {e}", exc_info=True)
                return render_template('index.html', error=f"오류: {e}", model_status=status)

    return render_template('index.html', model_status=status, error=error)


@app.route('/uploads/<filename>')
def uploaded_file_route(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# --- 6. 실행 ---
if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    try:
        torch.multiprocessing.set_start_method('spawn', force=True)
    except RuntimeError:
        pass

    app.run(debug=True, use_reloader=False)