# ******************Task#1 date 04.03.2024******************
# value = 0
# while value < 5:
#     value += 1
#     Enter_word = str(input("awaiting word"))
#     new_word = Enter_word[::-1]
#     if Enter_word == new_word:
#         print("+")
#     else:
#         print("-")
# print("successful end")


# ******************Task#2 date 04.03.2024******************
# value = 0
# while value < 5:
#     value += 1
#     text = str(input("awaiting text"))
#     word = str(input("awaiting word"))
#
#     if word not in text:
#         print("NO")
#     else:
#         print("YES")
# print("successful end")

# ******************* Task#3 date 04.03.2024*****************
value = 0
while value < 3:
    value += 1
    email = str(input("Please enter valid email"))

    if "@" and "." not in email:

        print("NO,Please enter valid email form")
    else:
        print("validation successful!")


