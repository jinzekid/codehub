# Author: Jason Lu
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


for i in range(0,10,2):
    print("loop ", i)


for i in range(0, 10):
    if i < 5:
        print("loop ", i)
    else:
        continue

print("hehehe...")
