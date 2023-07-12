import random
ans=input("Do you want to roll the dice ?(y/n):")    
while ans=='y':
    no=random.randint(1,6)
    print(no)
    ans='n'
    if ans=='n':
     ans=input("Do you want to roll the dice ?(y/n):")      
