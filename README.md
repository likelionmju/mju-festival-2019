2019 명지대학교 인문캠퍼스 대동제 소개 서비스
---------------------------------------------

![Version](https://img.shields.io/badge/Version-1.0.0-green.svg) ![Django](https://img.shields.io/badge/Python-Django-darkgreen.svg) ![Likelion](https://img.shields.io/badge/Likelion-MJU(Seoul)-informational.svg)

### 1. INFO

---

#### 개발 목표

-	명지대학교(서울) 멋쟁이사자처럼 7기가 직접 개발하는 서비스를 만든다.

-	축제를 이용하는 모든 사람들에게 편의성을 증진시켜 줄 서비스를 개발한다.

-	간단한 GitHub 활용을 통해 협업을 경험한다.

#### 개발 범위

-	2019년 5월 14일 부터 16일까지 진행되는 명지대학교 인문캠퍼스 대동제 정보 안내 사이트

#### 개발 포지션

-	Project manager: 반정훈, 한종우

-	Front-end: 김혜현, 박건희, 서유림, 최은지, 함범준

-	Back-end: 변현홍, 조형서, 황낙주

-	Designer: 한연희

-	Director: 김만수, 전기석

### 2. 개발 환경 구성

---

먼저, 터미널을 통하여 레파지토리를 다운로드할 폴더로 이동합니다. 그 다음 아래의 명령어를 통하여 레파지토리를 clone 해줍니다.

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

Django 다운로드 후, migrate와 runserver를 한 번씩 실행합니다.

```
python manage.py migrate
python manage.py runserver
```

### 3. Django에서 자주 사용되는 명령어

---

[Django에서 자주 사용되는 명령어](markdown/django.md)

### 4. Github 명령어

---

[Github 명령어](markdown/github.md)
