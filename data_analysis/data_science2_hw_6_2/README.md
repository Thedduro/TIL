# 📝 MLflow 기본 실험 기록 실습

## 🎯 학습목표
| 학습목표  
- MLflow를 설치하고 간단한 Python 코드를 통해 실험을 기록할 수 있다.  
- 파라미터와 metric을 MLflow Tracking UI에 저장하고 확인할 수 있다.  
- 실험 기록의 기본적인 흐름과 MLflow 로그 함수 사용법을 익힌다.  

| 학습 개념  
MLFlow의 가장 기본적인 기능인 **실험 기록**을 경험해보는 데 중점을 둡니다.  
`mlflow.log_param`, `mlflow.log_metric` 등의 함수를 사용하여 간단한 파라미터와 숫자 metric을 저장하고,  
Tracking UI를 통해 확인하는 과정과 실험 추적의 기본 개념을 이해합니다.  

---

## 📌 문제
| 학습 방향  
김싸피는 머신러닝 엔지니어로서, MLflow로 간단한 파라미터/메트릭 로깅 실습 환경을 구축하는 업무를 맡았습니다.  

1. MLFlow가 설치된 가상환경을 준비합니다.  
2. 간단한 Python 코드(파라미터로 숫자 입력 후 제곱 계산)를 작성합니다.  
3. 코드 내에서 `mlflow.start_run()`, `mlflow.log_param()`, `mlflow.log_metric()`을 사용하여 실험 결과를 기록합니다.  
4. `mlflow ui` 명령어로 Tracking 서버를 실행하고, 브라우저에서 기록된 실험을 확인합니다.  

---

## 📋 요구사항
1. `mlflow`가 설치된 환경에서 실행한 Python 코드 파일을 작성하세요.  
   - 코드 내에서 **최소 10개의 실험과 실행(run)** 을 생성하고 파라미터와 metric을 로깅하세요.  

2. MLflow Tracking 서버를 활성화하여 `http://localhost:5000` 으로 접속하세요.  

3. 기록된 파라미터와 metric이 보이는 **Tracking UI의 메인 화면**을 확인하세요.  

4. 여러 실험과 실행을 비교하여 파라미터와 metric을 비교하세요.  
