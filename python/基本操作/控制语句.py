# Author: Jason Lu

# 猜数字
age_of_oldboy = 56
guess_age = int(input("guess age:"))

if guess_age == age_of_oldboy:
    print("Yes, you got it.")
elif guess_age > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger...")


print("===============for语句================")


count = 0
age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("guess age:"))

    if guess_age == age_of_oldboy:
        print("Yes, you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")

    count += 1
else:
    print("you have tried too many times...fuck off")


for i in range(10):
    print('i:', i)

for i in range(0, 10, 2):
    print('i: ', i)

for i in range(0, 100):
    if i < 50:
        print('i < 50')
    else:
        continue


print("===============while语句================")


count = 0
age_of_oldboy = 100
while count < 3:
    int_guess_age = int(input(">>guess age:"))

    if int_guess_age == age_of_oldboy:
        break
    elif int_guess_age < age_of_oldboy:
        print('think bigger')
    else:
        print('think smaller')

    count += 1
else:
    print('You have tried too many times...fuck off')














