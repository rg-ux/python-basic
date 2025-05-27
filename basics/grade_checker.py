marks = int(input("enter the total number of marks \n"))

if marks >=90 :
    Grade = 'A'

elif marks >= 80 and marks <= 89 :
    Grade = 'B'

elif marks >= 70 and marks <= 79 :
    Grade = 'C'
    
elif marks >= 60 and marks <= 69 :
    Grade = 'D'

else:
    Grade = 'F'

print("Your Grade is ", Grade)