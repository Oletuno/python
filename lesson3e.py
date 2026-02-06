# below is a grading system based on what a student will have gotten
marks = int(input("enter student's marks"))
print("the entered marks is ", marks)
# print("the entered marks is ", marks)
if marks <30:
    print("below average")
 elif marks >= 30 and  marks < 40:
    print("average")   
 elif marks >= 40 and marks <70:
    print("above average")  
  else:
    print("excellent")   