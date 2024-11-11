#Create an Iterator
#To create an object/class as an iterator you have to
#implement the methods _iter() and __next_() to your object.

#Create an iterator that returns numbers,
# starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.) ?

class Mynumbers1:
    def __iter__(self):
        self.a = 1  # Initialize the starting number
        return self  # Return the iterator object itself

    def __next__(self):
        x = self.a
        self.a += 1  # Increment for the next number
        return x  # Return the current number


# Create an instance of the Mynumbers1 class
myclass1 = Mynumbers1()

# Get the iterator
myiter2 = iter(myclass1)

# Print the first three numbers
print(next(myiter2))  # Output: 1
print(next(myiter2))  # Output: 2
print(next(myiter2))  # Output: 3
# Use for loop to automatically call _next_ until StopIteration is raised
# Use for loop to automatically call _next_ until StopIteration is raised
# for num in myclass
# print(num)
