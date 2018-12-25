import json

import requests

data={
    'username':'map',
    'password':'gzshili@map',
    'userType':1,
    'p':'8njq6ZY'
}

res = requests.post('http://www.yunlinye.com//hlxj_test/login',data=data).json()
print(res)