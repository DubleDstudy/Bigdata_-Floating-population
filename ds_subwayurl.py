import os
import mylib
import urlparse

keyPath=os.path.join(os.getcwd(), 'key.properties')
key_dict=mylib.getKey(keyPath)
KEY=str(key_dict['dataseoul'])
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(1000)
LINE_NUM=str(1)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url