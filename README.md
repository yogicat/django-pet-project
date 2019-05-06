
# Django Pet Project

WIP 🚧 : HAPPY PETS :)

https://myhappypetsapp.herokuapp.com/



## Vritual Environment

- python 3.6
- virtualenv 16.4.3

## Requirements

- Django==2.0
- django-extensions==2.1.6
- codecov==2.0.15
- pytest==4.4.0
- requests==2.21.0
- psycopg2==2.8.2


## Database

- PostgreSQL

## Deployment

- Heroku
- S3: Media folder

---

## 가상환경 세팅

virtualenv를 이용해 가상환경을 세팅한다.

virtualenv 설치하기

`pip3 install virtualenv[==x.x.x]`

글로벌로 virtualenv를 설치한다. ==x.x.x 특정 버전을 설치할땐 버전을 입력해준다.

virtualenv로 환경세팅하기

`$ virtualenv -p python3.6 venv`

작업할 디렉토리에서 venv라는 디렉토리에 파이썬 가상환경을 세팅한다.

`$ source venv/bin/activate`- 가상환경을 활성화 한다.

`$ pip install <package name>` - 필요한 패키지를 설치한다.

`$ deactivate` - 가상환경 비활성화

setting에 패키지적용하기

```py
settings.py

INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

### Requirements 설명

- Django: 파이썬으로 만들어진 웹 프레임워크
- Django-extensions: 장고를 사용할때 유용한 기능들을 제공한다.
- codecov: 테스트 코드 커버리지를 측정해주는 라이브러리.(nodejs에서는 jest, istanbul와 유사함) 링크
- pytest: 테스트 코드 작성 라이브러리 (nodejs에서 jest, mocha와 유사함)
- requests: 간편하게 HTTP요청(GET, POST, PUT, DELETE, ..)을 보낼 수 있게 하는 패키지. urllib3를 가지고 만들어짐.
- virtualenv: 다양한 버전의 프로젝트 개발을 위한 가상환경 세팅 도구.


---

### DATABASE MODEL

**USER**

- 이메일 - pk
- 이름 - 필수
- 전화번호 - 필수, unique
- 우편번호
- 주소정보
- 상세주소정보
- 권한 - 일반유저, 직원, 슈퍼유저 (admin으로 자동 관리)


**PET**

- 반려동물의 소유자 정보 - 이메일, fk
- 반려동물을 구분하기 위한 키값 - pk
- 종류 - 강아지, 고양이, 기타
- 이름 - 필수
- 사진
- 생일
- 반려동물 등록번호
- 질병 정보 - json
- 알러지 정보 - json
- 선호 성분 - json
- 대표 반려동물 여부 - bool


