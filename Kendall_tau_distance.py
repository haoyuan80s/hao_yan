import random; random.seed(1)
a = [1,2,3,4,5,6]
b = a[:]; random.shuffle(b)

def K(a,b):
    """measure ranking distance to lists a,b"""
    n = len(a)
    return sum( [  (a[i] < a[j] and b[i] > b[j])
                   or (a[i] > a[j] and b[i] < b[j])
                   for i in range(n)
                   for j in range(i+1, n)])

def Kpp(a,b):
    """
    measure ranking distance to lists a,b,
    with panlize more low ranking mismatch 
    and high dist mismatch
    """
    n = len(a)
    return sum([(j-i)/(j+i)*((a[i] < a[j] and b[i] > b[j])
                   or (a[i] > a[j] and b[i] < b[j]))
                   for i in range(n)
                   for j in range(i+1, n)])
