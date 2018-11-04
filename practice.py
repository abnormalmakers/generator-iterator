def generator_fn(begin,end):
    if end<2:
        return False
    elif begin>end:
        print(1)
        begin,end=end,begin
        print(begin,end)
        for i in range(begin,end):
            if i<2:
                continue
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                yield i
    else:
        for i in range(begin,end):
            if i<2:
                continue
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                yield i
begin=100
stop=2
l=[x for x in generator_fn(begin,stop)]
print(l)



def myrange(start,stop=None,step=1):
    if stop is None:
        stop=start
        start=0
        while start<stop:
            yield start
            start+=step
    else:
        while start<stop:
            yield start
            start+=step


for i in myrange(10,step=2):
    print(i)









