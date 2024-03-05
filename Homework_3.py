# ******************Task#1 date 04.03.2024******************
value = 0
while value < 5:
    value += 1
    Enter_word = str(input("awaiting word"))
    new_word = Enter_word[::-1]
    if Enter_word == new_word:
        print("+")
    else:
        print("-")
print("successful end")


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