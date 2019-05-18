2019 명지대학교 인문캠퍼스 대동제 소개 서비스
---------------------------------------------

![Version](https://img.shields.io/badge/Version-1.0.0-green.svg) ![Django](https://img.shields.io/badge/Python-Django-darkgreen.svg) ![Likelion](https://img.shields.io/badge/Likelion-MJU(Seoul)-informational.svg)

### 0. 서비스 점검 안내

---

2019 명지대학교 인문캠퍼스 대동제 소개 서비스가 잠시 점검의 시간을 가지게 되었습니다.

#### 서비스 점검 개요

-	점검 일시 : 5월 17일 오전 12시 ~ 6월 1일 오전 12시

-	서비스 오픈 예정 시간 : 6월 1일 오전 12시

### 1. INFO

---

#### 개발 목표

-	명지대학교(서울) 멋쟁이사자처럼 7기가 직접 개발하는 서비스를 만든다.

-	분산되어 있는 축제 관련 정보를 종합, 정리해 제공하여 명지대학교 재학생 및 외부인의 편의성을 증진시켜 줄 서비스를 개발한다.

-	간단한 GitHub 활용을 통해 협업을 경험한다.

#### 개발 범위

-	명지대학교 인문캠퍼스에서 5월 14일 (화) ~ 5월 16일 (목)까지 진행되는 축제 정보 안내 서비스

-	축제 연예인 라인업 정보를 일별로 제공한다.

-	축제 기간 동안 운영되는 부스에 관한 종합적인 정보를 제공한다.

-	회원가입을 요구하지 않는 익명 자유게시판을 제공한다.

-	분실물 게시판을 ‘찾아요’, ‘찾았어요’ 메뉴로 구분하여 제공한다.

-	축제 기간 동안 심야에 운영하는 학교 인근 음식점에 대한 정보를 제공한다.

-	학교 정문에서 이용할 수 있는 버스 노선과 막차 시간에 대한 정보를 제공한다.

#### 개발 포지션

-	Project manager: 반정훈, 한종우

-	Server manager: 한종우

-	Front-end: 김혜현, 박건희, 서유림, 최은지, 함범준

-	Back-end: 변현홍, 조형서, 황낙주

-	Designer: 한연희

-	Director: 김만수, 전기석

### 2. 개발 환경 구성

---

먼저, 터미널을 통하여 레파지토리를 다운로드할 폴더로 이동합니다. 그 다음 아래의 명령어를 통하여 레파지토리를 clone 해 줍니다.

```
git clone https://github.com/likelionmyongji/mju_festival.git
```

clone한 폴더는 gitignore를 통하여 가상환경 없이 업로드 되었기 때문에 가상환경을 새로 생성해주어야 합니다. 생성 후 가상환경을 실행해 줍니다.

##### Windows

```
python -m venv venv
source venv/Scripts/activate
```

##### macOS

```
python3 -m venv venv
source venv/bin/activate
```

이후, pip 패키지를 통하여 Django를 가상환경 내에 다운로드해 줍니다.(이 작업은 처음 가상환경 생성 시, 한 번만 해 주시면 됩니다.)

```
pip install django
```

그다음, 프로젝트에서 필요한 pip 패키지들을 다운로드해 줍니다.

```
pip install Pillow
pip install gunicorn dj-database-url psycopg2-binary whitenoise
```

### 3. Django에서 자주 사용되는 명령어

---

Django 관련 명령어는 [여기](markdown/django.md)를 참고해 주세요.

### 4. Github 명령어

---

Github 명령어는 [여기](markdown/github.md)를 참고해 주세요.
