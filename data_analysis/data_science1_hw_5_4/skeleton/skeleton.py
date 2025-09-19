import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import folium

# Selenium: 웹 자동화 프레임워크로, 웹 페이지를 프로그래밍 방식으로 제어하는 데 사용됨.
# 브라우저를 실행하고, 페이지를 이동하며, 요소를 찾고, 클릭하는 등의 동작을 자동화할 수 있음.
# 웹 크롤링, UI 테스트, 자동화된 데이터 입력 등에 활용됨.
# WebDriverWait, expected_conditions(EC)를 활용하여 동적 웹 페이지의 요소가 로드될 때까지 기다릴 수 있음.
#
# Selenium과 BeautifulSoup의 차이점:
# - Selenium은 동적인 웹사이트(자바스크립트 기반 콘텐츠)를 크롤링할 때 사용됨. 브라우저를 직접 실행하여 페이지를 렌더링하고 데이터를 가져올 수 있음.
# - BeautifulSoup은 정적인 HTML을 파싱하는 데 적합하며, Selenium과 달리 브라우저를 실행하지 않음. 주로 requests와 함께 사용하여 HTML 소스를 받아 분석하는 방식으로 동작함.
# - Selenium은 더 강력하지만 속도가 느릴 수 있으며, BeautifulSoup은 빠르지만 동적 요소를 처리할 수 없음.

def setup_driver():
    """Chrome WebDriver 설정 및 초기화"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화 (리눅스 환경에서 필요할 수 있음)
    options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 사용 제한 (리소스 문제 방지)
    
    # TODO: Chrome 드라이버 실행
    driver = webdriver.Chrome(options = options)  # (힌트: options 인자를 전달해야 함)
    
    return driver


def navigate_to_page(driver):
    """TOPIS 서울교통정보 웹사이트로 이동 및 로딩 대기"""
    
    # TODO: 웹사이트 접속 (힌트: .get() 메서드 사용)
    driver.get("https://topis.seoul.go.kr")
    
    # TODO: 페이지 요소 로딩 대기 (힌트: WebDriverWait을 사용하여 특정 요소가 로드될 때까지 기다림)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "contents-area")))  
    print("페이지에 접속했습니다.")


def search_keyword(driver, keyword):
    """검색 창에 키워드를 입력하고 검색 버튼 클릭"""
    print(f"'{keyword}' 정류소 정보를 수집합니다.")
    
    # TODO: 검색 영역 찾기
    contents_area = driver.find_element(By.ID, "contents-area")
    
    # TODO: 검색 입력 필드 찾기 (힌트: CSS_SELECTOR 사용)
    search_box = contents_area.find_element(By.CSS_SELECTOR, "input.int-search")  
    
    search_box.clear()  # 기존 입력값 제거
    search_box.send_keys(keyword)  # 검색어 입력
    
    # TODO: 검색 버튼 찾기
    search_button = contents_area.find_element(By.CSS_SELECTOR, "input.int-btn")
    
    search_button.click()  # 검색 버튼 클릭
    
    # TODO: 검색 결과 로딩 대기
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "asideContent")))  
    print(f"'{keyword}' 검색 결과를 찾았습니다.")


def scrape_bus_stop_data(driver):
    """검색된 버스 정류소 정보를 크롤링하여 DataFrame으로 반환"""
    print("정류소 정보를 수집합니다.")
    try:
        # TODO: 검색 결과 영역 찾기
        aside_content = driver.find_element(By.CLASS_NAME, "asideContent") 
        
        # TODO: 정류소 리스트 찾기 (힌트: find_elements 사용, ID: "resultListBusStn")
        results = aside_content.find_element(By.ID, "resultListBusStn").find_elements(By.TAG_NAME, "li")
        
        data = []
        for result in results:
            try:
                # TODO: 정류소 이름 추출 (힌트: find_element, TAG_NAME 사용)
                name = result.find_element(By.TAG_NAME, "a").text.strip()
                
                # TODO: 정류소 번호 추출 (힌트: 문자열 메서드 split, replace 활용)
                bus_stop_number = name.split("(")[-1].replace(")", "")
                
                data.append([name, bus_stop_number])
            except NoSuchElementException:
                print("일부 정류소 정보를 찾을 수 없습니다.")
        
        # TODO: Pandas DataFrame 생성
        df = pd.DataFrame(data, columns=['정류소명', '정류소번호'])
        print("정류소 정보가 성공적으로 수집되었습니다.")
        return df
    
    except Exception as e:
        print(f"정류소 정보 수집 중 오류 발생: {e}")
        return pd.DataFrame()


def visualize_data(df):
    """수집된 정류소 데이터를 folium을 이용해 지도에 시각화"""
    if df.empty:
        print("시각화할 데이터가 없습니다.")
        return
    # folium: 파이썬 기반 지도 시각화 라이브러리로, OpenStreetMap 및 기타 타일셋을 활용해 지도 상에 데이터를 시각적으로 표현 가능함.
    # 주요 기능: 지도 마커 추가, 폴리곤/라인 오버레이, 팝업 및 툴팁 지원 등
    
    # 서울 강남구 중심 좌표를 기준으로 지도 생성
    # 서울 강남구 중심 좌표를 기준으로 지도 생성
    # 지도 초기화 (힌트: folium.Map 사용, 중심 좌표는 서울 강남구)
    map_center = [37.4979, 127.0276]  
    m = folium.Map(location=map_center, zoom_start=13)

    # TODO: 정류소 데이터를 지도에 마커로 추가 (힌트: for문 사용, folium.Marker 활용)
    for index, row in df.iterrows():
        folium.Marker(
            location=map_center,  # 현재는 임의 좌표 사용
            popup=row['정류소명'],  # 정류소 이름을 팝업으로 표시
            tooltip=row['정류소번호']  # 정류소 번호를 툴팁으로 표시
        ).add_to(m)

    # TODO: 생성된 지도를 HTML 파일로 저장
    m.save("bus_stop_map.html")
    print("정류소 시각화가 완료되었습니다. 'bus_stop_map.html' 파일을 확인하세요.")


def main():
    """메인 실행 함수"""
    driver = setup_driver()  # Chrome 드라이버 설정
    navigate_to_page(driver)  # 웹사이트 이동
    search_keyword(driver, "강남구")  # 강남구 버스 정류소 검색
    df = scrape_bus_stop_data(driver)  # 데이터 수집
    driver.quit()  # 드라이버 종료

    if not df.empty:
        print("\n수집된 정류소 데이터 분석:")
        print(df.head())  # 데이터 확인
        print(f"총 {len(df)}개의 정류소가 수집되었습니다.")

        # TODO: 중복된 정류소 확인
        if df.duplicated(subset=['정류소명']).any():
            print("중복된 정류소가 있습니다.")
        else:
            print("중복된 정류소가 없습니다.")

        # 시각화 실행
        visualize_data(df)
    else:
        print("정류소 데이터 수집에 실패하였습니다.")


if __name__ == "__main__":
    main()
