def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Please do not divide by zero!")