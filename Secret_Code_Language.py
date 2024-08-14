import random
import string

def encode():
    message= input("Enter your message here: ")
    split_message= message.split(" ")
    encode_message=[]

    for word in split_message:
        if len(word)>=3:
            word= word[1: ] + word[0]
            new_word= ''.join(random.choices(string.ascii_letters, k=3)) + word + ''.join(random.choices(string.ascii_letters, k=3))
            encode_message.append(new_word)
        else:
            word= word[ : :-1]
            encode_message.append(word)

    print(' '.join(encode_message))

def decode():
    message = input("Enter your encoded message here: ")
    split_message = message.split(" ")
    decoded_message = []

    for word in split_message:
        if len(word)>=3:
            word= word[3:-3]
            decoded_word= word[-1] + word[:-1]
            decoded_message.append(decoded_word)
        else:
            decoded_word= word[ : :-1]
            decoded_message.append(decoded_word)
    print(' '.join(decoded_message))

try:
    choice= int(input("Enter '1' for secret coding\nEnter '0' for decoding: "))
    if choice==1:
        encode()
    elif choice==0:
        decode()
    else:
        print("Invalid choice")
except ValueError:
    print("Enter value ('1' or '0') .")