# AI 흑백 사진 컬러 복원 웹 애플리케이션 (DeOldify Web Service)

Deep Learning based Image Colorization Project

흑백 이미지에 생명을 불어넣다: DeOldify와 Flask를 활용한 고해상도 이미지 복원 서비스

## 프로젝트 개요 (Project Overview)

### 1. 배경 및 목적

오래된 흑백 사진은 소중한 역사와 추억을 담고 있지만, 색상 정보의 부재로 인해 당시의 현장감이나 감정을 온전히 느끼기에는 한계가 있습니다. 본 프로젝트는 최신 딥러닝 기술인 Generative Adversarial Networks (GANs), 그중에서도 탁월한 성능을 보여주는 DeOldify 모델을 활용하여 누구나 쉽게 흑백 사진을 고화질의 컬러 사진으로 복원할 수 있는 웹 서비스를 구축하는 것을 목표로 합니다.

### 2. 핵심 가치

접근성(Accessibility): 복잡한 코드를 실행할 필요 없이, 웹 브라우저에서 사진을 업로드하는 것만으로 AI 기술을 활용할 수 있습니다.

심미성(Aesthetics): 단순한 색상 복원을 넘어, 'Artistic' 모델을 적용하여 예술적이고 생동감 넘치는 색감을 구현합니다.

기술적 해결(Problem Solving): 레거시 AI 모델(FastAI v1)과 최신 실행 환경(PyTorch v2) 간의 호환성 문제를 기술적으로 해결하여 안정적인 서비스를 제공합니다.

## 주요 기능 (Key Features)

이미지 업로드 및 전처리: 사용자가 업로드한 다양한 포맷(JPG, PNG)의 이미지를 서버에서 안전하게 수신하고 모델 입력에 맞게 전처리합니다.

AI 기반 자동 채색: DeOldify 모델이 이미지의 객체와 맥락(Context)을 분석하여 픽셀 단위로 색상을 예측 및 합성합니다.

실시간 결과 비교: 원본 흑백 이미지와 변환된 컬러 이미지를 나란히 배치하여 복원 효과를 직관적으로 확인할 수 있습니다.

고해상도 다운로드: 변환된 결과물을 저장이 가능한 고화질 이미지 파일로 제공합니다.

## 기술 스택 (Tech Stack)

본 프로젝트는 안정적인 백엔드 처리와 강력한 AI 성능을 위해 다음과 같은 기술을 사용했습니다.

### Backend & Server

Python 3.x: 프로젝트의 주 언어로, 풍부한 AI 라이브러리 생태계를 활용합니다.

Flask: 가볍고 확장성이 뛰어난 마이크로 웹 프레임워크로, 빠르고 효율적인 이미지 처리 서버를 구축했습니다.

### AI & Deep Learning

DeOldify: NoGAN 기술을 도입하여 GAN의 불안정성을 해결하고 일관된 고품질 채색을 수행하는 핵심 모델입니다. (ResNet34 Backbone 사용)

PyTorch & FastAI: 딥러닝 모델의 학습 및 추론(Inference)을 담당하는 프레임워크입니다.

OpenCV & NumPy: 이미지 데이터의 행렬 연산 및 전처리/후처리를 담당합니다.

### Frontend

HTML5 & CSS3: 시맨틱 마크업과 스타일링을 담당합니다.

Tailwind CSS: 유틸리티 퍼스트 CSS 프레임워크를 사용하여 반응형 디자인과 모던한 UI를 신속하게 구현했습니다.

## 설치 및 실행 가이드 (Installation & Usage)

이 프로젝트는 DeOldify 모델의 특성상 특정 라이브러리 버전과의 의존성이 매우 중요합니다. 아래 절차를 정확히 따라주세요.

### 1. 환경 설정 (Prerequisites)

Python 3.7 이상이 설치된 환경에서 진행하는 것을 권장합니다. 충돌 방지를 위해 가상환경(Virtual Environment) 사용을 추천합니다.

### 가상환경 생성 (예: conda 또는 venv)
conda create -n colorization python=3.8
conda activate colorization


