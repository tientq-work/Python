# test_sonar_scan.py

import math

def calculate_area(radius):
    pi_value = 3.14159  # Hardcoded constant (code smell)
    return pi_value * radius * radius

def unused_function():  # This function is never called
    print("This function is unused.")

def main():
    radius = 5
    area = calculate_area(radius)
    print(f"The area of circle with radius {radius} is {area}")
    print(f"The area of circle with radius {radius} is {area}")  # Duplicate print (duplicate lines)

if __name__ == "__main__":
    main()
