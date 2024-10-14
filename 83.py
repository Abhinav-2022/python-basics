#perform a case-insensitive sort of the list

thislist = ["banana", "orange", "kiwi", "cherry"]

thislist.sort(key=str.lower)

print(thislist)

#the key parameter is set to str.lower

#which means that the list will be sorted based
#on the lowercase  version of each string element


#"banana".lowe()return"banana"
#"orange".lower()return"orange"
#"kiwi".lowe()return"kiwi"
#"cherry".lower()return "cherry"
