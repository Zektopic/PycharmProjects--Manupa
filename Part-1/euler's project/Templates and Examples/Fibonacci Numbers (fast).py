from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonnaci(n):
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    elif n > 2 :
        return fibonnaci(n-1) + fibonnaci(n-2)
for n in range(1, 501):
    print(n, ":",fibonnaci(n))

