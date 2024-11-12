#search the string to see if it starts with
#"the" and ends with "spain"
import re

txt = "the rain in spain "
x = re.search("^the *Spain$",txt)
if x:
    print("yes! we have a match")
else:
    print("no match")
    #  ^ -----	Starts with
    #  .  ------	Any character (except newline character)
    #  *  -------	Zero or more occurrences
    #  $ ------	Ends with