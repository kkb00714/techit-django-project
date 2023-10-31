from django.db import models

# ORM 기능
# 이 클래스를 가지고 migrations에 명세함, 설정 파일을 만듦

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지') # 필드에 대한 이름 지정
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일')
    view_count = models.IntegerField('조회수')



# python manage.py makemigrations => database 생성?
# python manage.py migrate => 테이블 생성
