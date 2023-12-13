from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = UserCreationForm
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)

    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        pass