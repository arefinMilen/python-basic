str= 'aghdhhdjv123433489$%#@!&*'

digit=0
char=0
sChar=0

for i in str:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        sChar += 1

print(f"your countings are:\nNumbers = {digit}\nCharacters = {char}\nSpecial Characters = {sChar}")
