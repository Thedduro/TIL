import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
file_path = 'data/dementia_dataset.csv'
data = pd.read_csv(file_path)

################### 코드 작성 ###################
# 문제 07. 성별(M/F)과 치매 발병 여부(Group)에 따라 뇌 용적 비율(nWBV)의 차이를 Boxplot으로 비교하세요.
sns.boxplot(data=data, x= data['M/F'], y= data['nWBV'], hue= data['Group'])
plt.legend()
###############################################

plt.title("nWBV by Gender and Dementia Group")
plt.xlabel("Gender")
plt.ylabel("nWBV")
plt.show()

################### 코드 작성 ###################
# 문제 08. Group이 ‘Demented’인 사람들의 데이터를 필터링하고, 성별별 치매 발병률을 계산하고, 이를 막대 그래프로 시각화하시오.
F = (data[(data['M/F']=='F')&(data['Group']=='Demented')].shape[0]/data[data['M/F']=='F'].shape[0])*100
M = (data[(data['M/F']=='M')&(data['Group']=='Demented')].shape[0]/data[data['M/F']=='M'].shape[0])*100
sns.barplot(x= ['F','M'], y = [F, M])

###############################################
plt.title('Dementia Incidence Rate by Gender (%)')
plt.xlabel('Gender')
plt.ylabel('Dementia Incidence Rate (%)')
plt.show()

