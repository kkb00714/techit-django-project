# techit-django-project

※ python -m venv venv => venv 라는 파이썬 가상환경 생성

※ .\venv\Scripts\activate => 가상환경 접속

※ pip install django => 장고 설치

------

# 장고 프로젝트 생성하기

※ django-admin startproject config . => 원래는 파일명을 입력
    // config . => 장고 프로젝트를 만들 때, 유지보수를 용이하게 하기 위해서 만들어줌
    ※ config 파일 내에는 설정들이 들어가있음. (임의로 바꾸면 오류가 날 수 있으니 주의!)

※ django의 루트 파일(first-django와 같은)에 manage.py 파일이 있는지 꼭 확인 후 python manage.py runserver => 장고 실행

※ asgi.py & wsgi.py 는 배포에 관련된 파일 => 나중에 다시 설명

※ settings.py => 장고가 실행되는 데 있어서 필요한 설정값(변수)들이 있음. 

※ urls.py => 이 파일 안에 path 에 설정된 것이 바로 주소임.

※ django-admin startapp demos(demos는 파일명) => 장고의 앱을 만듦(폴더가 생김)
    => 앱을 만들 땐 무조건 앱을 추가해줘야 함!!
    => config/settings.py 에서 INSTALLED APPS 에 무조건 추가해줘야 함. 
    => 자동으로 생기는 대부분의 파일들의 이름을 건들지 말자.

    ※ admin.py => 장고가 제공하는 기능으로, 관리자 인터페이스를 제공함

    ※ apps.py => 이 앱의 이름이나 설정값을 넣는 곳

    ※ models.py => 데이터베이스에 저장해야하는 데이터들을 작성하는 곳

    ※ tests.py => 테스트 코드를 짤 수 있는 곳

    ※ views.py => controller 역할을 해주는 비즈니스를 처리해주는 곳