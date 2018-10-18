def fn(n):
    i=0
    while i<n:
        yield i
        i+=1


gen=fn(5)
for i in gen:
    print(i)

def odd_generator(n):
    i=0
    while i<n:
        if i%2!=0:
            yield i
        i+=1


for i in odd_generator(10):
    print("i:",i)
