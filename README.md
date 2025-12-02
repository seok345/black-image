
# 🎨 AI 흑백 사진 컬러 복원 웹 애플리케이션  
### *DeOldify vs OpenCV — 모델 비교 + 웹 서비스 구현 보고서 (모델 다운로드 링크 포함)*

---

# ⚠️ 작성 규칙  
- 평어체(~이다, ~한다) 사용  
- 경어체 금지  
- 이미지 자료 적극 활용  

---

# 📌 1. 프로젝트 개요

본 프로젝트는 두 가지 AI 채색 방식을 비교한 뒤, 최종적으로 **DeOldify 모델을 기반으로 한 고화질 컬러 복원 웹 서비스**를 구현하는 것이다.

---

# 📌 2. 사용된 두 가지 모델

## 🔵 (A) OpenCV Colorization 모델  
- Caffe 기반  
- 속도 빠름  
- 품질 낮음  
- 고해상도 불가  

필요 파일:
- `colorization_deploy_v2.prototxt`
- `colorization_release_v2.caffemodel`
- `pts_in_hull.npy`

🔗 **OpenCV 공식 모델 다운로드 링크 (Caffe Model)**  
https://github.com/richzhang/colorization/tree/master/models

---

## 🟣 (B) DeOldify (최종 선택 모델)  
- GAN/NoGAN 구조  
- ResNet34 기반  
- 매우 자연스러운 색감  
- 고해상도 복원 가능  
- 웹 서비스와 궁합이 좋음  

필요 파일:  
- `ColorizeArtistic_gen.pth`

🔗 **DeOldify 공식 모델 다운로드 링크**  
- Artistic 모델 (ColorizeArtistic_gen.pth):  
  https://deepai.org/machine-learning-model/colorizer  
- Stable 모델 (ColorizeStable_gen.pth):  
  https://github.com/jantic/DeOldify

---

# 📌 3. 모델 비교

| 항목 | OpenCV 모델 | DeOldify 모델 |
|------|-------------|---------------|
| 색감 품질 | 낮음 | 매우 우수 |
| 고해상도 | 불가 | 가능 |
| 얼굴 복원 | 많이 부족함 | 크게 우수함 |
| 속도 | 매우 빠름 | 상대적으로 느림 |
| 설치 난이도 | 쉬움 | 어려움 (버전 의존성 큼) |
| 웹 서비스 적합성 | 낮음 | 매우 높음 |

---

# 📸 4. 예시 이미지

## OpenCV 모델 실패 사례
<img src="6.png" width="700">

## DeOldify 모델 성공 사례
<img src="4.png" width="700">

---

# 📌 5. 웹 서비스 UI

## 초기 화면  
<img src="1.png" width="700">

## 변환 결과 화면  
<img src="2.png" width="700">

## 컬러 복원 결과  
<img src="3.png" width="700">

---

# 📌 6. 기술적 문제 해결

## 🔧 PyTorch 보안 정책 문제 해결  
PyTorch 2.x에서 `.pth` 파일 로딩 오류 발생 →  
`torch.load()` monkey-patching 후 `weights_only=False` 강제 적용  

## 🔧 FastAI 1.x 환경 복원  
DeOldify 원본이 FastAI 1.x 기반 →  
버전 고정 필요:
```
pip install fastai==1.0.61
```

---

# 📌 7. 설치 및 실행 가이드

## ✔ 가상환경 생성
```
conda create -n colorization python=3.8
conda activate colorization
```

## ✔ 필수 패키지 설치
```
pip install flask numpy opencv-python Pillow werkzeug
pip install deoldify fastai==1.0.61
```

## ✔ 모델 다운로드  
아래 링크에서 모델 파일을 다운로드하고 `models/` 폴더에 넣는다.

### 🔗 **OpenCV Caffe 모델 다운로드**  
https://github.com/richzhang/colorization/tree/master/models

### 🔗 **DeOldify 모델 다운로드(Artistic)**  
https://deepai.org/machine-learning-model/colorizer

---

# 📁 프로젝트 폴더 구조

```
project/
 ├── app.py
 ├── models/
 │     ├── ColorizeArtistic_gen.pth
 │     ├── colorization_release_v2.caffemodel
 │     ├── colorization_deploy_v2.prototxt
 │     └── pts_in_hull.npy
 ├── image/
 ├── static/
 ├── templates/
 └── README.md
```

---

# 📌 8. 결론

OpenCV 모델은 속도가 빠르다는 장점이 있지만 품질적으로 서비스 수준에 적합하지 않다.  
반면, DeOldify는 고품질 복원 능력, 색감, 디테일, 얼굴 복원에서 압도적으로 우수하여  
최종 서비스 모델로 선정되었다.

또한 Flask 기반 웹 UI로 사용자가 흑백 사진을 손쉽게 컬러로 변환할 수 있도록 구현하였다.

---

# ✔ README 파일 생성 완료
