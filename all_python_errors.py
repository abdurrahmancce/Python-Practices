import re 
for i in dir (__builtins__):
    if re.match('^[A-Z][a-zA-Z]+Error$', i):
        print(i)