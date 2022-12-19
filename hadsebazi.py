#this code will show how many times did you try
import random
pc_number = random.randint(0, 10)
count = 1
while True:
    user_numbr = int(input("entr numbr: "))

    if pc_number == user_numbr:
        print("barande shodi" )
        print(count)
        break
    if pc_number > user_numbr:
        print("bro balatar")
        count = count + 1

    elif pc_number < user_numbr:
        print("bro paeentar")
        count = count + 1
