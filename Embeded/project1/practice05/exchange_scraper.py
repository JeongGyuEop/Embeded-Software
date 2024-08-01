from tkinter import messagebox

import requests
import tkinter as tk

def get_exchange_rate():
    # 공공 API나 웹 스크래핑을 통해 환율 정보를 가져오는 코드를 작성합니다.
    # 이 예시에서는 공공 API를 사용하는 것으로 가정하겠습니다.
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"]["KRW"]  # 한국 원화 환율 정보 가져오기
    return exchange_rate

def show_exchange_rate():
    exchange_rate = get_exchange_rate()
    messagebox.showinfo("환율 정보", f"1 USD = {exchange_rate} KRW")

# Tkinter GUI 생성
root = tk.Tk()
root.title("환율 정보")

# 라벨 생성
label = tk.Label(root, text="환율 정보를 확인하려면 아래의 버튼을 클릭하세요.")
label.pack(pady=10)

# 버튼 생성
button = tk.Button(root, text="환율 정보 확인", command=show_exchange_rate)
button.pack(pady=5)

# 윈도우 실행
root.mainloop()
