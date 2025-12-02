
# 🎨 AI 흑백 사진 컬러 복원 웹 애플리케이션  
### *DeOldify 기반 고품질 이미지 컬러 복원 서비스 

---

# 📌 1. 프로젝트 개요

흑백 사진은 색상이 없어 감정 전달력이 떨어진다.  
이 프로젝트는 **흑백 사진을 자동으로 컬러 복원하는 AI 웹 서비스**를 구현하는 것을 목표로 한다.  

초기에는 OpenCV 기반 모델을 실험했으나 품질적 한계가 명확했으며,  
최종적으로 **DeOldify 모델을 기반으로 한 고해상도 복원 서비스**로 전환하였다.

---

# 📌 2. OpenCV Colorization 모델 상세 소개 (확장 설명)

OpenCV Colorization 모델은 Berkeley 연구팀의 딥러닝 기반 색채화 모델로,  
기본적으로 **Lab 색공간 변환 + Caffe 기반 신경망 구조**로 이루어져 있다.

이 모델은 *이미지의 패턴(Edge, Texture)*을 기반으로 주변부 색상을 예측하는 방식이며,  
GAN 기반 모델들과 달리 ‘문맥 이해(Context Understanding)’ 기능이 매우 약하다.

### 🧩 OpenCV 모델의 동작 방식
1. 입력 이미지를 **그레이스케일 → Lab 색공간으로 변환**  
2. L(Lightness) 채널만 모델에 입력  
3. 모델이 a, b 색상 채널을 예측  
4. L + ab 채널을 합쳐 다시 BGR 이미지로 변환  

### ⚠️ 근본적 한계
- 얼굴, 하늘, 피부, 물체 재질 등 **의미 기반 분석이 불가능**  
- 큰 객체에서는 색이 일정하게 퍼지지 않고 얼룩짐(Blotchy Artifacts) 발생  
- 해상도가 높아질수록 품질이 크게 악화됨  
- 최신 GPU 환경에서 속도는 빠르지만 **결과 품질이 낮아 실사용 불가**

---

# 📸 OpenCV 모델 실패 사례 (이미지 + 수정된 설명)

<div align="center">
<img src="image/6.png" width="700">
</div>

### ❌ 이미지 6.png — 상세 문제 설명 (업데이트됨)

위 출력 사례는 OpenCV 기반 Colorization 모델이 **색 추론에 실패한 전형적인 모습**이다.  

- 이미지 전체가 **검정 또는 회색으로 출력**되며  
- 모델이 a/b 색 공간 값을 제대로 생성하지 못할 때 발생한다  
- 특히 인물이 중앙에 있는 사진에서 자주 발생하며  
- 배경·피부·옷 등의 복잡한 패턴을 분류하지 못해 색상 채널 계산이 무너진다  

결과적으로 OpenCV 방식은 “색상 필터를 채우는 수준”에서 크게 벗어나지 못해  
**완전한 AI 색 복원이 불가능한 구조적 한계**를 가진다.

---

# 📌 3. DeOldify 모델 성공 사례 (이미지 + 설명)

<div align="center">
<img src="image/4.png" width="700">
</div>

DeOldify는 GAN 기반 NoGAN 기법을 사용하여  
사진의 의미·형태·질감을 인식하고 색을 자연스럽게 생성한다.

- 얼굴 복원 능력 우수  
- 배경·의류·피부톤이 실제처럼 복원  
- 고해상도 이미지에서도 높은 품질을 유지  
- 실사용 서비스에 적합한 컬러 재현 성능  

---

# 📌 4. 웹 서비스 UI 흐름

## ✔ 초기 화면  
<div align="center">
<img src="image/1.png" width="700">
</div>

---

## ✔ 처리 중 화면  
<div align="center">
<img src="image/2.png" width="700">
</div>

---

## ✔ 최종 컬러 복원 결과  
<div align="center">
<img src="image/3.png" width="700">
</div>

---

# 📌 5. 동작 구조 (설명 + 이미지)

<div align="center">
<img src="image/7.png" width="750">
</div>

---

# 📌 6. 모델 다운로드 링크

### 🔗 DeOldify 모델 (최종 선택)
- Artistic 모델: https://deepai.org/machine-learning-model/colorizer  
- Stable 모델: https://github.com/jantic/DeOldify  

### 🔗 OpenCV(Caffe) 모델 (참고용)
https://github.com/richzhang/colorization/tree/master/models

---

# 📌 7. 기술적 문제 해결 요약

## PyTorch 2.x 로딩 문제 해결  
- pickle 객체 차단 → DeOldify 모델 로딩 불가  
- `torch.load()` monkey-patching  
- `weights_only=False`로 해결  

## FastAI 1.x 버전 고정
```
pip install fastai==1.0.61
```

---

# 📌 8. 설치 및 실행 가이드

## 가상환경
```
conda create -n colorization python=3.8
conda activate colorization
```

## 라이브러리 설치
```
pip install flask numpy opencv-python Pillow werkzeug
pip install deoldify fastai==1.0.61
```

---

# 📌 9. 프로젝트 폴더 구조 (최종)

```
PythonProject11/
 ├── model/
 │    ├── colorization_deploy_v2.prototxt
 │    ├── colorization_release_v2.caffemodel
 │    ├── places2.prototxt
 │    └── pts_in_hull.npy
 │
 ├── models/
 │    └── ColorizeArtistic_gen.pth
 │
 ├── result_images/
 ├── static/
 │    └── styles.css
 ├── templates/
 │    └── index.html
 ├── uploads/
 ├── app.py
 ├── model2.py
 └── README.md
```

---


