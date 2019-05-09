Django 명령어 모음
------------------

#### 가상환경 실행

---

##### Windows

```
source venv/Scripts/activate
```

##### macOS

```
source venv/bin/activate
```

#### 프로젝트에 App 추가

---

```
python manage.py startapp 앱이름
```

#### 서버 켜기

---

```
python manage.py runserver
```

#### migrations 만들기

---

```
python manage.py makemigrations
```

#### DB migrate

---

```
python manage.py migrate
```

#### 관리자(admin) 계정 생성

---

```
python manage.py createsuperuser
```

#### Static 파일 collecting

---

```
python manage.py collectstatic
```

#### 가상환경 종료

---

```
deactivate
```
