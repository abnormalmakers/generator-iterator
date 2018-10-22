def fn():
    yield 2
    yield 3
    yield 4

gen=fn()
print(gen,type(gen))
print(next(gen))
print(next(gen))
it=iter(gen)
print(it,type(it))

# print(next(it))
# print(next(it))
# print(next(it))


generators=(x for x in range(1,10))
print(generators,type(generators))
