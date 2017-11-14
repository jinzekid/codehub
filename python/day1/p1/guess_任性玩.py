# Author: Jason Lu

count = 0
age_of_oldboy = 56

while True:

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


    if count == 3:
        continue_confirm = input("do you want to keep guessing..?")
    else:
        print("Game over! Byebye...")
        break

    if continue_confirm == 'y':
        count = 0;
    else:
        print("Game over! Byebye...")
        break