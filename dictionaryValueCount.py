a=[1,1,1,3,3,4,5,6,5,3,4,3,3,5,7,7,5,4,3,3,3,3,5,6,7,8,8,8,78,6,5,4,3,3,3,3,3,3,3,3,3,3,3,3]
dict={}
for i in a :
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
