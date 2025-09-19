import requests  # HTTP 요청을 보내고 응답을 받을 수 있도록 해주는 라이브러리
import xml.etree.ElementTree as ET  # XML 데이터를 파싱(분석)하고 다루기 위한 라이브러리
import pandas as pd  # 데이터프레임을 활용하여 데이터를 효율적으로 처리하기 위한 라이브러리
from datetime import datetime, timedelta  # 날짜 및 시간 계산을 위해 필요한 라이브러리

'''
# 참고사항
공공데이터의 api를 다루는 사이트는 여러 곳이 있습니다.
그 중에서 과제에 해당하는 사이트: https://data.seoul.go.kr 에 가입 후 인증키를 발급받아야 합니다.

버스 api 사이트: https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do
지하철 api 사이트: https://data.seoul.go.kr/dataList/OA-12912/S/1/datasetView.do
각각의 사이트에서 인증키를 받아야 하며 첫 번째 이미지의 인증키 신청을 누르고 두 번째의 내용을 작성합니다.
여기서 사용URL이 헷갈릴 수 있는데, 이건 "API 테스트 및 학습용" 정도로 기입해주시면 인증키를 발급받을 수 있고 이 인증키를 두 개의 사이트에 대해서 발급받고 진행합니다.
'''

# API 키 및 기본 URL 설정 (실제 사용 시 보안상 환경 변수로 관리하는 것이 바람직함)
BUS_API_KEY = "796c76694d6c737738307a654c446c"  # 서울시 버스 교통 데이터 API 키 (빈칸 채우기)
SUBWAY_API_KEY = "546c73634b6c737736394f6f6c7959"  # 서울시 지하철 교통 데이터 API 키 (빈칸 채우기)
BUS_URL = "http://openapi.seoul.go.kr:8088/"  # 서울시 버스 API 기본 URL
SUBWAY_URL = "http://openapi.seoul.go.kr:8088/"  # 서울시 지하철 API 기본 URL

def get_bus_data(date):
    """
    주어진 날짜에 대한 서울시 버스 승하차 데이터를 API에서 가져와 DataFrame으로 변환하는 함수

    Args:
        date (str): YYYYMMDD 형식의 날짜 문자열

    Returns:
        pandas.DataFrame: 버스 데이터가 저장된 데이터프레임
    """
    # API URL 구성 (날짜별 버스 데이터 요청)
    url = f"{BUS_URL}{BUS_API_KEY}/xml/CardBusStatisticsServiceNew/1/1000/{date}"  # ( BUS_URL과 BUS_API_KEY, date를 이용하여 API 요청 URL 생성)

    # API 요청을 보냄
    response = requests.get(url)  # requests 라이브러리를 사용하여 GET 요청 보내기)
    
    # 응답 상태 코드 확인 (200이면 정상)
    print("\n문제 1. 버스 데이터 수집")
    print("답: 상태 코드:", response.status_code)
    print("설명: 상태 코드 200은 API 호출이 성공적으로 완료되었음을 의미합니다.")
    
    # XML 응답 데이터를 파싱
    root = ET.fromstring(response.text)  # API 응답 데이터를 XML 형식으로 변환)

    # 데이터를 저장할 리스트 생성
    bus_data = []
    
    # XML에서 <row> 태그를 찾아 각 데이터 항목을 추출
    for row in root.findall('.//row'):
        bus_data.append({
            '날짜': row.find('USE_YMD').text if row.find('USE_YMD') is not None else '',  # 사용일자
            '노선번호': row.find('RTE_NM').text if row.find('RTE_NM') is not None else '',  # row에서 'RTE_NM' 태그의 텍스트 추출)
            '정류장명': row.find('STTN_NM').text if row.find('STTN_NM') is not None else '',  # row에서 'STTN_NM' 태그의 텍스트 추출)
            '승차인원': int(row.find('GTON_TNOPE').text) if row.find('GTON_TNOPE') is not None else 0,  # 승차 인원
            '하차인원': int(row.find('GTOFF_TNOPE').text) if row.find('GTOFF_TNOPE') is not None else 0  # 하차 인원
        })

    print(f"설명: {date} 날짜의 버스 데이터를 수집하여 리스트에 저장했습니다.")
    
    # 리스트를 데이터프레임으로 변환하여 반환
    return pd.DataFrame(bus_data)


