from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from posts.views import (PostListCreateView, 
                        PostRetrieveUpdateView,
                        calculator, 
                        CalculatorAPIView, 
                        PostModelViewSet,
                        )
from accounts.views import login_view


# router의 핵심 => view를 기준으로 urlpattern 등을 작성해줌
router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('login/', login_view),
    
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),
    
    # path('calculator/', calculator, name='calculator-fbv'),
    path('calculator/', CalculatorAPIView.as_view(), name='calculator-cbv'),
]
