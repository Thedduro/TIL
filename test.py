
import openai

def get_openai_response(messages, api_key, model="gpt-3.5-turbo"):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message["content"].strip()

def main():
    import getpass
    print("[맞춤 식단 추천 프로그램]")
    api_key = getpass.getpass("OpenAI API Key 입력: ")

    # 1. 신체 스펙 및 인바디 입력
    print("\n[1단계] 신체 정보 및 최근 인바디 결과 입력")
    age = input("나이: ")
    gender = input("성별(남/여): ")
    height = input("키(cm): ")
    weight = input("몸무게(kg): ")
    muscle = input("골격근량(kg, 없으면 Enter): ")
    fat = input("체지방량(kg, 없으면 Enter): ")
    bmi = input("BMI(없으면 Enter): ")
    etc = input("기타 참고할 인바디 정보(없으면 Enter): ")

    # 2. 목표 선택
    print("\n[2단계] 목표 선택 (예: 다이어트, 벌크업, 컷팅 등)")
    goal = input("목표: ")

    # 3. 알러지/비선호/제외 재료 입력
    print("\n[3단계] 알러지/비선호/제외 재료 입력 (쉼표로 구분, 없으면 Enter)")
    allergy = input("알러지/비선호/제외 재료: ")

    # 4. 식단 제공 (OpenAI 프롬프트)
    print("\n[4단계] 맞춤 식단 생성 중...")
    diet_prompt = f"""
    아래 신체 정보와 목표, 알러지/비선호 재료를 참고해 하루 식단(아침, 점심, 저녁, 간식 포함)을 추천해줘. 각 끼니별로 구체적인 메뉴와 양을 제시하고, 제외해야 할 재료는 반드시 빼줘.
    [신체 정보] 나이: {age}, 성별: {gender}, 키: {height}cm, 몸무게: {weight}kg, 골격근량: {muscle}, 체지방량: {fat}, BMI: {bmi}, 기타: {etc}
    [목표] {goal}
    [알러지/비선호/제외 재료] {allergy}
    답변은 표 형식으로 끼니, 메뉴, 재료, 양을 구분해서 제공해줘.
    """
    messages = [{"role": "user", "content": diet_prompt.strip()}]
    diet = get_openai_response(messages, api_key)
    print("\n[추천 식단]")
    print(diet)

    # 5. 식단 기반 건강/체중 예측
    print("\n[5단계] 식단을 기반으로 건강 및 체중 변화 예측 중...")
    predict_prompt = f"""
    위에서 추천한 식단을 4주간 꾸준히 실천할 경우 예상되는 건강 변화(체중, 체지방, 근육량 등)를 간단히 예측해줘. 신체 정보와 목표를 참고해서 현실적으로 답변해줘.
    [신체 정보] 나이: {age}, 성별: {gender}, 키: {height}cm, 몸무게: {weight}kg, 골격근량: {muscle}, 체지방량: {fat}, BMI: {bmi}, 기타: {etc}
    [목표] {goal}
    """
    messages = [{"role": "user", "content": predict_prompt.strip()}]
    prediction = get_openai_response(messages, api_key)
    print("\n[예상 건강/체중 변화]")
    print(prediction)

    # 6. 식단 재료 정보 제공
    print("\n[6단계] 식단 재료 정보 제공 중...")
    ingredient_prompt = f"""
    위에서 추천한 식단의 모든 재료별로, 각 재료의 영양 정보(칼로리, 단백질, 탄수화물, 지방, 주요 미네랄/비타민 등)를 표로 정리해줘.
    """
    messages = [{"role": "user", "content": ingredient_prompt.strip()}]
    ingredient_info = get_openai_response(messages, api_key)
    print("\n[식단 재료별 영양 정보]")
    print(ingredient_info)

if __name__ == "__main__":
    main()
