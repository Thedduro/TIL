# 📊 모델 성능 평가 (Confusion Matrix & Metrics)

## 🎯 목표
| 학습목표  
- 모델의 예측 결과를 분석하기 위해 혼동 행렬(confusion matrix)을 생성하는 방법을 학습한다.  
- 정확도(Accuracy), 정밀도(Precision), 재현율(Recall), F1-score 등의 평가 지표를 계산하는 능력을 기른다.  
- 각 클래스별 성능을 개별적으로 평가하고 해석하는 방법을 익힌다.  

| 학습개념  
- `confusion_matrix()`: 모델이 예측한 값과 실제값을 비교하여 혼동 행렬을 생성하는 함수  
- `accuracy_score()`: 모델이 올바르게 예측한 비율을 계산하는 함수  
- `precision_score()`, `recall_score()`, `f1_score()`: 개별 클래스에 대한 정밀도, 재현율, F1-score를 계산하는 함수  
- `classification_report()`: 모델의 전체 성능을 요약하여 출력하는 함수  

---

## 📌 문제
| 지문  
김싸피는 데이터 분석가로서, AI 모델의 예측 성능을 평가해야 합니다.  
모델이 교통사고 발생 여부를 예측했으며, 상급자가 해당 모델의 성능을 분석할 것을 요청했습니다.  

이를 위해 혼동 행렬을 생성하고, 정확도, 정밀도, 재현율, F1-score를 계산하여 모델의 성능을 평가하세요.  
또한, 각 클래스(0=사고 없음, 1=사고 발생)에 대한 개별적인 성능 지표를 분석하세요.  

---

## 🛠️ 절차
1. `confusion_matrix()`를 사용하여 혼동 행렬을 생성한다.  
2. `accuracy_score()`를 사용하여 모델의 전체 정확도를 계산한다.  
3. `precision_score()`, `recall_score()`, `f1_score()`를 사용하여 각 클래스(0과 1)에 대한 개별 성능 지표를 계산한다.  
4. `classification_report()`를 사용하여 모델의 전체 평가 결과를 출력한다.  

---

## 📋 요구사항
- `confusion_matrix()`를 사용하여 모델의 혼동 행렬을 생성하고 출력해야 합니다.  
- `accuracy_score()`를 사용하여 모델의 전체 정확도를 계산하고 출력해야 합니다.  
- `precision_score()`, `recall_score()`, `f1_score()`를 사용하여 각 클래스별 성능을 개별적으로 계산하고 출력해야 합니다.  
- `classification_report()`를 사용하여 전체 평가 지표를 요약하고 출력하세요.  
