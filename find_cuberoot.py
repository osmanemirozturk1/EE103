
given_number = int(input("Enter an integer to find cube root: "))

is_negative = given_number < 0
num_abs = abs(given_number)

guess_number = 0

while guess_number ** 3 < num_abs:
    guess_number += 1

if guess_number ** 3 == num_abs:
    if is_negative:
        guess_number = -guess_number
    print(f"The cube root of {given_number} is {guess_number}.")
else:
    print(f"{given_number} is not a perfect cube.")