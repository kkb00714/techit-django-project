from django.shortcuts import render

from rest_framework import status

from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics

from .models import Post, Comment
from .serializers import (PostListModelSerializer, 
                        PostCreateModelSerializer, 
                        CommentHyperlinkedModelSerializer,
                        PostRetrieveModelSerializer,
                        CommentListModelSerializer,
                        )

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# 게시글 목록 + 생성
# ListAPIView, CreateAPIView => pk 값이 안 들어감
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
    
    # Overriding 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(writer = request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# 게시글 상세, 수정, 삭제
# RetrieveAPIView, UpdateAPIView, DestroyAPIView => pk 값이 들어감
class PostRetrieveUpdateView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


# 
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
    
    def get_permissions(self):
        permission_classes = list()
        action = self.action

        if action == 'list':
            permission_classes = [AllowAny]
        elif action in ['create', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    
    
    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk=None):
        post = self.get_object()
        comment_all = post.comment_set.all()
        serializer = CommentListModelSerializer(comment_all, many=True)
        return Response(serializer.data)
    
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
