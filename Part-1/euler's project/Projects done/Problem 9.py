import math
def pythagorean_triplet(n):
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                if a +b+c == 1000:
                    print(a, b, int(c))
                    print(a*b*c)


pythagorean_triplet(1000)