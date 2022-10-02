# 개발자도 틀리는 깜짝 퀴즈 | 해설편 | 파이썬

## Quiz 1

다음 코드를 실행하면 출력값이 어떻게 될까요?

### [코드]

```python
def three():
    print("three", end=" ")
    return 3

def five():
    print("five", end=" ")
    return 5

def seven():
    print("seven", end=" ")
    return 7


# main code
three() > five() > seven()
```

### [출력 결과]

1. three five seven
2. three five
3. three
4. 정답 없음

### [정답]

2. three five

### [해설]

```python
# (3 > 5) and (5 > 7)
# => (3>5) 값이 False 라서 (5>7) 부분은 실행하지 않음
# => three five 출력
three() > five() > seven()
```

---

## Quiz 2

다음 코드를 실행하면 출력값이 어떻게 될까요?

### [코드]

```python
def 서류심사(): print("1. 서류심사"); return True
def 서류심사(): print("2. 인적성검사"); return True
def 서류심사(): print("3. 코딩테스트"); return True
def 서류심사(): print("4. 면접1차"); return False
def 서류심사(): print("5. 면접2차"); return True
def 서류심사(): print("6. 신체검사"); return True

if 서류심사() and 인적성검사() and 코딩테스트() and 면접1차() and 면접2차() and 신체검사():
    print("최종 합격입니다")
else:
    print("아쉽게도 탈락입니다")

```

### [정답]

1. 서류심사
2. 인적성검사
3. 코딩테스트
4. 면접1차

아쉽게도 탈락입니다

---

유튜버 나도코딩의 파이썬 퀴즈

- [유튜브 해설 바로가기][youtube]

[youtube]: ?