# x=15
# def my_fun():
#     global x
#     x=10
#     y=10
#     print(x+y)
# my_fun()    
import random
def guess_num():
    return random.randint(1,100)
target_number=guess_num()
attempts=0
while True:
    user_goes=int(input("guess the number"))
    attempts+=1
    if user_goes==target_number:
        print("congratulation you guessed it right:",attempts,"attempts")
        break
    elif user_goes>target_number:
        print("try a smaller num")
    else:
        print("try a higher num")        
