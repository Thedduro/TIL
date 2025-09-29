import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 파일 불러오기
file_path = 'data/dementia_dataset.csv'
dementia_data = pd.read_csv(file_path)

# 문제 04. Group이 'Nondemented'이고, M/F가 'F'인 사람들의 MMSE 평균과 중앙값을 계산하세요.
################### 코드 작성 ###################
nondemented_female_mmse_mean = dementia_data[(dementia_data['Group']=='Nondemented')& (dementia_data['M/F']=='F')]['MMSE'].mean() # 비치매 여성들의 MMSE 평균
nondemented_female_mmse_median = dementia_data[(dementia_data['Group']=='Nondemented')& (dementia_data['M/F']=='F')]['MMSE'].median() # 비치매 여성들의 MMSE 중앙값
###############################################
print(f"비치매 여성들의 평균 MMSE: {nondemented_female_mmse_mean}")
print(f"비치매 여성들의 중앙값 MMSE: {nondemented_female_mmse_median}")

# 문제 05. 치매 연관성 데이터에서 이상치와 결측치를 제거한 새로운 데이터 프레임을 만드시오
# MMSE 열에서 결측치가 있는 행을 제거하고, Age 열에서 나이가 18세 미만이거나 100세를 초과하는 승객들을 이상치로 간주하고, 이를 제거한 새로운 데이터프레임을 만드세요.
data = pd.read_csv(file_path)

################### 코드 작성 ###################
# 5-1. MMSE 열에서 결측치가 있는 행 제거
data_cleaned =dementia_data.iloc[dementia_data['MMSE'].dropna().index,:]
###############################################


################### 코드 작성 ###################
# 5-2. Age 열에서 나이가 18세 미만이거나 100세를 초과하는 승객을 제거
data_cleaned = data_cleaned[(data_cleaned['Age'] >= 18) & (data_cleaned['Age'] <= 100)]
###############################################

# 새로운 데이터프레임 출력
print(data_cleaned.info())


# 문제 06. 치매 연관성 데이터에서, Subject ID, MRI ID, Group, M/F, Hand를 제외한 요소의 상관관계를 분석하고, 이를 히트맵 시각화 하시오
# 'Subject ID', 'MRI ID', 'Group', 'M/F', 'Hand' 열을 제외하고 상관관계 계산
################### 코드 작성 ###################
correlation_matrix = data_cleaned.loc[:,(data_cleaned.dtypes != object)==True].corr() # Subject ID, MRI ID, Group, M/F, Hand를 제외한 요소의 상관관계 matrix
###############################################

# 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Dementia Dataset')
plt.show()
