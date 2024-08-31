a={1:"samsul",2:"arefin",3:"milen"}
print(a[3])
a[4]="musa"
print(a)

b ={33:"rahim",44:'karim',55:'bakker'}
c={66:"asif",99:'rakib',44:"faisal"}

b.update(c)
print(b)
for i in b.values():
    print(i)