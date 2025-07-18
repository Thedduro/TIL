
# Flask 웹앱 버전
from flask import Flask, render_template_string, request
from openai import OpenAI

app = Flask(__name__)

OPENAI_API_KEY = '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'
clint = OpenAI(api_key=OPENAI_API_KEY)

FORM_HTML = '''
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <title>🍱 맞춤 식단 추천</title>
  <style>
    body { background: #f8fafc; }
    .container { max-width: 500px; margin-top: 40px; background: #fff; border-radius: 16px; box-shadow: 0 2px 16px #0001; padding: 32px; }
    h2 { font-weight: bold; margin-bottom: 24px; }
    .form-label { font-weight: 500; }
    .form-label .required { color: #e74c3c; margin-left: 2px; }
    .btn-primary { width: 100%; }
    .alert { margin-bottom: 16px; }
  </style>
  <script>
    function validateForm() {
      let required = ['age','gender','height','weight','goal'];
      let valid = true;
      required.forEach(function(name) {
        let el = document.forms[0][name];
        if (!el.value.trim()) {
          el.classList.add('is-invalid');
          valid = false;
        } else {
          el.classList.remove('is-invalid');
        }
      });
      if (!valid) {
        document.getElementById('form-alert').style.display = 'block';
      } else {
        document.getElementById('form-alert').style.display = 'none';
      }
      return valid;
    }
  </script>
</head>
<body>
  <div class="container">
    <h2>🍱 맞춤 식단 추천</h2>
    <div id="form-alert" class="alert alert-danger" style="display:none;">필수 입력란을 모두 입력해 주세요.</div>
    <form method="post" onsubmit="return validateForm()">
      <div class="mb-3">
        <label class="form-label">나이<span class="required">*</span></label>
        <input name="age" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">성별(남/여)<span class="required">*</span></label>
        <input name="gender" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">키(cm)<span class="required">*</span></label>
        <input name="height" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">몸무게(kg)<span class="required">*</span></label>
        <input name="weight" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">골격근량(kg)</label>
        <input name="muscle" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">체지방량(kg)</label>
        <input name="fat" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">BMI</label>
        <input name="bmi" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">기타 인바디 정보</label>
        <input name="etc" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">질병/복용 중인 약 (있으면)</label>
        <input name="disease" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">목표(다이어트, 벌크업 등)<span class="required">*</span></label>
        <input name="goal" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">알러지/비선호/제외 재료(쉼표로 구분)</label>
        <input name="allergy" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">식단 추천받기</button>
    </form>
  </div>
</body>
</html>
'''

RESULT_HTML = '''
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <title>🍱 맞춤 식단 추천 결과</title>
  <style>
    body { background: #f8fafc; }
    .container { max-width: 800px; margin-top: 40px; background: #fff; border-radius: 16px; box-shadow: 0 2px 16px #0001; padding: 32px; }
    h2 { font-weight: bold; margin-bottom: 24px; }
    h3 { margin-top: 32px; }
    .card { margin-bottom: 24px; border: none; border-radius: 12px; box-shadow: 0 2px 8px #0001; }
    .card-header { background: #f0f4fa; font-weight: 600; font-size: 1.2rem; }
    pre { background: #f6f8fa; border-radius: 8px; padding: 16px; font-size: 1.05rem; }
    .btn { margin-top: 24px; }
    hr { margin: 32px 0; }
  </style>
</head>
<body>
  <div class="container">
    <h2>🍱 맞춤 식단 추천 결과</h2>
    <div class="card border-primary">
      <div class="card-header text-primary">🥗 추천 식단</div>
      <div class="card-body"><pre>{{ diet }}</pre></div>
    </div>
    <div class="card border-warning">
      <div class="card-header text-warning">💊 질병/복용 중인 약 정보</div>
      <div class="card-body"><pre>{{ disease }}</pre></div>
    </div>
    <div class="card border-success">
      <div class="card-header text-success">💪 예상 건강/체중 변화</div>
      <div class="card-body"><pre>{{ prediction }}</pre></div>
    </div>
    <div class="card border-info">
      <div class="card-header text-info">🍅 식단 재료별 영양 정보</div>
      <div class="card-body"><pre>{{ ingredient_info }}</pre></div>
    </div>
    <a href="/" class="btn btn-secondary">다시 입력</a>
  </div>
</body>
</html>
'''

def get_openai_response(messages, clint, model="gpt-4o-mini"):
    response = clint.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form.get('age', '')
        gender = request.form.get('gender', '')
        height = request.form.get('height', '')
        weight = request.form.get('weight', '')
        muscle = request.form.get('muscle', '')
        fat = request.form.get('fat', '')
        bmi = request.form.get('bmi', '')
        etc = request.form.get('etc', '')
        goal = request.form.get('goal', '')
        allergy = request.form.get('allergy', '')

        diet_prompt = f"""
        아래 신체 정보와 목표, 알러지/비선호 재료를 참고해 하루 식단(아침, 점심, 저녁, 간식 포함)을 추천해줘. 각 끼니별로 구체적인 메뉴와 양을 제시하고, 제외해야 할 재료는 반드시 빼줘.
        [신체 정보] 나이: {age}, 성별: {gender}, 키: {height}cm, 몸무게: {weight}kg, 골격근량: {muscle}, 체지방량: {fat}, BMI: {bmi}, 기타: {etc}
        [목표] {goal}
        [알러지/비선호/제외 재료] {allergy}
        답변은 표 형식으로 끼니, 메뉴, 재료, 양을 구분해서 제공해줘.
        """
        messages = [{"role": "user", "content": diet_prompt.strip()}]
        diet = get_openai_response(messages, clint)

        predict_prompt = f"""
        위에서 추천한 식단을 4주간 꾸준히 실천할 경우 예상되는 건강 변화(체중, 체지방, 근육량 등)를 간단히 예측해줘. 신체 정보와 목표를 참고해서 현실적으로 답변해줘.
        [신체 정보] 나이: {age}, 성별: {gender}, 키: {height}cm, 몸무게: {weight}kg, 골격근량: {muscle}, 체지방량: {fat}, BMI: {bmi}, 기타: {etc}
        [목표] {goal}
        """
        messages = [{"role": "user", "content": predict_prompt.strip()}]
        prediction = get_openai_response(messages, clint)

        ingredient_prompt = f"""
        위에서 추천한 식단의 모든 재료별로, 각 재료의 영양 정보(칼로리, 단백질, 탄수화물, 지방, 주요 미네랄/비타민 등)를 표로 정리해줘.
        """
        messages = [{"role": "user", "content": ingredient_prompt.strip()}]
        ingredient_info = get_openai_response(messages, clint)

        return render_template_string(RESULT_HTML, diet=diet, prediction=prediction, ingredient_info=ingredient_info)
    return render_template_string(FORM_HTML)

if __name__ == "__main__":
    app.run(debug=True)
