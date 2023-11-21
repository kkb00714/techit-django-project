from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

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
    
