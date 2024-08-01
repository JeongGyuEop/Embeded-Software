# 생성기 함수 정의
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 생성기를 사용하여 피보나치 수열을 출력
fib_gen = fibonacci()
for i in range(10):  # 처음 10개의 피보나치 수열 출력
    print(next(fib_gen))
