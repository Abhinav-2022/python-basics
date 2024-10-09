#you can use index number{0}
#to be sure the arguments are placed in the correct placeorder
quantity = 3
itemono = 567
price = 49.40
myorder = "i want to pay {2} dollar for {0} pieces of item{1}."
print(myorder.format(quantity,itemono,price))