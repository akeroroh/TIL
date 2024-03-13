import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbjah018941453002'
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'SearchTarget': 'book',
    'Output': 'JS',
    'Version': 20131101
}

result = requests.get(API_URL, params=params).json()
print(result)