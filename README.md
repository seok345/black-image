
# 🎨 AI 흑백 사진 컬러 복원 웹 애플리케이션  
## **OpenCV vs DeOldify: 흑백 사진에 숨결을 불어넣다**

---

# 📌 1. 프로젝트 개요

오래된 흑백 사진은 시간의 흐름을 간직하고 있지만, 색상이 없다는 이유만으로  
당시의 생생한 분위기와 감정을 온전히 전달하지 못하는 경우가 많다.  

이를 해결하기 위해 본 프로젝트는 **딥러닝 기반 컬러 복원 기술**을 적용하여  
흑백 이미지를 **고품질 컬러 이미지**로 복원하는 웹 애플리케이션을 개발하였다.

초기에는 가벼운 모델인 **OpenCV Colorization**을 활용했지만  
색 번짐, 칙칙한 색감, 검정 화면 오류 등 명확한 한계가 드러났다.

따라서 최종적으로 GAN 기반의 **DeOldify** 모델을 채택하여  
보다 자연스럽고 사실적인 컬러 복원을 제공하는 서비스를 구축했다.

---

# 📌 2. 모델 비교 분석 (OpenCV vs DeOldify)

| 항목 | **OpenCV Colorization** | **DeOldify (최종 채택)** |
|------|-------------------------|---------------------------|
| 핵심 기술 | Caffe 기반 CNN | GAN (NoGAN) + ResNet 기반 |
| 학습 방식 | L 채널 입력 → ab 채널 예측 | Generator + Discriminator 경쟁 학습 |
| 색감 품질 | 단조롭고 칙칙함 | 자연스러움 + 색감 풍부 |
| 디테일 | 낮음 | 피부·피부결·물체 질감 뛰어남 |
| 문맥 이해 | 부족 | 매우 우수 |
| 해상도 | 낮은 해상도 적합 | 고해상도 지원 |
| 속도 | 매우 빠름 | 다소 느림 |
| 안정성 | 검정 화면 등 오류 발생 | 안정적 결과 |

---

# 📌 3. OpenCV Colorization: 한계와 교훈

OpenCV Colorization 모델은 **Lab 색공간 기반 신경망**으로 동작한다.

### 🧩 동작 원리
1. 이미지를 Lab 색공간으로 변환  
2. L(밝기) 채널만 모델에 입력  
3. a·b 채널(색상) 값 예측  
4. L + ab 결합 → 컬러 이미지 생성  

이 방식은 간단하고 빠르지만  
**이미지의 의미나 문맥을 이해하지 못한다는 근본적 한계**가 있다.

---

# 📸 OpenCV 실패 사례

<div align="center">
<img src="image/6.png" width="700" alt="OpenCV Colorization 실패 사례">
</div>

### ❗ 문제점 설명 (확장본)

- 전체가 칙칙한 회색 톤으로 처리됨  
- 피부, 배경, 의류 색감이 전혀 반영되지 않음  
- 복잡한 패턴이나 객체를 이해하지 못하고 텍스처 기반 추론만 수행  
- 일부 경우 **완전히 검정색 이미지를 출력하는 오류**도 발생함  

→ 결론적으로 OpenCV는 “색을 칠하는 수준”에 불과하며  
실제 서비스에서 사용할 만한 품질을 제공하지 못한다.

---

# 📌 4. DeOldify: 혁신적인 컬러 복원 기술

<div align="center">
<img src="image/4.png" width="700" alt="DeOldify 모델 소개 이미지">
</div>

DeOldify는 GAN 기반 기술을 적용하여  
흑백 사진의 구조, 인물, 배경 등을 모두 고려한 **문맥 기반 색상 복원**을 수행한다.

### ✔ DeOldify 주요 특징

- **탁월한 문맥 이해 능력**  
- **NoGAN 학습 기법**으로 안정적 훈련  
- **고해상도 지원**  
- **인물 사진 복원에 매우 강함**  
- Artistic / Stable 두 가지 모델 제공  

본 프로젝트에서는 색감 표현이 뛰어난 **Artistic 모델**을 사용했다.

---

# 📌 5. 웹 서비스 사용 흐름 (UI/UX)

## 🖼️ 1) 메인 화면 (파일 업로드)
<div align="center">
<img src="image/1.png" width="700" alt="메인 화면">
</div>

---

## 🎨 2) 흑백 vs AI 컬러 이미지 비교
<div align="center">
<img src="image/2.png" width="700" alt="이미지 비교 화면">
</div>

---

## 💾 3) 고화질 복원 결과 다운로드
<div align="center">
<img src="image/3.png" width="700" alt="결과 다운로드 화면">
</div>

---

# 📌 6. 시스템 아키텍처

<div align="center">
<img src="image/7.png" width="750" alt="시스템 아키텍처 다이어그램">
</div>

### 구성 요소
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **AI Model**: DeOldify (PyTorch + FastAI)  

---

# 📌 7. 모델 다운로드 및 설정

## 🔥 DeOldify 모델 (필수)
- Artistic 모델:  
  https://deepai.org/machine-learning-model/colorizer  
- Stable 모델:  
  https://github.com/jantic/DeOldify  

→ 다운로드한 `.pth` 파일을 **models/** 폴더에 넣는다

---

## 📌 OpenCV 모델 (참고용)
https://github.com/richzhang/colorization/tree/master/models

(본 프로젝트에서는 사용하지 않음)

---

# 📌 8. 트러블슈팅 (Troubleshooting)

### ❗ PyTorch 2.x + FastAI 1.x 호환성 문제  
- pickle 로딩 보안 제한  
- fastai 객체 구조 변경  

✔ 해결  
- `torch.load()` monkey patching  
- `weights_only=False` 적용  
- fastai 클래스 safe_globals 등록  

### ❗ 메모리 부족(OOM)  
- 고해상도 이미지 처리 시 GPU 메모리 부족 발생  
✔ 해결:  
- render_factor 조절  
- CPU 모드 fallback  

---

# 📌 9. 설치 및 실행 가이드

## 1️⃣ 환경 설정
```
conda create -n colorization python=3.8
conda activate colorization
```

## 2️⃣ 의존성 설치
```
pip install flask numpy opencv-python Pillow werkzeug
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install fastai==1.0.61 deoldify
```

## 3️⃣ 실행
```
python app.py
```
접속:  
http://127.0.0.1:5000/

---

# 📌 10. 프로젝트 디렉토리 구조

```
Colorize-App/
├── app.py
├── model2.py
├── models/
│   └── ColorizeArtistic_gen.pth
├── model/
│   ├── colorization_deploy_v2.prototxt
│   ├── colorization_release_v2.caffemodel
│   └── pts_in_hull.npy
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── uploads/
├── result_images/
└── README.md
```

---

# ✨ 완료  
모델 비교 + 확장된 OpenCV 설명 + 이미지 + 전체 구성 포함한 README 파일 생성됨.
