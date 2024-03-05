# ******************Task#1 date 04.03.2024******************
value = 0
# Use a for loop with a range instead of while loop for clearer iteration
for _ in range(5):
    # Use descriptive variable names adhering to snake_case convention
    enter_word = input("Enter a word: ")  # No need to convert input to string using str()
     # Reverse the entered word using slicing
    reversed_word = enter_word[::-1]
    # Check if the word is a palindrome
    if enter_word == reversed_word:
        print("+")
    else:
        print("-")
# Move the print statement outside the loop for better readability
print("Successful end")


# ******************Task#2 date 04.03.2024******************
value = 0
while value < 5:
    value += 1
    text = str(input("awaiting text"))
    word = str(input("awaiting word"))

    if word not in text:
        print("NO")
    else:
        print("YES")
print("successful end")

# ******************* Task#3 date 04.03.2024*****************
value = 0
while value < 3:
    value += 1
    email = str(input("Please enter valid email"))

    if "@" and "." not in email:

        print("NO,Please enter valid email form")
    else:
        print("validation successful!")

# ******************* Task#4 date 05.03.2024*****************
value = 0
while value < 5:
    value += 1
    text = str(input("Please enter text"))

    a = text.split(' ')
    b = a[-2:]
    c = a[-3:]
    if b > a:
        print("Successful! last 3 words from list")
        print(c)
    else:
        print("Error!. Text shoud to contain more than 3 words !")
        print(text.split(' '))
        print("Your text have less than 3 elements")
        print(text.count(' '))


# count()	Повертає кількість вказаних елементів у списку.
