from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Post
from .serializers import PostModelSerializer

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

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
