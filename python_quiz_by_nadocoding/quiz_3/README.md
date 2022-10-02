# 파이썬 퀴즈 #3 (레벨 1)

## Quiz

"사회적 거리두기"에 따른 영화관 좌석 예매 시스템을 만드시오

### [조건]

- 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성
    - 예)<br>
        A1 A2 A3 A4 ... A20<br>
        B1 B2 B3 B4 ... B20<br>
        C1 C2 C3 C4 ... C20
- 이 때 A열에 대해서 홀수로 끝나는 좌석에 대해서만 출력 (각 좌석은 ""로 구분)
    - 예) A1 A3 A5 A7 ... A19

---

## 코드 리뷰

나의 코드와 유튜버의 코드를 비교 분석해서 개선해야 할 부분 찾기

### 홀수만 출력하기

- 나의 코드
    - range 활용

```python
# range 활용
for i in range(1,21,2):
    print(f'A{i}', end=" ")
```

- 유튜버 코드
    - for 문 + if 문
    - slicing 활용

```python
# for 문과 if 문 활용
for i in range(1, 21):
    if i % 2 == 1:  # i 를 2 로 나눈 나머지
        print("A" + str(i), end=" ")

print()

# slicing 활용
for i in range(1, 21)[::2]:  # 2 칸씩 건너 뛰어서
    print("A" + str(i), end=" ")
```

### 결론

#### 1. 일반적인 홀수인 경우만 출력하는 방법
- for 문 + if 문

#### 2. 그 외 방법
- range 활용
- slicing 활용

---

유튜버 나도코딩의 파이썬 퀴즈

- [유튜브 해설 바로가기][youtube]

[youtube]: https://youtu.be/QEYIVLyGIRI