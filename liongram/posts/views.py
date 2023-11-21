from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def url_view(request): # request는 무조건 있어야 함
    data = {'code':'001', 'ln':'good'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)
    
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(username)
    print(request.GET)
    # 터미널 창에 요청을 받아와서 출력
    # ?key=value 형식으로 사용해서 확인 가능

    return HttpResponse(username)