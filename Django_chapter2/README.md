# 교재: Django 한그릇 뚝딱 

## project 1. ToDoList 만들기

### Application 구조
- 하나의 프로젝트를 개별적 기능으로 나눈다

### MVC 패턴과 Django
- Model : models.py
- View : templates 폴더 내 html
- Control : views.py

### MVC, MTV 패턴
- MVC의 뷰 == MTV의 템플릿
- MVC의 컨트롤러 == MTV의 뷰

### GET, POST 전송 방식
- GET: url 뒤에 ?를 이용해 파라미터 전송. 값이 노출됨.
- POST: body에 값을 숨겨서 보냄. 속도는 상대적으로 느림.

### 