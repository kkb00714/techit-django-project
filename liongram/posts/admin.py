from django.contrib import admin
from .models import Post, Comment
# 이미 posts 내부에 같은 선상에 있기 때문에 .models로 사용

admin.site.register(Post)
admin.site.register(Comment)

