from django.contrib import admin
from .models import Post, Comment
# 이미 posts 내부에 같은 선상에 있기 때문에 .models로 사용

@admin.register(Post)
# @ 어노테이션을 붙이는 이유? => admin 페이지 커스터마이징 때문?
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    # Post 탭의 리스트를 id, content 로 보여줌
    # list_editable = ('content',) # => 모든 게시글의 내용을 그 즉시 수정 가능함
    list_filter = ('created_at', ) 
    # => 날짜별로 조회하는 필터 기능
    search_fields = ('id', 'writer')
    # => 검색 상자를 활성화하는 기능
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    

admin.site.register(Comment)


