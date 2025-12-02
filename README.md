# AI 흑백 사진 컬러 복원 보고서 (확장본)

이 보고서는 사용자가 제공한 실제 UI 캡처 이미지와 예시 입력 사진을 포함하여 OpenCV vs DeOldify 모델 비교, 웹 UI 동작 흐름, 프로젝트 구조 등을 종합적으로 정리한 문서이다.

---

## 📌 Q1. 흑백 → 컬러 복원 품질 비교 (모델 성능 분석)

### 🔹 입력된 흑백 이미지 예시
<img src="image/q1_input.png" width="600">

### 🔹 DeOldify 복원 결과 예시
<img src="image/q1_output.png" width="600">

(※ 실제 이미지는 사용자가 제공한 예시 이미지에 맞게 교체 가능)

---

## 📌 Q2. 웹 UI 캡처 기반 흐름 설명

### 1) 메인 업로드 화면
<img src="image/ui_main.png" width="700">

**설명:**  
사용자가 이미지를 업로드하고 ‘컬러 변환 시작하기’ 버튼을 눌러 변환을 시작한다.

---

### 2) 로딩 화면 (AI 처리 중)
<img src="image/ui_loading.png" width="700">

**설명:**  
DeOldify 모델이 GPU/CPU 환경에서 이미지에 대한 색 정보를 생성한다.  
처리 시간: 약 10~30초

---

### 3) 변환 결과 비교 화면
<img src="image/ui_compare1.png" width="700">
<img src="image/ui_compare2.png" width="700">
<img src="image/ui_compare3.png" width="700">

**설명:**  
흑백(original) 이미지와 컬러(colorized) 이미지가 나란히 표시되며 다운로드 기능도 제공한다.

---

## 📌 Q3. 추가 예시 이미지 활용 (풍경/인물)

### 🔹 풍경 이미지 컬러 복원
<img src="image/landscape_bw.png" width="700">
<img src="image/landscape_color.png" width="700">

### 🔹 도시 이미지 컬러 복원
<img src="image/city_bw.png" width="700">
<img src="image/city_color.png" width="700">

### 🔹 인물 사진 복원
<img src="image/portrait_bw.png" width="600">
<img src="image/portrait_color.png" width="600">

---

## 📌 프로젝트 구조 (최종)

```
Colorize-App/
├── app.py
├── model2.py
├── models/
│   ├── ColorizeArtistic_gen.pth
│   └── ColorizeStable_gen.pth
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
