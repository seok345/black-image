
# 🎨 AI 흑백 사진 컬러 복원 웹 애플리케이션  
### *OpenCV vs DeOldify —

---

# 📌 1. 프로젝트 개요

흑백 사진은 색상이 없어 당시의 분위기와 감정을 충분히 전달하지 못한다.  
이 프로젝트는 **흑백 이미지를 AI 기반으로 컬러 복원하는 웹 서비스**를 구축하는 것을 목표로 한다.

초기에는 OpenCV Colorization 모델을 사용했으나  
품질적 한계가 명확했기 때문에  
**최종적으로 DeOldify GAN 모델**을 기반으로 완성도 높은 서비스를 구현하였다.

---

# 📌 2. 모델 비교 (OpenCV vs DeOldify)

| 항목 | OpenCV Colorization | DeOldify |
|------|---------------------|----------|
| 모델 구조 | Caffe 기반 CNN | GAN/NoGAN 기반 + ResNet34 |
| 색감 품질 | 탁함, 단순 | 자연스러움, 생동감 |
| 디테일 | 부족함 | 얼굴·피부·재질 복원 뛰어남 |
| 해상도 | 낮은 해상도 권장 | 고해상도 처리 가능 |
| 속도 | 매우 빠름 | 느림 |
| 문맥 이해 | 거의 없음 | 우수함 |
| 서비스 활용성 | 낮음 | 매우 높음 |
| 안정성 | 검정 화면 오류 빈번 | 안정적 결과 |

---

# 📌 3. OpenCV Colorization 모델 상세 소개 (확장 설명)

OpenCV Colorization은 Berkeley AI Research(BAR)의 연구로 개발된 모델이다.  
흑백 이미지의 **윤곽·텍스처를 기반으로 주변부 색을 예측하는 방식**이다.

### 🧩 OpenCV 모델 동작 방식
1. 흑백 이미지를 **Lab 색공간(L, a, b)** 형태로 변환  
2. L 채널만 신경망에 입력  
3. 신경망은 a, b 채널 색상값을 예측  
4. L + ab를 합쳐 최종 컬러 이미지 생성  

### ⚠ OpenCV 방식의 근본적 한계
- 문맥 이해 능력이 없다  
- 얼굴·피부·배경과 같은 의미적 구조를 파악하지 못한다  
- 고해상도 처리 시 오류가 증가한다  
- 색상 계산이 단순해 **단색으로 뒤덮이거나 검정 출력**이 자주 발생한다  
- GAN 기반 모델들에 비해 복원 품질이 낮다  

---

# 📸 OpenCV 모델 실패 사례 (이미지 + 수정된 설명)

<div align="center">
<img src="image/6.png" width="700">
</div>

### ❌ 이미지 6.png 설명 (확장본)

이 이미지는 OpenCV Colorization 모델이 **색상 복원에 실패한 대표 사례**이다.

- 전체 이미지가 검정/회색으로 출력  
- a/b 채널이 제대로 생성되지 않아 색공간 합성 실패  
- 텍스처·윤곽 인식까지만 수행하고 의미 이해를 못함  
- 복잡한 얼굴·배경·피부톤을 분류하지 못해 모델 계산이 붕괴됨  

> OpenCV 기반 모델은 필터 수준의 색 도포 그 이상을 수행하기 어렵다.  
> 실서비스용 컬러 복원에 사용하기에는 품질이 부족하다.

---

# 📌 4. DeOldify 모델 소개 (이미지 + 설명)

<div align="center">
<img src="image/4.png" width="700">
</div>

DeOldify는 GAN 기반 NoGAN 기술을 적용해  
사진의 **사람, 자연, 배경, 재질, 빛의 흐름까지 이해하며 색을 생성하는 모델**이다.

### ✔ DeOldify 장점  
- 자연스러운 색감  
- 얼굴·피부톤 복원 능력이 매우 뛰어남  
- 높은 해상도에서도 안정적  
- 실제 사진처럼 생생한 결과 제공  

> 서비스 품질 측면에서 OpenCV보다 월등히 우수하여 최종 채택되었다.

---

# 📌 5. 웹 서비스 UI 흐름

## ✔ 초기 화면  
<div align="center">
<img src="image/1.png" width="700">
</div>

---

## ✔ 처리 화면  
<div align="center">
<img src="image/2.png" width="700">
</div>

---

## ✔ 복원 결과 화면  
<div align="center">
<img src="image/3.png" width="700">
</div>

---

# 📌 6. 시스템 구조도 (설명 + 이미지)

<div align="center">
<img src="image/7.png" width="750">
</div>

---

# 📌 7. 모델 다운로드 링크

### 🔗 DeOldify 모델 다운로드  
- Artistic: https://deepai.org/machine-learning-model/colorizer  
- Stable: https://github.com/jantic/DeOldify  

### 🔗 OpenCV(Caffe) 모델 다운로드  
https://github.com/richzhang/colorization/tree/master/models

---

# 📌 8. 기술적 문제 해결 요약

## PyTorch 2.x 모델 로딩 문제 해결  
- pickle 객체 제한으로 인해 DeOldify 로딩 실패  
- `torch.load()` monkey-patching  
- `weights_only=False` 적용  
- fastai 관련 클래스 safe globals 등록  

## FastAI 버전 호환  
- DeOldify는 FastAI 1.x 기반  
- 최신 FastAI와 호환되지 않아 버전 고정 필요  
```
pip install fastai==1.0.61
```

---

# 📌 9. 설치 및 실행

## 가상환경
```
conda create -n colorization python=3.8
conda activate colorization
```

## 패키지 설치
```
pip install flask numpy opencv-python Pillow werkzeug
pip install deoldify fastai==1.0.61
```

---

# 📌 10. 프로젝트 구조

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

