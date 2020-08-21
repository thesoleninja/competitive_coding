# https://assessment.hackerearth.com/challenges/hiring/amazon-hiring-challenge/algorithm/akash-and-gcd-1-15/
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a, a)
    
def f(x):
    return sum( gcd(i, x) for i in range(1,x+1))

def C(x, y):
    return sum( f(arr[i-1]) for i in range(x, y+1)) % (10**9+7)

def U(x, y):
    arr[x-1] = y
    return ''

n = int(input())
arr = list( map(int, input().split()))
Q = int(input())
for q in range(Q):
    query = input().split()
    q1 = int(query[1])
    q2 = int(query[2])
    print(eval(query[0])(q1, q2))
