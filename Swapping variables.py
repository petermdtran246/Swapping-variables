# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    swap_numbers = swap_values(num1, num2, num3, num4)
    print(*swap_numbers)


