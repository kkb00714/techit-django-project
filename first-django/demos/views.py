from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculator(request): 
    # request는 요청이라는 의미로, 첫번째 인자로 무조건 들어와야 함(약속)
    
    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')
    
    # 2. 계산
    if operators == '+': # 연산자가 +일 때
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    # 3. 응답    
    # return HttpResponse('계산기 기능 구현 시작입니다.') # 텍스트는 자유
    return render(request, 'calculator.html', {'result' : result})

    