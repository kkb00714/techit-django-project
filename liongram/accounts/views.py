from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm

from accounts.forms import SignUpForm #, UserCreateForm

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)

    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        
        if SignUpForm.is_valid():
            # 회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password2 = form.cleaned_data['password2']
            
            instance = form.save()
            return redirect('index')
            
        else:
            # 리다이렉트
            return redirect('accounts:signup')