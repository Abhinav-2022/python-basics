#string format
#use the format ()method to insert number into string
quanity =3
itemno = 598
price = 49.95
myorder = "i want {} pieces of item{} for {} dollar"
print(myorder.format(quanity,itemno,price))