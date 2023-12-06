from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
# settings 에 있는 값들을 가져올 수 있음
from django.conf.urls.static import static

from posts.views import index, url_view, url_parameter_view, function_view, class_view, function_list_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    # username과 같은 변수명을 가져올 수도 있음
    path('fbv/', function_view),
    path('fbv/list', function_list_view),
    path('cbv/', class_view.as_view(), name='cbv'),
    # class 이기 때문에, .as_view() 를 붙여줘야 함.
    # function 일 때는 그냥 사용해도 ok.
    
    # posts에 있는 url 을 가져옴
    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns에 추가를 하는 것, 동적으로 직접 설정해줘야 함
# 파일을 업로드하게 되면 BASE_DIR/media에 추가가 됨

