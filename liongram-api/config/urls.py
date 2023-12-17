from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from posts.views import PostModelViewSet, calculator, CalculatorAPIView # CommentModelViewSet

# router의 핵심 => view를 기준으로 urlpattern 등을 작성해줌
router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)
# router.register('comments', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
    # path('calculator/', calculator, name='calculator-fbv'),
    path('calculator/', CalculatorAPIView.as_view(), name='calculator-cbv'),
]
