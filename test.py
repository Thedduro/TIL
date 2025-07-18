
# Flask 웹앱 버전
from flask import Flask, render_template_string, request
from openai import OpenAI

app = Flask(__name__)

OPENAI_API_KEY = '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'
clint = OpenAI(api_key=OPENAI_API_KEY)

FORM_HTML = '''
<h2>맞춤 식단 추천</h2>
<form method="post">
  나이: <input name="age"><br>
  성별(남/여): <input name="gender"><br>
  키(cm): <input name="height"><br>
  몸무게(kg): <input name="weight"><br>
  골격근량(kg): <input name="muscle"><br>
  체지방량(kg): <input name="fat"><br>
  BMI: <input name="bmi"><br>
  기타 인바디 정보: <input name="etc"><br>
  목표(다이어트, 벌크업 등): <input name="goal"><br>
  알러지/비선호/제외 재료(쉼표로 구분): <input name="allergy"><br>
  <input type="submit" value="식단 추천받기">
</form>
'''

RESULT_HTML = '''
<h2>맞춤 식단 추천 결과</h2>
<h3>추천 식단</h3>
<pre>{{ diet }}</pre>
<h3>예상 건강/체중 변화</h3>
<pre>{{ prediction }}</pre>
<h3>식단 재료별 영양 정보</h3>
<pre>{{ ingredient_info }}</pre>
<a href="/">다시 입력</a>
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
