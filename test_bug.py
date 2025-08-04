def divide(a, b):
    return a / b  # <-- Sonar sẽ báo lỗi potential division by zero ở đây

def unused_func():
    pass  # <-- Code Smell: function never used

divide(5, 0)  # <-- Dòng này Sonar chắc chắn detect lỗi run-time division by zero
