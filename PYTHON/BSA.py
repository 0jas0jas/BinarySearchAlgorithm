import random
import time

print("CHOOSE A NUMBER BETWEEN 1 AND 100")
time.sleep(3)

min = 1
max = 100
attempts = 1
def game(min, max, attempts):
    while(1 <= 10):
        randInt = random.randrange(min, max, 1)
        print("*************************************")
        print("IS YOUR NUMBER " + str(randInt) + "?")
        print("*************************************")
        status = int(input("YES THIS IS MY NUMBER! -- 0 \nNope my number is smaller -- 1 \nNah my number is larger -- 2 \n"))
        while(status >= 0 and status <=2):
            if (status == 0):
                break
            elif (status == 1):
                max = randInt
                break
            elif (status == 2):
                min = randInt
                break
        attempts = attempts + 1 
        if (status < 0 or status > 2):
            print("Invalid Input. Try again.")
        if status == 0: 
            print("WoW it took " + str(attempts - 1) + " to find your number") 
            break
            
   
        

game(min, max, attempts)


again = input("Do you wanna play again? (y/n): ")
if (again == 'y' or again == 'Y'):
    game(min, max, attempts)