a={1:30,3:40,5:60}
b={2:40,3:50,6:80}

for i in b.keys():
    if i in a.keys():
        a[i]= a[i]+b[i]
    else:
        a[i]=b[i]
print(a)