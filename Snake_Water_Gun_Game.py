import random

name= input("Enter your name: ")

# computerChoice= random.choice([0,1,-1])
computerChoice= random.randint(-1,1)
userChoice= input("Enter your choice 's', 'w', 'g' : ")

userDic= {'s': 0, 'w':1, 'g':-1}
computerDic={0:"Snake", 1:"Water", -1:"Gun"}

user= userDic[userChoice]

print(f"Your choice: {computerDic[user]}\nComputer choice: {computerDic[computerChoice]}")

if user==computerChoice:
    print("Draw!")
else:
    if user==0 and computerChoice==1:
        print(f"{name} WIN this battle")
    elif user==0 and computerChoice==-1:
        print(f"{name} LOSE this battle")
    elif user==1 and computerChoice==0:
        print(f"{name} WIN this battle")
    elif user==1 and computerChoice==-1:
        print(f"{name} LOSE this battle")
    elif user==-1 and computerChoice==0:
        print(f"{name} WIN this battle")
    elif user==-1 and computerChoice==1:
        print(f"{name} lose this battle")