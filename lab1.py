import numpy as np
import matplotlib.pyplot as plt

def create_array(N,v):
    return [v] * N

def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def sum_numbers_float32(numbers):
    sum = np.float32(0)
    for number in numbers:
        sum += number
    return sum

def error(a,b):
    return abs(a-b)
    
def relative_error(a,b):
    return abs(a - b) / b

def zad2(numbers):
    a = sum_numbers(numbers)
    b = sum_numbers_float32(numbers)

    print(a)
    print(b)
    print(error(a,b))
    print(relative_error(a,b))

def zad3(N,numbers):
    result = []
    i = 0
    sum1 = 0
    sum2 = np.float32(0)
    while i < N:
        sum1 += numbers[i]
        sum2 += numbers[i] 
        if i % 25000 == 0:
            result.append(relative_error(sum1,sum2))
        i += 1
    plt.plot(result)
    plt.show()

def recursive_sum(numbers):
    if len(numbers) == 1: return numbers[0]
    return recursive_sum(numbers[:len(numbers)//2]) + recursive_sum(numbers[len(numbers)//2 :])
    
def zad5(numbers):
    a = recursive_sum(numbers)
    b = sum_numbers(numbers)
    print(error(a,b))
    print(relative_error(a,b))

if __name__== '__main__':
    N = 10**7

    v = np.float32(0.53125)
    numbers = create_array(N,v)

    print(zad5(numbers))
    
r = 1
x0 = 0.5

def xn(n,r,x0):
    if n <= 0:
        return r * x0 * (1 - x0)
    x = xn(n - 1, r, x0)
    return r * x * (1 - x)

x = []
rr = []
while r <= 4:
    x.append(xn(100,r,x0))
    rr.append(r)
    r += 0.0001

plt.plot(x)
plt.show()

