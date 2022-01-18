# 깃허브 특강

## MarkDown 문법

```
# 제목 1
## 제목 2
###### 제목 6

- 순서 없는 목록

1. 순서 있는 목록

*이텔릭*
**볼드**
`하이라이트`

```python
코드 블록
\```
```

## git 명령
```
git init
touch README.md
git add README.md
git config --global user.name 'my_name'
git config --global user.email 'my_mail'
```

```
git add README.md
git commit -m 'first commit'
git status
git log
```

## 최초 저장소 생성 및 commit, push하기
```zsh
mkdir new_project
cd new_project
touch README.md .gitignore
#`gitignore.io`에 접속하여 gitignore 복붙
git init
git add .
git commit -m 'first commit'
#`github` 저장소 만들기
git remote add origin https://github.com/WonguLee/git_lesson2.git
git push origin master
git log --oneline
```

## 리모트 저장소 로컬에 clone
```zsh
git clone https://github.com/WonguLee/git_lesson2.git
```

## 리모트에서 pull 받기
```zsh
 git pull
```

## 수동 merge
```zsh
# 수동으로 머지 작업 실시 후
git add .
git commit -m '머지 완료'
git push origin master
```

## branch
```zsh
git branch b1
git switch b1
# 브랜치 작업 후
git add .
git commit -m '브랜치 작업'
git switch master
git pull
git merge b1
git push origin master
```

## branch 제거
```zsh
git branch -d b1
```

## fork와 pull request(PR)
1. 깃허브에서 상대방 repo를 복사해온다.(fork)
2. 복사된 내 repo에서 작업을 마치고 PR을 요청한다. (충돌 발생시 깃허브에서 머지 후 PR 요청한다.)
3. PR 요청을 받은 원본repo 관리자가 확인 후 머지한다.
- `푸쉬 권한이 없는 경우 이렇게 작업한다.`