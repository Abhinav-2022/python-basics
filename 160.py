#check if key exist
#to determine if a specified key is present in
#a dictionary use the in keyword

#check if "model" is present in the dictionary

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1974

}
if "model" in thisdict:
    print("yes 'model'is one of the keys in thisdict dictionary ")

else:
    print("not in thisdict")