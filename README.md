# AI 흑백 사진 컬러 복원 웹 애플리케이션 (DeOldify)

딥러닝 모델인 DeOldify와 Flask 웹 프레임워크를 사용하여, 흑백 사진을 고해상도 컬러 사진으로 자동 변환해주는 웹 서비스 프로젝트입니다.

 프로젝트 소개 (Project Overview)

이 프로젝트는 단순히 흑백 이미지를 컬러로 바꾸는 것을 넘어, 과거의 기록을 생생한 현재의 모습으로 복원하는 것을 목표로 합니다. 사용자가 웹 인터페이스를 통해 흑백 사진을 업로드하면, 서버 내부의 AI 모델이 이미지의 맥락(Context)을 분석하여 가장 자연스럽고 예술적인 색상을 입혀줍니다.

# ## 주요 기능

원클릭 자동 복원: 복잡한 설정 없이 사진 업로드만으로 컬러 변환 수행.

고품질 결과물: 최신 딥러닝 기술(GAN)을 활용하여 피부 톤, 풍경 등을 사실적으로 표현.

비교 및 다운로드: 원본과 결과물을 나란히 비교하고, 결과물을 즉시 다운로드 가능.

 왜 DeOldify 모델을 선택했나요? (Model Selection)

초기 개발 단계에서는 전통적인 CNN 기반의 모델(Caffe)을 고려했으나, 다음과 같은 이유로 DeOldify를 최종 선정했습니다.

압도적인 품질 (State-of-the-Art Quality):

기존 모델들은 색상이 칙칙하거나 경계선이 모호한 문제가 있었습니다.

DeOldify는 NoGAN 기술을 도입하여 GAN(생성적 적대 신경망)의 장점인 선명한 디테일과, 지도 학습의 장점인 안정성을 모두 확보했습니다.

'Artistic' 모델의 강점:

본 프로젝트에서 채택한 Artistic 모델은 색감의 다채로움과 흥미로운 디테일을 강조합니다.

단순한 사실 재현을 넘어, 사진에 생동감을 불어넣기에 가장 적합하다고 판단했습니다.

검증된 성능:

ResNet34를 백본(Backbone)으로 하는 U-Net 구조를 사용하여, 이미지의 특징을 깊이 있게 추출하면서도 빠른 처리 속도를 유지합니다.

 시스템 동작 원리 (How It Works)

사용자 입력 (Input):

사용자가 웹 브라우저를 통해 흑백 이미지(JPG, PNG 등)를 업로드합니다.

서버 처리 (Processing):

Flask 서버가 이미지를 수신하고, OpenCV를 통해 모델이 처리할 수 있는 형태로 전처리합니다.

DeOldify AI 모델이 픽셀 단위로 색상 정보를 예측(Inference)합니다. 이때, 이미지의 구조적 특징(질감, 명암)을 유지하면서 색채(Chrominance) 채널을 생성합니다.

결과 출력 (Output):

생성된 색상 정보를 원본의 명도 정보와 합성하여 최종 컬러 이미지를 생성합니다.

결과 페이지에서 원본과 변환된 이미지를 시각적으로 비교하여 보여줍니다.

# ##기술 스택 (Tech Stack)

Language: Python 3.x

Web Framework: Flask

AI Model: DeOldify (Generative Adversarial Networks 기반)

Library: PyTorch, FastAI, OpenCV, NumPy

Frontend: HTML5, CSS3 (Tailwind CSS)

# ## 설치 및 실행 방법 (Installation)

1. 필수 라이브러리 설치

본 프로젝트는 DeOldify와 구버전 FastAI의 호환성을 위해 특정 버전의 라이브러리가 필요합니다.

# 기본 웹 및 이미지 처리 라이브러리
pip install flask numpy opencv-python Pillow werkzeug

# AI 코어 라이브러리 (버전 호환성 중요)
pip install deoldify fastai==1.0.61


참고: PyTorch는 시스템 환경에 맞춰 자동으로 설치되거나, CUDA 사용 시 별도 설치가 필요할 수 있습니다.

2. 프로젝트 실행

프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다.

python app.py


3. 웹 접속

브라우저를 열고 http://127.0.0.1:5000 주소로 접속합니다.

 폴더 구조

Project/
├── app.py               # 메인 Flask 서버 코드 (PyTorch 보안 패치 포함)
├── templates/
│   └── index.html       # 웹 인터페이스 (UI)
├── uploads/             # 업로드된 원본 및 변환 이미지 저장소 (자동 생성)
├── models/              # (선택) 모델 파일 수동 저장소
└── README.md            # 프로젝트 설명서


# ## 트러블슈팅 및 해결 과정

본 프로젝트 개발 중 최신 PyTorch(2.6+) 환경에서 발생한 호환성 문제를 다음과 같이 해결했습니다.

PyTorch 보안 이슈 (WeightsUnpickler error):

문제: 최신 PyTorch는 구형 모델 파일(pickle 방식) 로드 시 보안을 위해 로딩을 차단함.

해결: torch.load 함수에 weights_only=False 옵션을 강제 적용하는 몽키 패치(Monkey Patch) 코드를 app.py에 적용하여 레거시 모델 호환성 확보.

라이브러리 버전 충돌:

문제: fastai 2.x 버전과 DeOldify 간의 호환성 문제 발생.

해결: fastai==1.0.61로 버전을 고정하여 안정적인 실행 환경 구축.
