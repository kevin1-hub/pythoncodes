# write a program to show the bonus given interms salary and the no of years worked

year=int(input("enter the number of years"))
salary=int(input("enter salary"))

if(year>10):
    print("you receive 10% bonus")
    print(0.1*salary(+salary))
    
elif(year>6 and year<10):
    print("you receive 10% bonus")
    print(0.08*salary(+salary))
    
elif(year<6):
    print("you receive 5 % discount")
    print(0.06*salary(+salary))
    print("your net salary is" 0.06*salary(+salary))