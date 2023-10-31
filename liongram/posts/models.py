from django.db import models
from django.contrib.auth import get_user_model

# ORM 기능
# 이 클래스를 가지고 migrations에 명세함, 설정 파일을 만듦
User = get_user_model()

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True) # 필드에 대한 이름 지정
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    # 처음은 to, 두번째는 on_delete(게시글이 삭제됐을 때 댓글도 삭제되는 기능)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)


# python manage.py makemigrations => database 생성?
# python manage.py migrate => 테이블 생성
