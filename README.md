
# 🎨 AI 흑백 사진 컬러 복원 웹 애플리케이션  
### *DeOldify 기반 고품질 이미지 컬러 복원 서비스 (업데이트된 프로젝트 구조 반영)*
---

# 📌 1. 프로젝트 개요

본 프로젝트는 AI 기반으로 흑백 사진을 컬러 사진으로 변환하는 웹 서비스이다.  
초기에는 OpenCV Colorization 모델을 사용했으나 품질 문제가 있어  
최종적으로 **DeOldify 모델**을 사용해 고품질 컬러 복원을 제공한다.

---

# 📸 3. OpenCV 모델 실패 사례

OpenCV Colorization 모델은 색감 품질이 낮고 검정 화면 출력 오류가 존재한다.

<div align="center">
<img src="image/6.png" width="700">
</div>

---

# 🟣 4. DeOldify 성공 사례

DeOldify 모델은 자연스러운 색상과 뛰어난 디테일 복원을 제공한다.

<div align="center">
<img src="image/4.png" width="700">
</div>

---

# 📌 5. 웹 서비스 UI 흐름

## ✔ 초기 화면
<div align="center">
<img src="image/1.png" width="700">
</div>

---

## ✔ 업로드 후 처리 화면
<div align="center">
<img src="image/2.png" width="700">
</div>

---

## ✔ 최종 컬러 복원 결과
<div align="center">
<img src="image/3.png" width="700">
</div>

---

# 📌 6. 기술적 문제 해결

## 🔧 PyTorch 2.x 모델 로딩 오류 해결  
- pickle 기반 구조 차단 문제 발생  
- `torch.load()` monkey-patching  
- `weights_only=False` 강제 적용  
- FastAI 객체 Whitelist 등록으로 해결

## 🔧 FastAI 1.x 의존성 해결  
```
pip install fastai==1.0.61
```

---

# 📌 7. 설치 & 실행

### 가상환경 생성
```
conda create -n colorization python=3.8
conda activate colorization
```

### 필수 라이브러리 설치
```
pip install flask numpy opencv-python Pillow werkzeug
pip install deoldify fastai==1.0.61
```

### 모델 다운로드  

#### 🔗 DeOldify 모델 (Artistic)
https://deepai.org/machine-learning-model/colorizer  

#### 🔗 OpenCV 모델(Caffe)
https://github.com/richzhang/colorization/tree/master/models

---
---

# 📌 2. 최종 프로젝트 폴더 구조

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
 │    └── (복원 완료 이미지 저장)
 │
 ├── static/
 │    └── styles.css
 │
 ├── templates/
 │    └── index.html
 │
 ├── uploads/
 │    └── (사용자 업로드 이미지)
 │
 ├── app.py
 ├── model2.py
 └── README.md
```


# 📌 8. 결론

OpenCV 모델은 빠르지만 품질적으로 부족하다.  
DeOldify는 고품질 컬러 복원이 가능해 실제 서비스에 적합하며  
자연스러운 색감, 얼굴 복원 품질이 매우 뛰어나기 때문에 최종 선택 모델이 되었다.

---

