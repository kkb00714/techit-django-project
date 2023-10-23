from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculator(request): 
    # request는 요청이라는 의미로, 첫번째 인자로 무조건 들어와야 함(약속)
    
    # return HttpResponse('계산기 기능 구현 시작입니다.') # 텍스트는 자유
    return render(request, 'calculator.html')
    