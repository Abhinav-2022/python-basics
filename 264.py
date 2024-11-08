# Create a method in the Book class.
# Insert a function that returns a formatted string
# with the book title and author,
# and execute it on the b1 object.

class Book():
    def __init__(self,title,auther):
        self.title = title
        self.auther = auther

    def get_info(self):
        return f"'{self.title}' by {self.auther}"
b1 = Book("to kill a mocking bird","harper lee")
print(b1.get_info())