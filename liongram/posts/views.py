from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView

from .models import Post

def index(request):
    return render(request, 'index.html')


def post_list_view(request):
    return render(request, 'posts/post_list.html')
    # settings.py 의 TEMPLATES 란에 templates 라는 경로를 입력했기 때문에(?)
    # posts(앱명) 을 써준 이후에 templates 다음의 경로들을 써주어야 함.

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')


def url_view(request): # request는 무조건 있어야 함
    data = {'code':'001', 'ln':'good'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)
    
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    # 터미널 창에 요청을 받아와서 출력
    # ?key=value 형식으로 사용해서 확인 가능

    return HttpResponse(username)

def function_view(request):

    print(f'request.method: {request.method}')
    if request.method == 'GET':
            print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
            print(f'request.POST: {request.POST}')
    return render(request, 'view.html')
    
# 클래스 기반 뷰 

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
    
def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list':object_list})
