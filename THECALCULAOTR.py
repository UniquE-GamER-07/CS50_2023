from turtle import delay
print('Hello and welcome to THE CALCULATOR hope this will help find your answers ')
a=float(input("Enter your first number = "))
b=float(input("Enter your second number = "))
print("make sure to read what is written before typing your Arithmetic operation... It will you make your life easier")
print("please type [add] if you want to add the number")
print("please type [sub] if you want to subtract the number")
print("please type [div] if you want to divide the number")
print("please type [mul] if you want to multiply the number")
print("make sure to type the same way as instructed in the box given above")
user_input=input("please enter your Arithmetic operation from above = ")
if user_input=='add':
    print("here is your answer",a+b)
elif user_input=='sub':
    print("here is your answer",a-b)
elif user_input=='div':
    print("here is your answer",a/b)
elif user_input=='mul':
    print("here is your answer",a*b)
else:
    print("sorry I think your put a wrong input")
    print("please try again")

qwerty=input("do you want to use it again? = ")

if qwerty=='no':
    print("ok bye")
    delay(3)
    quit()
elif qwerty=='yes':
    print("good choice lets continue...")    
a=float(input("Enter your first number = "))
b=float(input("Enter your second number = "))
print("make sure to read what is written before typing your Arithmetic operation... It will you make your life easier")
print("please type [add] if you want to add the number")
print("please type [sub] if you want to subtract the number")
print("please type [div] if you want to divide the number")
print("please type [mul] if you want to multiply the number")
print("make sure to type the same way as instucted in the box given above")
user_input=input("please enter your Arithmetic operation from above = ")
if user_input=='add':
    print("here is your answer",a+b)
elif user_input=='sub':
    print("here is your answer",a-b)
elif user_input=='div':
    print("here is your answer",a/b)
elif user_input=='mul':
    print("here is your answer",a*b)
    
else:
    print("sorry I think your put a wrong input")
    print("please try again")
    delay(3)
    quit()