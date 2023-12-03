# techit-django-project 정리노트

※ python -m venv venv => venv 라는 파이썬 가상환경 생성

※ .\venv\Scripts\activate => 가상환경 접속

※ pip install django => 장고 설치

※ pip list => 설치된 pip 목록 확인
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

------

# HTTP 노트   
    ※ HTTP는 HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜

    ※ F12(개발자 도구)를 통해 각각의 요소들을 볼 줄 알아야 함

    ※ 장고 공식 페이지(Request and Response) - https://docs.djangoproject.com/ko/4.0/ref/request-response/
    
    ※ 

----------

# 데이터베이스와 ORM
    ※ 데이터베이스의 특징
        - 실시간 접근성 (사용자의 요구를 즉시 처리)
        - 지속적인 변화 (정확한 값을 유지하기 위해 삽입, 삭제, 수정작업 등을 이용해 데이터를 지속적으로 갱신)
        - 동시 공유 (동시에 여러 사람이 동일한 데이터에 접근하고 이용할 수 있음)
        - 내용에 대한 참조 (데이터 값에 따라 참조할 수 있어야 함)

    ※ DBMS (Database Management System ) :데이터베이스 관리 시스템)
        - DB 내의 데이터를 접근할 수 있도록 해주는 소프트웨어
        - 사용자 또는 다른 프로그램의 요구를 처리하고 응답하여 데이터를 사용할 수 있게 함
        - 일반적으로 DB라고도 부름
        - DBS(Database System) DB + DBMS 등의 전체 시스템

    ※ DBMS의 장단점
        - 장점
            => 데이터 중복 최소화
            => 데이터 독립성이 확보
            => 데이터를 동시 공유
            => 데이터 보안이 향상
            => 데이터 무결성을 유지
            => 장애 발생 시 회복이 가능

        - 단점
            => 비용이 많이 발생
            => 백업과 회복 방법이 복잡
            => 중앙 집중 관리로 인한 취약점이 존재

    ※ DBMS의 기능
        - 정의 : 요구하는 데이터 구조를 지원하기 위해 데이터베이스에 저장될 데이터의 형(Type) 과 구조에 대한 정의, 이용 방식, 제약 조건 등을 명시하는 기능

        - 조작 : 데이터 검색, 갱신, 삽입, 삭제 등을 체계적으로 처리하기 위해 사용자와 데이터베이스 사이의 인터페이스 수단을 제공하는 기능

        - 제어 : 데이터의 무결성이 유지되도록 제어해야 하는 기능

    ※ 대표적인 DBMS 
        - Oracle (대기업에서 주로 사용, 점유율 1위)

        - SQLite (응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스 시스템)

        - MySQL (세계에서 가장 많이 쓰이는 오픈소스 관계형 데이터베이스{RDBMS})

        - PostgreSQL (SQL 언어를 사용하는 오픈 소스 객체 관계형 데이터베이스 시스템)

    ※ 구조적 질의 언어 (Structured Query Language, SQL)
        - DDL : 데이터 정의 언어, 각 릴레이션을 정의하기 위해 사용 (테이블들을 생성하거나 수정하기 위함)
        - ☆ DML : 데이터 조작 언어, 데이터를 관리하기 위한 언어 (데이터베이스의 ROW에 삽입, 수정, 삭제, 업데이트 등의 기능)
        - DCL : 데이터 제어 언어, 데이터를 관리하고 접근하는 권한을 다루기 위한 언어 (사용자가 요구했을 때, 그 권한을 나누기 위한 기능)

----------

# ORM 

    ※ 객체지향과 관계형 데이터베이스가 같지 않기 때문에, ORM이라는 것이 필요함

    => Object Relational Mapping, 객체-관계 매핑으로, 파이썬의 객체(Object)와 데이터베이스의 데이터를 연결해주는 역할을 해줌

    ※ORM의 장점
        - 생산성 향상, 비즈니스 로직 집중
        - 재사용 및 유지보수 용이
        - DBMS 종속되지 않음
    
    ※ ORM의 단점
        - 프로젝트가 복잡한 경우 난이도 상승
        - Raw Query 보다 성능이 낮음
    
----------
    
# MTV 디자인 패턴 - 1 (Models)

    ※ View (컨트롤러 역할) - Template (데이터 출력 역할) - Model (데이터 관리)

    ※ Model 의 역할
        => 데이터를 관리하는 역할
        => 데이터베이스에 저장할 테이블 정의
        => 모델에 작성된 코드를 기준으로 데이터베이스 생성(ORM, Object Relational Mapping)

    ※ 주요 모델 필드
        => CharField : 작거나 큰 문자열을 위한 문자열 필드 (str())
        => TextField : 긴 텍스트 필드 (str())
        => BooleanField : 참/거짓 필드 (bool())
        => DataTimeField : datatime.datetime 인스턴스로 표시되는 날짜 및 시간 필드 (datatime())
        => IntegerField : 정수 필드 (int())
        => FloatField : 부동 소수점 숫자 필드 (float())

    ※ 필드 주요 속성 => 노션, PPT 참조

-----------

# Model

    ※ 모델링 : 저장하고자 하는 데이터를 모델로 정의하는 것
    ※ 모델 관계
        - 1:1 (일대일)

        - 1:N (일대다)
        ex) 게시글 - 댓글 관계 / 사용자 - 게시글 관계
            => 1:N 관계에서는 N이 되는 모델에 ForeignKey를 사용

        - N:N (다대다)

