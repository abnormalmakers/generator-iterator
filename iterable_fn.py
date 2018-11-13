l1=['中国移动','中国联通','中国电信']
l2=[10086,10010,10000,9999]

for t in zip(l1,l2):
    print(t)

for n,a in zip(l1,l2):
    print(n,a)

print(dict(zip(l1,l2)))

def myzip(iter1,iter2):
    it1=iter(iter1)
    it2=iter(iter2)
    while True:
        v1=next(it1)
        v2=next(it2)
        yield (v1,v2)

for n,a in myzip(l1,l2):
    print(n,a)


for index,value in enumerate(l1):
    print(index,value)

for index,value in enumerate(l1,start=2):
    print(index,value)


def write_fn():
    while True:
        a=input(">>>")
        if not a:
            break
        yield a

for i in write_fn():
    print(i)

arr=[1,2,3]
arr1=arr*3
print(arr1)

