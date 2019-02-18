import math
import csv
from gekko import GEKKO
import sys

print("List all the points on a circle with integer 'x' values")
print("Circle equation in (x-h)^2+(y-k)^2=r^2 form for circle with centerpoint (h, k)")
print("r, h, and k values must be integers")
print("enter 'r' value")
r = int(sys.stdin.readline())
print("enter 'h' value")
h = int(sys.stdin.readline())
print("enter 'k' value")
k = int(sys.stdin.readline())
b = 2*h
c = h**2 - r**2
m = GEKKO()
f1 = m.Var(value=1)
f2 = m.Var(value=-1)
m.Equation(f1+f2==b)
m.Equation(f1*f2==c)
m.solve(disp=False)
f_1 = [float(i) for i in f1.value]
f_2 = [float(i) for i in f2.value]


solutions1 = []
solutions2 = []

def F(x):
    factors = abs((x-f_1[0])*(x-f_2[0]))
    sqrtfactors = round(math.sqrt(factors), 2)
    solution1 = sqrtfactors + 12
    if ".000" or ".999" in  solution1:
        rounded_solution1 = int((10*solution1-0.5)+1) / 10.0
        point1 = ('(%s, %s)' % (x, float(rounded_solution1)))
        solutions1.append(point1)
    else:
        point1 = ('(%s, %s)' % (x, float(solution1)))
        solutions1.append(point1)
    solution2 = sqrtfactors - 12
    if ".000" or ".999" in  solution2:
        rounded_solution2 = int((10*solution2-0.5)+1) / 10.0
        point2 = ('(%s, %s)' % (x, float(rounded_solution2)))
        solutions2.append(point2)
    else:
        point2 = ('(%s, %s)' % (x, float(solution2)))
        solutions2.append(point2)
    
def solve():
    for x in range(4, 21):
        F(x)
    zip(solutions1, solutions2)

solve()

with open('filepath.txt', 'w+') as file:
    #replace "filepath" with the filepath of where you want the .txt file to be located
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(zip(solutions1, solutions2))


    
    
