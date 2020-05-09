grades=[]


for i in range(0,4):
    user_input = int(input("Enter the grades:"))
    grades.append(user_input)
print(str((grades)))

grades.sort(reverse=True)   #sorting from highest to lowest
print(str(grades))

removed_grade=grades.pop()
print("removed grades are:"+str(removed_grade))
removed_grade=grades.pop()
print("removed grades are:"+str(removed_grade))

print("remainig grades are:",str(grades))
print("1st grade is :",grades[0])