----------

# QuerySet API
    
    ※ Query : DB에 정보를 요청하는 것
    ※ QuerySet : DB에서 전달받은 객체의 목록
    ※ QuerySet API : DB에 요청하기 위한 인터페이스

    ※Queryset API 주요 함수
        - 새 QuerySet을 반환하는 메서드
            => filter() : 특정 사용자의 게시글 검색(데이터 조회)에 사용
            => exclude() : 특정 사용자의 게시글(데이터)을 제외하고 조회하는데 사용
            => order_by() : 특정 필터를 기준으로 오름차, 내림차 순으로 정렬
            => select_related() : 
            => prefetch_related() : 
            => raw() : 직접 SQL문을 작성해서 Query를 전송할 때 사용

        - QuerySet을 반환하지 않는 메서드
            => get() : 하나의 데이터만 뽑을 때 사용
            => create() : 데이터를 추가할 때 사용
            => count() : 특정 데이터가 몇 개가 있는지, 그 숫자를 반환
            => first() : 데이터의 가장 첫번째 데이터
            => last() : 데이터의 가장 마지막 데이터
            
        => 공식 문서 참조

    ※ Django shell
        - 파이썬 인터프리터 형식으로 장고 사용
        - Model을 import하여 사용 가능
        - python manage.py shell 명령으로 사용 가능

    ※ Database Tool
        - 데이터베이스의 관리를 위한 도구
        - 툴을 활용하여 테이블이나 데이터를 조작
        - GUI (Graphical User Interface) 제공
    
----------

# Views를 만드는 2가지 방법

    ※ View : 웹 요청을 수신하고 응답하는 파이썬 함수 또는 클래스, (컨트롤러 역할)

    ※ FBV (Function Based Views) => 함수 기반 뷰, 일회성 및 특수 목적이 있는 View에 적합
        <장점>
        - 구현이 간편
        - 읽기 쉬우며 직관적인 코드
        - 데코레이터의 간단한 사용법

        <단점>
        - 코드 확장 및 재사용이 어려움
        - 조건부 분기를 통한 HTTP 메서드 처리
    
    ※ CBV (Class Based Views) => 클래스 기반 뷰, 일반적인 CRUD 등의 View에 적합함
        <장점>
        - 코드 확장과 재사용에 용이
        - 다중 상속, Mixin 가능
        - 내장 Class Based View 사용 (ListView, CreateView, DetailView 등)

        <단점>
        - 읽기 어려우며 복잡도가 높음
        - 데코레이터 사용 시 함수를 재정의 해야 함

-------------

# Django Template Engine

    ※ Template은 서버에서 실행 ☆

    ※ Template 태그
        - block : 자식 템플릿으로 재정의할 수 있는 블록
            ex) {% block name %} {% endblock %}
        - extends : 부모 템플릿을 확장, 상속
            ex) {% extends 'template_name' %}
        - include : 템플릿을 로드하고 현재 Context로 렌더링, 템플릿 포함
            ex) {% include template_name %}
        - for : Context 변수의 배열의 항목을 반복 사용 (for, empty)
            ex) {% for variable in variable_list %} ... {% endfor %}
        - if : 조건이 true 이면 출력하고 false 인 경우 미출력 (if, else, elif)
            ex) {% if bool %} {% endif %}
        - url : 보기 및 선택적 매개 변수와 일치하는 절대 경로 참조 (도메인 이름이 없는 URL)를 반환
            ex) {% url 'url_name' %}

    ※ Template 상속
        - 부모 HTML을 자식 HTML들이 가져다 쓰는 것. (자식에서 작성한 HTML들이 부모 HTML에 들어가는 형태 ??)
        
    ※ Template 필드
        - date : 주어진 형식에 따라 날짜 형식을 지정 
            ex) {{ value|date:"D d M Y" }}
        - default : 값이 로 평가 False가 되면 지정된 기본값을 사용하고, 그렇지 않으면 값을 사용
            ex) {{ value|default:"nothing" }}
        - center : 주어진 너비의 필드에서 값을 가운데에 맞춤 
            ex) {{ value|center:"15" }}
        - truncatechars : 정된 문자 수보다 긴 경우 문자열을 자름. 잘린 문자열은 번역 가능한 줄임표 문자("...")로 끝남
            ex) {{ value|truncatechars:7 }}
        - intcomma : 정수 또는 부동 소수점(또는 둘 중 하나의 문자열 표현)을 세 자리마다 쉼표가 포함된 문자열로 변환
            ex) {% load humanize %} {{ value|intcomma }}


------------

# CRUD 란?

    ※ CRUD : 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말

    ※ 대부분의 웹 서비스의 기반이 되는 개념

    ※ Create의 흐름
        폼(html) 요청 => 폼(html) 응답 => 데이터 생성 요청 => (데이터베이스) 데이터 응답
    
    ※ Create 참고
        - 사용자에게 입력 받는 데이터, 시스템에서 생성하는 데이터 
        => 두 데이터의 차이점들을 명심할 것

        - 인증 / 권한 => 로그인이 필요하거나, 관리자만 생성할 수 있는 등의 경우를 확인할 때
            ex) 글쓰기, 공지사항 작성 등

        - 데이터 유효성 검사 => 클라이언트가 입력한 데이터가 유효한지 검증
            ex) 나이, 전화번호, 파일 등
        
        - 



