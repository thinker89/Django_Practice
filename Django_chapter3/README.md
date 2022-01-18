# 교재: Django 한그릇 뚝딱 

## project 2. RestaurantShare 만들기

### ForeignKey
- 다른 테이블을 연결해주는 참조키

### on_delete 종류
- CASCADE : 데이터가 삭제되면 참조하는 모든 요소도 삭제
- PROTECT : 참조하는 요소가 딸려있는 데이터는 삭제 불가
- SET_NULL : 참조하는 데이터가 삭제되면 참조값은 NULL로 세팅
- SET_DEFAULT : 참조하는 데이터가 삭제되면 참조값은 디폴트값으로 세팅
- SET() : 참조하는 데이터가 삭제되면 설정된 함수를 실행
- DO_NOTHING : 아무 조치도 하지 않음