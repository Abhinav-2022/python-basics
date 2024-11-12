#stop iteration
#stop after 20 th iteration
#from logging.config import stopListening

#
# class Mynumbers:
#     def __iter__(self):
#         self.a = 1
#         return
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
# n1 = Mynumbers
# myiter =iter(n1)
# for x in myiter:
#         print(x)


    # Stop iteration
    # Stop iteration at 20

# class Numbers:
#         def _iter_(self):
#             self.a = 1
#             return self
#
#         def _next_(self):
#             if self.a <= 20:
#                 x = self.a
#                 self.a += 1
#                 return x
#             else:
#                 raise StopIteration
#
#
# n1 = Numbers()
# myiter = iter(n1)
#        for x in n1:
#             print(x)

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# Create an instance of the class
n1 = Mynumbers()

# Get an iterator from the in stance
myiter = iter    (n1)

# Use the iterator in a for loop
for x in myiter:
    print(x)

