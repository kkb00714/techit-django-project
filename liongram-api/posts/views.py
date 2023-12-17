from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework import generics

from .models import Post, Comment
from .serializers import (PostListModelSerializer, 
                        PostCreateModelSerializer, 
                        CommentHyperlinkedModelSerializer,
                        PostRetrieveModelSerializer)

# 게시글 목록 + 생성
class PostListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
    
    
# 게시글 상세
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer

# 게시글 작성

# 게시글 수정 1

# 게시글 수정 2

# 게시글 삭제 



class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
    
# class CommentModelViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentHyperlinkedModelSerializer

@api_view()
def calculator(request):
    # 1. 데이터 확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')
    
    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    data = {
        'type' : 'FBV', # 함수 기반이기 때문에
        'result': result,
    }

    # 3. 응답
    return Response(data)

class CalculatorAPIView(APIView):
    # Get방식
    def get(self, request):
        
        # 1. 데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')
        
        # 2. 계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators == '-':
            result = int(num1) - int(num2)
        elif operators == '*':
            result = int(num1) * int(num2)
        elif operators == '/':
            result = int(num1) / int(num2)
        else:
            result = 0

        data = {
            'type' : 'CBV', # 클래스 기반이기 때문에
            'result': result,
        }

        # 3. 응답
        return Response(data)
    
    # Post 방식
    def post(self, request):
        data = {
            'type' : 'CBV',
            'method': 'POST',
            'result' : 0,
            
        }

        # 3. 응답
        return Response(data)
