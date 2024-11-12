#print the position (start -and end postion)
#of the first match occurrence
#the regular expression looks for any words
#that starts with an upper case "s"
import re

txt = "the rain in spain "
x = re.search(r"\bs\w+",txt)
print(x.span())