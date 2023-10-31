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

# Model

    ※ 모델링 : 저장하고자 하는 데이터를 모델로 정의하는 것
    ※ 모델 관계
        - 1:1 (일대일)

        - 1:N (일대다)
        ex) 게시글 - 댓글 관계 / 사용자 - 게시글 관계
            => 1:N 관계에서는 N이 되는 모델에 ForeignKey를 사용

        - N:N (다대다)

    ※ 





