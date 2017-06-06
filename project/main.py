import requests
s=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlFlpop/1/500/201606')
f=open('example3.csv','w')
mail = []
Fml =[]
femail = []
age60 =[]
youngman=[]
tmp=[]
dy=s.json()
d= dict()
maxi = [0,-1000000]
amin=[0,1000000]
for index, data1 in enumerate(dy['InfoTrdhlFlpop']['row']):
    d[index] = data1['TRDAR_CD_NM']
    femail.append(data1['FML_FLPOP_CO'])
    mail.append(data1['ML_FLPOP_CO'])
    if maxi[1] < data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO']:
        maxi = [data1['TRDAR_CD_NM'],data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO']]
    if amin[1] > data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO']:
        amin = [data1['TRDAR_CD_NM'],data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO']] 
    man=data1['ML_FLPOP_CO']
    woman=data1['FML_FLPOP_CO']
    f.write(str(man))
    f.write(",")
    f.write(str(woman))
    f.write("\n")
    
    tmp.append(data1['ML_FLPOP_CO']-data1['FML_FLPOP_CO'])
    age60.append(data1['AGRDE_60_ABOVE_FLPOP_CO'])
    youngman.append(data1['AGRDE_10_FLPOP_CO'])
    print index, data1['ML_FLPOP_CO'],data1['FML_FLPOP_CO']
f.close()
print "A place where a lot of women go"
print maxi[0]
print "A place where a lot of men go"
print amin[0] 