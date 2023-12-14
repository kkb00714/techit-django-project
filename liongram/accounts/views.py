
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.forms import SignUpForm, UserCreateForm

from users.models import User

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)

    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST) # 데이터 유효성 검사
        
        if form.is_valid(): # 데이터 유효성 검사
            # 회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password2 = form.cleaned_data['password2']
            
            instance = form.save() # 회원가입을 처리하는 것이 비즈니스 로지기 처리
            return redirect('index')
            
        else:
            # 리다이렉트
            return redirect('accounts:signup')
        
def login_view(request):
    # GET, POST 분리
    if request.method == 'GET':
        
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()})
    
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            # 응답
            return redirect('index')
        
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return redirect(request, 'accounts/login.html', {'form': form})
        
        
        # 데이터 유효성 검사
        # username = request.POST.get('username')
        # if username == ''or username == None:
        #     pass
        
        # user = User.objects.get(username = username)
        # if user == None:
        #     pass
        # password = request.POST.get('password')
        
        # 순서 꼭 기억하기
        # 데이터 유효성 검사 => 비즈니스 로직 처리 => 응답
        
        
