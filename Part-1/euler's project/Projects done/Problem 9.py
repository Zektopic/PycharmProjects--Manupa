def pythagorean_triplet(n):
    for b in range(n):
        for a in range(1, b):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                print(a, b, c)
                print(float(a*b*c))


pythagorean_triplet(1000)