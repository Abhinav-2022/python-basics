#Task: Write a Python function called summarize_numbers
#Create a function that can take an arbitrary number of numerical arguments. The function should print the following:

#The total sum of the numbers.
#The average of the numbers.
#If no numbers are provided, it should print: "No numbers provided."
#Call the function with the numbers 10,20, and 30.

def summarize_numbers(*args):
    if not args:
        print("no number is provide")

    total_sum = sum(args)
    average = total_sum / len(args)
    print("average:", average)


#calling the function with numbers 10 ,20,and 30
summarize_numbers(10,20,30)