import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
file_path = 'data/seoul_traffic_data.csv'
traffic_data = pd.read_csv(file_path)

# 문제 01. 온도와 교통량 간의 관계 분석
def temperature_vs_traffic(traffic_data):
    ################### 코드 작성 ###################
    # Temperature과 Traffic Volume를 보여주는 산점도 그리기
    sns.scatterplot(x = traffic_data['temperature'], y = traffic_data['traffic_volume'])
    ###############################################
    plt.title('Temperature vs Traffic Volume')  # 제목
    plt.xlabel('Temperature (C)')  # x축 레이블
    plt.ylabel('Traffic Volume')  # y축 레이블
    plt.show()

    ################### 코드 작성 ###################
    # 상관 계수 계산
    # corr()으로 메트릭스 계산 후 필요한 부분 저장
    correlation = traffic_data[['temperature','traffic_volume']].corr().loc['temperature','traffic_volume']
    ###############################################
    print(f"Correlation coefficient between temperature and traffic volume: {correlation:.4f}")


# 문제 02. 강수량과 평균 속도 간의 관계 분석
def precipitation_vs_avg_speed(traffic_data):
    ################### 코드 작성 ###################
    # 평균 속도 계산
    avg_speed_rainy = traffic_data[traffic_data['precipitation'] >= 0.2]['avg_speed'].mean() # 비 오는 날의 평균 속도
    avg_speed_non_rainy = traffic_data[traffic_data['precipitation'] < 0.2]['avg_speed'].mean() # 비 오지 않는 날의 평균 속도
    ###############################################
    print(f"Average speed on rainy days: {avg_speed_rainy:.2f} km/h")
    print(f"Average speed on non-rainy days: {avg_speed_non_rainy:.2f} km/h")
    
# 문제 03. 요일별 교통량 패턴 분석
def day_of_week_vs_traffic(traffic_data):
    ################### 코드 작성 ###################
    # 요일별 평균 교통량 계산하여 막대그래프로 시각화
    sns.barplot(data=traffic_data, x=traffic_data['day_of_week'], y= traffic_data['traffic_volume'])
    ###############################################
    plt.xticks(rotation = 90)
    plt.title('Average Traffic Volume per Day of the Week')  # 제목
    plt.xlabel('Day of Week (0=Mon, 6=Sun)')  # x축 레이블
    plt.ylabel('Average Traffic Volume')  # y축 레이블
    plt.show()
    # 주말과 평일 교통량 비교
    ################### 코드 작성 ###################
    avg_weekend_traffic = traffic_data[traffic_data['is_weekend'] == 1]['traffic_volume'].mean() # 주말의 평균 교통량
    avg_weekday_traffic = traffic_data[traffic_data['is_weekend'] == 0]['traffic_volume'].mean() # 평일의 평균 교통량
    ###############################################

    print(f"Average weekend traffic: {avg_weekend_traffic:.2f}")
    print(f"Average weekday traffic: {avg_weekday_traffic:.2f}")

# Execute the functions
temperature_vs_traffic(traffic_data)
precipitation_vs_avg_speed(traffic_data)
day_of_week_vs_traffic(traffic_data)