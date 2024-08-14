def main():
    name= input("Enter your name: ")
    print(f"Welcome, {name} to Kaun Banega Crorepati")

    questions= [
        ["Which of the following is a valid variable name in Python?", "a) 1variable", "b) variable1", "c) variable-1", "d) variable@1", 2],
        ["What is the output of the following code?\npython\nprint(2 * 3 + 5)\n", "a) 11", "b) 16", "c) 21", "d) 23", 1],
        ["Which keyword is used to define a function in Python?", "a) func", "b) define", "c) def", "d) function", 3],
        ["What is the correct file extension for Python files?", "a) .pyt", "b) .pyth", "c) .pt", "d) .py", 4],
        ["What will be the output of the following code?\npython\nprint(type(3.14))\n", "a) <class 'int'>", "b) <class 'float'>", "c) <class 'double'>", "d) <class 'str'>", 2],
        ["How do you insert comments in Python code?", "a) //", "b) /*", "c) #", "d) **", 3],
        ["Which function is used to get the length of a string in Python?", "a) length()", "b) len()", "c) size()", "d) strlength()", 2],
        ["What will be the output of the following code?\npython\nprint('Hello' + ' ' + 'World')\n", "a) HelloWorld", "b) Hello World", "c) Hello+World", "d) 'Hello' ' ' 'World'", 2],
        ["What is the correct syntax to create a dictionary in Python?", "a) {key1: value1, key2: value2}", "b) [key1: value1, key2: value2]", "c) (key1: value1, key2: value2)", "d) <key1: value1, key2: value2>", 1],
        ["Which of the following is used to start a loop in Python?", "a) for", "b) while", "c) loop", "d) both a and b", 4],
        ["What will be the output of the following code?\npython\nprint(10 // 3)\n", "a) 3.3333", "b) 3", "c) 4", "d) 3.0", 2],
        ["How do you create a list in Python?", "a) []", "b) {}", "c) ()", "d) <>", 1],
        ["Which of the following is a built-in function in Python?", "a) sqrt()", "b) pow()", "c) power()", "d) exp()", 2],
        ["What is the output of the following code?\npython\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[2])\n", "a) 1", "b) 2", "c) 3", "d) 4", 3],
        ["What will be the output of the following code?\npython\nif 5 > 2:\n print('Five is greater than two!')\n", "a) Five is greater than two!", "b) Error", "c) 5 > 2", "d) None of the above", 1],
        ["How do you start an if statement in Python?", "a) if", "b) if()", "c) if:", "d) if()", 1]
    ]

    levels= [1000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]

    answer= () 

    money=0

    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i][0]}\n{questions[i][1]}        {questions[i][2]}\n{questions[i][3]}       {questions[i][4]}")
        try:
            answer= int(input("Enter your answer in 1-4, 0 to Quit: "))
        except ValueError:
            print("Please enter value between 1 to 4 (in integer format) ")
        if answer ==0 :
            print("You Quit the game!!")
            break 
        elif answer==questions[i][5]:
            print(f"Correct answer, you won {levels[i]} Rupees")
            if i==4 or i==8 or i==15:
                money=levels[i]
        elif answer==1 or answer==2 or answer==3:
            print(f"Wrong Answer, The correct answer is {questions[i][5]}\n{name}, you take {money} Rupees at your home")
            break 
        else:
            print("Something went wrong, please run the game again")
            break
    else:
        print(f"Congratulations Mr. {name}, You answered all questions correctly and won Kaun Banega Crorpati\nYou take home the huge amount of {levels[i]} at your home")

if __name__=="__main__":
    main()