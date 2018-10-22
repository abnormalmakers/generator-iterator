l=[1,2,3,4]

lst=[x for x in l]
gen=(x for x in l)

print(lst)
print(gen)

l[1]=222

print(lst)
print(gen)

for i in gen:
    print(i)
