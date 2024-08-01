import threading

# 피보나치 수열 생성기
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 피보나치 수열을 출력하는 함수
def print_fibonacci_sequence(generator, n):
    for _ in range(n):
        print(threading.current_thread().name, ": ", next(generator))

# 생성된 피보나치 수열 생성기
fibonacci_gen = fibonacci_generator()

# 쓰레드 1
thread1 = threading.Thread(target=print_fibonacci_sequence, args=(fibonacci_gen, 10), name="Thread-1")

# 쓰레드 2
thread2 = threading.Thread(target=print_fibonacci_sequence, args=(fibonacci_gen, 10), name="Thread-2")

# 쓰레드 시작
thread1.start()
thread2.start()

# 쓰레드가 종료될 때까지 대기
thread1.join()
thread2.join()
