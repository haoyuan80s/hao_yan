import random; random.seed(1)
a = [1,2,3,4,5,6]
b = a[:]; random.shuffle(b)

def K(a,b):
    n = len(a)
    return sum( [  (a[i] < a[j] and b[i] > b[j])
                   or (a[i] > a[j] and b[i] < b[j])
                   for i in range(n)
                   for j in range(i+1, n)])
