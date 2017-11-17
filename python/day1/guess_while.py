# Author: Jason Lu

'''
count = 0
while True:
    print("count:", count)
    count = count + 1
'''

count = 0
age_of_oldboy = 56

while count < 3:

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



