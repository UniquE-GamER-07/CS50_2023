from turtle import delay
print("Hello and welcome to The calculator I hope this will help you find all your answers")
a=float(input("Enter you first number : "))
b=float(input("Enter your second number : "))
print("make sure to read what is written below before entering your Arithematic operation... it will make your life easier :)")
print("type [add] if you want to add your numbers")
print("type [sub] if you want to subtract your numbers")
print("type [div] if you want to divide your numbers")
print("type [mul] if you want to multiply your numbers")
print("make sure to type the same way as instructed in the box given above :)")
user_input=input("please enter your arithematic operation = ")

if user_input=="add":
    print("This is your answer :", a+b)
elif user_input=="sub":
    print("this is your answer ", a-b)
elif user_input=="div":
    print("this is your answer :", a/b)
elif user_input=="mul":
    print("this is your answer :", a*b)
else:
    print("I think there is a mistake ")
    print("please try again")

qwerty=input("do you want to use it again? (Y/N) = ")

if qwerty=="N":
    print("ok byeeee")
    delay(3)
    quit()
    
elif qwerty=="Y":
    print("good choice lets continue...")
a=float(input("Enter you first number : "))
b=float(input("Enter your second number : "))
print("make sure to read what is written below before entering your Arithematic operation... it will make your life easier")
print("type [add] if you want to add your numbers")
print("type [sub] if you want to subtract your numbers")
print("type [div] if you want to divid your numbers")
print("type [mul] if you want to multiply your numbers")
print("make sure to type the same way as instructed in the box given above :)")
user_input=input("please enter your arithematic operation")

if user_input=="add":
    print("This is your answer :", a+b)
elif user_input=="sub":
    print("this is your answer ", a-b)
elif user_input=="div":
    print("this is your answer :", a/b)
elif user_input=="mul":
    print("this is your answer :", a*b)
    
else:
    print("I think there is a mistake ")
    print("please try again later")
    delay(3)
    quit()

