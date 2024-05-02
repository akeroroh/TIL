from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    fixed_price = models.BooleanField()

    @classmethod
    def insert_data(cls):
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        params = {
            'ttbkey': 'ttbjah018941453002',
            'QueryType': 'ItemNewAll',
            'MaxResults': '50',
            'start': '1',
            'SearchTarget': 'Book',
            'output': 'JS',
            'Version': '20131101',
        }
        response = requests.get(API_URL, params=params).json()
        data = response['item']
        
        for item in data:
            my_model = cls(isbn=item['isbn'], author=item['author'], title=item['title'], fixed_price=item['fixedPrice'])
            my_model.save()

