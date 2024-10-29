#Write a Python program to determine a student's grade
# based on their score and attendance rate.

#If the score is 70 or above, check the attendance rate:
#If the attendance rate is 90% or above, print "Grade: A"
#If the attendance rate is between 80% and 89%, print "Grade: B"
#If the attendance rate is below 80%, print "Grade: C"
#If the score is below 70, print "Grade: F" regardless of attendance  rate

score =87
attendance_rate = 89
if score>=70:
    if attendance_rate >=90:
        print( " grade A")
    elif 80 <= attendance_rate <90:
        print("grade B")
    else:
        print("grade C")

else:
    print("grade F")