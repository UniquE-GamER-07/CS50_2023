from turtle import delay

print("hello this is just a random things i am doing at 4:35 am in the morning hope this helps :)")
print("please enter your numbers here and chose what you want to do.")
a=float(input("please enter your first number : "))
b=float(input("please enter your second number: "))
print("BFORE GOING ON..... read this it will make your life way easier")
print("please type [add] if you want to add the number")
print("please type [sub] if you want to subtract the number")
print("please type [div] if you want to divide the number")
print("please type [mul] if you want to multiply the number")
print("make sure to type the same way as instucted in the box given above")
user_input=input("Please enter what you want to do : ")
if user_input=='add':
    print("this is your answer : ", a+b)
if user_input=='sub':
    print("this is your answer : ", a-b)
if user_input=='div':
    print("this is your answer : ", a/b)
if user_input=='mul':
    print("this is your answer : ", a*b)
else:
    print("bro really i quit :)")
    delay(5)
    quit()

