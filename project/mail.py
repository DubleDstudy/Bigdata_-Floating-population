import requests
s=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlFlpop/1/500/201606')
mail = []
Fml =[]
femail = []
age60 =[]
youngman=[]
tmp=[]
dy=s.json()
d= dict()
for index, data1 in enumerate(dy['InfoTrdhlFlpop']['row']):
    d[index] = data1['TRDAR_CD_NM']
    femail.append(data1['FML_FLPOP_CO'])
    mail.append(data1['ML_FLPOP_CO'])
    tmp.append(data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO'])
    age60.append(data1['AGRDE_60_ABOVE_FLPOP_CO'])
    youngman.append(data1['AGRDE_10_FLPOP_CO'])
    index, data1['ML_FLPOP_CO'],data1['FML_FLPOP_CO']
import matplotlib.pyplot as plt

plt.plot(mail,'bo')
plt.show()