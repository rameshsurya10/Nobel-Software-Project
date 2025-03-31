# import jwt
# import datetime

# def code():

#     secret_code = "Well,Yeahh"

#     # payload={
#     #     "user_id": 1,
#     #     "user_name": "admin",
#     #     "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5)
#     # }

#     # encode = jwt.encode(payload,secret_code,algorithm="HS256")

#     # print(encode)

#     de_code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJhZG1pbiIsImV4cCI6MTc0MzE2NzI0Nn0.-lz6pl5yJdZ-qA7IltfhfJZklZCkVAl6B1wBt6DHw2I"

#     encode = jwt.decode(de_code,secret_code,algorithms=["HS256"])

#     print(encode)

# code()



# def game():
#     import random

#     print("Welcome to the Game")
#     print("You have to guess the number between 1 to 100")

#     num = random.randint(1,100)

#     chances = 0

#     while chances < 5:
#         guess = int(input("Enter your guess: "))

#         if guess == num:
#             print(f"Congratulation you have guessed the number in {chances} chances")
#             break
#         elif guess < num:
#             print("Your guess is too low")
#         else:
#             print("Your guess is too high")
        
#         chances += 1

#     if chances == 5:
#         print(f"Sorry you have lost the game, the number was {num}")
# game()

def signal():

    select = sele.lower()

    if select == "start":
        print("The car is started")
        for i in range(1,3):
            print("The car is moving")
        print("The car is stopped")

        select = input("Enter the direction (left/right/stright): ")

        

        if select == "left" or "right" or "straight":
            print(f"The car is moving in the direction of {select}")
        for i in range(1,3):
            print("The car is moving")
        print("The car is stopped")

        select = input("Enter the direction (left/right/stright): ")

        

        if select == "left" or "right" or "straight":
            print(f"The car is moving in the direction of {select}")
        for i in range(1,3):
            print("The car is moving")
        print("The car is stopped")

        select = input("Enter the direction (left/right/stright): ")

        

        if select == "left" or "right" or "straight":
            print(f"The car is moving in the direction of {select}")
        for i in range(1,3):
            print("The car is moving")
        print("The car is stopped")

        select = input("Enter the direction (left/right/stright): ")

    

        if select == "right":
            print(f"The car is moving in the direction of {select}")
            for i in range(1,3):
               print("The car is moving")
            print("The car is stopped")
            print("The car is parked")
        else:
             print("destination is not reached")

    else:
        print("The car is not started")

sele = input("Enter the signal (start/stop): ")
signal()
