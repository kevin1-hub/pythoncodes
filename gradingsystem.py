# write a program to show grading system of 3 subjects


math=int(input("enter marks foe mathematics"))
english=int(input("enter marks for english"))
kiswahili=int(input("enter marks for kiswahili"))

avg=((math+kiswahili+english)/3)
print(avg)

if((avg<=100) and (avg>=70)):
    print("grade A")
    
elif((avg<=69) and (avg>=60)):
    print("grade B")
    
elif((avg<=50) and (avg>=70)):
    print("grade c")
    
elif((avg<=40) and (avg>=49)):
    print("grade D")
    
elif((avg<=0) and (avg>=39)):
    print("grade c")
    
else:
    print("invalid input")