def get_subway_data(date):
    """
    주어진 날짜에 대한 서울시 지하철 승하차 데이터를 API에서 가져와 DataFrame으로 변환하는 함수
    """
    # API URL 구성 (날짜별 지하철 데이터 요청)
    url = f"{SUBWAY_URL}{SUBWAY_API_KEY}/xml/CardSubwayStatisticsServiceNew/1/1000/{date}"  # SUBWAY_URL과 SUBWAY_API_KEY, date를 이용하여 API 요청 URL 생성)
    
    # API 요청을 보냄
    response = requests.get(url)  # requests 라이브러리를 사용하여 GET 요청 보내기)
    
    # 응답 상태 코드 확인 (200이면 정상)
    print("\n문제 2. 지하철 데이터 수집")
    print("답: 상태 코드:", response.status_code)
    print("설명: 상태 코드 200은 API 호출이 성공적으로 완료되었음을 의미합니다.")
    
    # XML 응답 데이터를 파싱
    root = ET.fromstring(response.text)  # API 응답 데이터를 XML 형식으로 변환)

    # 데이터를 저장할 리스트 생성
    subway_data = []
    
    # XML에서 <row> 태그를 찾아 각 데이터 항목을 추출
    for row in root.findall('.//row'):
        subway_data.append({
            '날짜': row.find('USE_YMD').text if row.find('USE_YMD') is not None else '',  
            '노선번호': row.find('SBWY_ROUT_LN_NM').text if row.find('SBWY_ROUT_LN_NM') is not None else '',  
            '역명': row.find('SBWY_STNS_NM').text if row.find('SBWY_STNS_NM') is not None else '',   # row에서 'SBWY_STNS_NM' 태그의 텍스트 추출)
            '승차인원': int(row.find('GTON_TNOPE').text) if row.find('GTON_TNOPE') is not None else 0,  
            '하차인원': int(row.find('GTOFF_TNOPE').text) if row.find('GTOFF_TNOPE') is not None else 0    # row에서 'GTOFF_TNOPE' 태그의 텍스트 추출 후 정수로 변환)
        })

    print(f"설명: {date} 날짜의 지하철 데이터를 수집하여 리스트에 저장했습니다.")
    
    # 리스트를 데이터프레임으로 변환하여 반환
    return pd.DataFrame(subway_data)


def integrate_data(bus_data, subway_data):
    """
    버스 및 지하철 데이터를 하나의 데이터프레임으로 통합하는 함수
    """
    # 버스 데이터에 '교통수단' 컬럼 추가 후 '정류장명'을 '역/정류장명'으로 변경
    bus_data['교통수단'] = '버스'
    bus_data = bus_data.rename(columns={'정류장명': '역/정류장명'})

    # 지하철 데이터에 '교통수단' 컬럼 추가 후 '역명'을 '역/정류장명'으로 변경
    subway_data['교통수단'] = '지하철'
    subway_data = subway_data.rename(columns={'역명': '역/정류장명'})  # ✅ 변경 완료

    # 두 데이터를 합치기
    integrated_df = pd.concat([bus_data, subway_data], ignore_index=True)
    
    print("\n문제 3. 데이터 통합")
    print("답: 버스와 지하철 데이터가 통합되었습니다.")
    print(f"설명: 통합된 데이터의 컬럼은 {integrated_df.columns.tolist()} 입니다.")

    return integrated_df[['교통수단', '날짜', '노선번호', '역/정류장명', '승차인원', '하차인원']]  # ✅ 필요한 컬럼만 반환


def get_data_for_date_range(start_date, end_date):
    """
    주어진 날짜 범위에 대해 버스 및 지하철 데이터를 수집하고 통합하는 함수

    Args:
        start_date (datetime): 데이터 수집 시작 날짜
        end_date (datetime): 데이터 수집 종료 날짜

    Returns:
        pandas.DataFrame: 통합된 전체 데이터프레임
    """
    current_date = start_date
    all_data = []

    while current_date <= end_date:
        date_str = current_date.strftime("%Y%m%d")
        print(f"\n설명: {date_str} 날짜의 데이터를 수집 중입니다.")

        bus_data = get_bus_data(date_str)
        subway_data = get_subway_data(date_str)

        daily_data = integrate_data(bus_data, subway_data)
        all_data.append(daily_data)

        current_date += timedelta(days=1)

    return pd.concat(all_data, ignore_index=True)

def main():
    # 데이터를 수집할 시작 날짜와 종료 날짜를 설정합니다.
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2023, 9, 7)  # 일주일 치 데이터

    # 지정된 날짜 범위에 대한 데이터를 수집하고 통합합니다.
    all_data = get_data_for_date_range(start_date, end_date)

    # 일별 총 승하차 인원을 계산합니다.
    daily_totals = all_data.groupby(['교통수단', '날짜']).agg({
        '승차인원': 'sum',
        '하차인원': 'sum'
    }).reset_index()
    print("\n문제 4. 일별 총 승하차 인원 계산")
    print(daily_totals.head())  # 일별 총 승하차 인원 데이터를 출력합니다.
    print("설명: 일별로 교통수단별 총 승하차 인원을 계산하여 데이터프레임에 저장했습니다.")

    # 노선별 평균 승하차 인원을 계산합니다.
    route_averages = all_data.groupby(['교통수단', '노선번호']).agg({
        '승차인원': 'mean',
        '하차인원': 'mean'
    }).reset_index()
    print("\n문제 5. 노선별 평균 승하차 인원 계산")
    print(route_averages.head())  # 노선별 평균 승하차 인원 데이터를 출력합니다.
    print("설명: 노선별로 평균 승하차 인원을 계산하여 데이터프레임에 저장했습니다.")

    # 결과를 CSV 파일로 저장합니다.
    all_data.to_csv("seoul_transport_data_detailed.csv", index=False, encoding='utf-8-sig')
    daily_totals.to_csv("seoul_transport_daily_totals.csv", index=False, encoding='utf-8-sig')
    route_averages.to_csv("seoul_transport_route_averages.csv", index=False, encoding='utf-8-sig')
    print("\n문제 6. 결과 CSV 파일로 저장")
    print("설명: 데이터를 분석하고, CSV 파일로 저장하여 나중에 참고할 수 있도록 했습니다.")
    print("Data has been saved to CSV files.")


if __name__ == "__main__":
    main()
