# 파이썬 퀴즈 #2 (레벨 4)

## Quiz

행맨 게임(영어 단어 퀴즈) 프로그램을 만드시오

### [조건]

- 리스트에 3개 이상의 단어를 추가
    - 예) apple, banana, orange
- 위 리스트에서 랜덤으로 1개의 단어를 선택
- 단어의 길이에 맞게 밑줄 출력
    - 예) apple 의 경우 _ _ _ _ _
- 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct' 출력, 아니면 'Wrong' 출력
    - 예)<br>
        a 입력 시 : a _ _ _ _<br>
        p 입력 시 : a p p _ _<br>
        c 입력 시 : a p p _ _
- 정답을 맞히면 Success 출력 후 프로그램 종료 (단, 횟수 제한은 없음)

---

## 코드 리뷰

나의 코드와 유튜버의 코드를 비교 분석해서 개선해야 할 부분 찾기

- 나의 코드
    - 규칙 추가해서 작성
        - 기회 10번
        - 알파벳이 아닌 입력값 들어오면 재입력
        - 정답 맞춘 알파벳을 또 입력하면 재입력

```python
def is_over(chance):
    if chance <= 0:
        print('--- Game Over ---')
        return True
    return False

user_ch = input(f"남은 도전 횟수 {chance}. 알파벳 1개 입력: ")
if len(user_ch) != 1 or not user_ch.isalpha():
    print("다시 입력하세요. 알파벳 1개만 입력 가능합니다.")
    continue
if user_ch in user_answer:
    print("다시 입력하세요. 앞서 정답을 맞춘 알파벳입니다.")
    continue
```

### 1. 정답 문자열 길이만큼 언더바(_)로 표시하기

- 나의 코드
    - 정답이 apple 인 경우 _____ 으로 표시
        - 띄어쓰기 들어간 _ _ _ _ _ 으로 표시하려다 관둠
        - re 라이브러리를 사용해서 정규표현식을 이용한 정답 알파벳 모두 언더바로 대체한 사용자 문자열 생성

```python
def make_user_answer(answer):
    user_answer = re.sub('\w', '_', answer)
    return user_answer
```

- 유튜버 코드
    - 정답 문자열 for 문 작성
        - 정답 알파벳이 사용자가 입력한 알파벳에 포함된다면 그 알파벳 출력
        - 그렇지 않다면 언더바(_) 출력

```python
letters = ""  # 사용자로부터 지금까지 입력받은 모든 알파벳

for w in word:
    if w in letters:
        print(w, end=" ")
    else:
        print("_", end=" ")
```

### 2. 사용자로부터 입력받은 알파벳을 어떻게 할 것인가

- 나의 코드
    - 사용자로부터 입력받은 알파벳이 정답 문자열에 포함되면 해당 인덱스를 찾아서 사용자의 문자열에서 그 알파벳으로 변경
        - 문자열 슬라이싱 사용

```python
def check_ch(answer, user_answer, user_ch):
    if user_ch in answer:
        for i, ch in yield_index_ch(answer, user_ch):
            user_answer = user_answer[:i] + user_ch + user_answer[i+1:]
        print('--- Correct ---')
        print(user_answer)
    else:
        print('--- Wrong ---')
    return user_answer
```

- 유튜버 코드
    - 사용자로부터 입력받은 알파벳을 모두 저장

```python
letters = ""  # 사용자로부터 지금까지 입력받은 모든 알파벳

letter = input("Input letter > ")  # 사용자 입력 받기
if letter not in letters:
    letters += letter

if letter in word:
    print("Correct")
else:
    print("Wrong")
```

### 3. 행맨 게임 종료

- 나의 코드
    - 사용자의 문자열과 정답 문자열이 똑같으면 Success

```python
def is_answer(answer, user_answer):
    if user_answer == answer:
        print('--- Success ---')
        return True
    return False
```

- 유튜버 코드
    - 기본값 True 인 트리거 변수 하나 생성
        - 정답을 맞춘 경우 False 로 변경
    - 트리거 변수 값이 True 면 행맨 게임 종료

```python
while True:
    succed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succed = False
    print()

    if succed:
        print("Success")
        break

    letter = input("Input letter > ")  # 사용자 입력 받기
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")
```

### 결론

1. 사용자 문자열을 따로 만들어서 관리하지 말고 입력받은 알파벳을 모두 저장해서 정답 문자열의 알파벳이 포함되는지 알아보는 방식이 덜 복잡하고 코드를 줄일 수 있다.
2. 함수를 따로 만들지 말고 True 값인 트리거 변수를 하나 만들어서 성립하지 않을 경우에만 False 로 설정해서 작동하는 방식이 더 깔끔하고 코드를 줄일 수 있다.

---

유튜버 나도코딩의 파이썬 퀴즈

- [유튜브 해설 바로가기][youtube]

[youtube]: https://youtu.be/487mr-e_Z74