### 2. 필수 라이브러리 설치

프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 의존성 패키지를 설치합니다.

### 1. 웹 서버 및 이미지 처리를 위한 기본 패키지
pip install flask numpy opencv-python Pillow werkzeug

### 2. AI 모델 구동을 위한 핵심 패키지 (버전 준수 필수)
### DeOldify는 FastAI 1.x 버전에 최적화되어 있습니다.
pip install deoldify fastai==1.0.61


주의: GPU(CUDA)를 사용하려면 시스템에 맞는 PyTorch 버전을 확인해야 합니다. 일반적인 CPU 환경에서는 위 명령어로 충분합니다.

### 3. 모델 가중치(Weights) 준비

AI 모델이 학습한 데이터 파일이 필요합니다.

파일명: ColorizeArtistic_gen.pth

다운로드:  모델 다운로드 링크 (DeepAI)

위치: 다운로드한 파일을 프로젝트 폴더 내 models/ 디렉토리에 저장합니다.

### 5. 서비스 이용

웹 브라우저를 열고 http://127.0.0.1:5000에 접속하여 흑백 사진을 업로드하세요.

 디렉토리 구조 (Directory Structure)

Project_Root/
├── app.py               # [핵심] Flask 서버 메인 코드 (보안 패치 및 라우팅 로직)
├── templates/           # [Frontend] HTML 템플릿 파일 저장소
│   └── index.html       # 사용자 인터페이스 (UI) 파일
├── static/              # [Frontend] CSS, JS, 이미지 등 정적 파일
├── uploads/             # [Data] 사용자가 업로드한 원본 및 변환된 이미지 저장소
├── models/              # [Model] DeOldify 학습 모델(.pth) 저장소
│   └── ColorizeArtistic_gen.pth
└── README.md            # 프로젝트 설명서


## 트러블슈팅 및 기술적 챌린지 (Troubleshooting)

개발 과정에서 발생한 주요 기술적 문제와 이를 해결한 과정입니다.

### Issue 1: PyTorch 보안 정책 충돌 (WeightsUnpickler error)

현상: 최신 버전의 PyTorch(2.6+) 환경에서 구형 모델 파일(pickle 방식)을 로드할 때, 보안상의 이유로 functools.partial 등의 내부 객체 로딩이 차단되어 에러 발생.

원인: PyTorch의 torch.load 함수가 기본적으로 weights_only=True로 설정되어 코드 실행을 포함한 객체 로딩을 막음.

해결:

app.py 코드 내에서 torch.load 함수를 오버라이딩(Monkey Patching)하여 강제로 weights_only=False 옵션을 적용.

torch.serialization.add_safe_globals를 사용하여 Recorder, Hook, Conv2d 등 모델에 사용된 클래스들을 안전한 리스트(Allowlist)에 등록하여 호환성 확보.

### Issue 2: 라이브러리 버전 비호환성 (Dependency Hell)

현상: pip install fastai로 최신 버전을 설치할 경우, DeOldify 코드 내부에서 사용하는 모듈 경로와 API가 달라 실행 불가.

해결: fastai==1.0.61로 버전을 명시적으로 고정(Pinning)하여 DeOldify가 의도한 실행 환경을 정확히 재현함.

### 향후 발전 계획 (Future Roadmap)

비디오 컬러 복원: 단일 이미지를 넘어 흑백 동영상 파일(MP4)을 프레임 단위로 변환하여 합치는 기능 추가.

모델 선택 옵션: 'Artistic' 모델 외에 원본을 최대한 보존하는 'Stable' 모델 선택 기능 추가.

클라우드 배포: Docker 컨테이너화를 통해 AWS나 Google Cloud Platform에 배포하여 외부 접속 허용.

## 라이선스 및 크레딧 (License & Credits)

이 프로젝트는 Jason Antic이 개발한 DeOldify 오픈소스 프로젝트를 기반으로 합니다.

본 웹 애플리케이션 코드는 학습 및 포트폴리오 목적으로 작성되었습니다.
