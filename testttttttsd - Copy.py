import os
import sys

def add_numbers(a, b):
    # lỗi: biến không dùng
    unused_var = 10

    # lỗi: hardcoded credentials
    password = "123456"

    # lỗi: kiểm tra điều kiện vô nghĩa
    if a == a:
        print("a equals a")

    # lỗi: nested if quá sâu
    if a > 0:
        if b > 0:
            if a > b:
                print("Deep nested")

    return a + b

def main():
    # lỗi: không xử lý exception
    result = add_numbers("10", 5)  # lỗi: cộng chuỗi + int
    print("Result is: " + result)

    # lỗi: không sử dụng biến đã khai báo
    temp = 999

main()
