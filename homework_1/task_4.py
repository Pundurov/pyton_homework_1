user_number = int(input("Enter a positive integer: "))
max_number = 0

while user_number >= 1:
    next_number = user_number % 10
    if max_number < next_number:
        max_number = next_number
    user_number = user_number // 10

print(f"Самая большая цифра в числе: {max_number}")
