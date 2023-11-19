from django.contrib import admin
from .models import Post, Comment
# 이미 posts 내부에 같은 선상에 있기 때문에 .models로 사용

class CommentInline(admin.TabularInline):
    # TabularInline => 내용, 작성자가 가로 정렬 / StackedInline => 내용, 작성자가 세로 정렬
    model = Comment
    extra = 5 # 기본적인 빈 공간 갯수
    min_num = 3 # 빈 공간의 최솟값
    max_num = 5 # 빈 공간의 최댓값
    verbose_name = '댓글' # 라벨 이름 지정

@admin.register(Post)
# @ 어노테이션을 붙이는 이유? => admin 페이지 커스터마이징 때문?
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)
    # Post 탭의 리스트를 id, content 로 보여줌
    # list_editable = ('content',) # => 모든 게시글의 내용을 그 즉시 수정 가능함
    list_filter = ('created_at', ) 
    # => 날짜별로 조회하는 필터 기능
    search_fields = ('id', 'writer',)
    # => 검색 상자를 활성화하는 기능
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at',)
    # 작성 일자를 read only로 보여줌
    inlines = [CommentInline]
    
    actions = ['make_published']
    
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()
    

# admin.site.register(Comment)


