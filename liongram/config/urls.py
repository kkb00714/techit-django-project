from django.contrib import admin
from django.urls import path

from posts.views import url_view, url_parameter_view, function_view, class_view, function_list_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    # username과 같은 변수명을 가져올 수도 있음
    path('fbv/', function_view),
    path('fbv/list', function_list_view),
    path('cbv/', class_view.as_view()),
    # class 이기 때문에, .as_view() 를 붙여줘야 함.
    # function 일 때는 그냥 사용해도 ok.
    
]
