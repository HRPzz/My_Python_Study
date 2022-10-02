# for 문과 if 문 활용
for i in range(1, 21):
    if i % 2 == 1:  # i 를 2 로 나눈 나머지
        print("A" + str(i), end=" ")

print()

# slicing 활용
for i in range(1, 21)[::2]:  # 2 칸씩 건너 뛰어서
    print("A" + str(i), end=" ")