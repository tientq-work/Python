import os  # Unused import — Sonar sẽ cảnh báo

def connect_to_db():
    username = "admin"  # Hardcoded credentials — Sonar sẽ cảnh báo security
    password = "123456"
    print("Connecting to database with user", username)

def multiply(a, b):
    result = a * b
    return result
    print("This will never be executed")  # Unreachable code — Sonar báo

def multiply_duplicate(a, b):
    result = a * b
    return result  # Duplicate code với hàm multiply — Sonar báo

def divide(a, b, log_result=False):
    try:
        result = a / b
    except ZeroDivisionError:
        pass  # Swallow exception — Sonar cảnh báo
    if log_result:
        print("Result is:", result)
    return result

def unused_parameter(a, b, c):
    return a + b  # c không dùng — Sonar báo

if __name__ == "__main__":
    connect_to_db()
    print(multiply(2, 3))
    print(divide(5, 0))
    print(unused_parameter(1, 2, 3))
