# def hello_dtsc5502() :
#   print("Hello DTSC5502@")

# def greeting(name: str) -> str:
#   return 'Hello '+ name +' from the greeting function!'

# def calculate_mean(lst: list) -> float:
#   sum_ele = 0
#   # for i in lst:
#   #   sum_ele += i
#   return sum(lst) / len(lst) 
    

# def calculate_median(lst: list):
#   lst.sort()
#   n1 = int(len(lst)/2)
#   n2 = int((len(lst)/2) + 1)
#   if(len(lst)%2 == 0):
#     m1 = lst[n1]
#     m2 = lst[n2]
#     num = (m1+m2)/2
#   else:
#     num = lst[n1]
#   return num
    
    
    
# def calculate_mode(lst: list):
#     count = 0
#     temp = 0
#     idx = 0
#     for i in range(0,len(lst)):
#         j = i+1
#         for j in range(i+1,len(lst)):
#             if(lst[j]==lst[i]):
#                 count+=1

#         if count > temp:
#             temp == count
#             idx = i

  
#     return lst[idx]  
      
    

import sympy as sp

# Define the variables and the function
x, y = sp.symbols('x y')
f = 4*x**2 + x*y + 4*y**2

# Calculate the gradient of the function
grad_f = [sp.diff(f, var) for var in (x, y)]

# Find the critical points by solving the system of equations grad_f = [0, 0]
critical_points = sp.solve(grad_f, (x, y))

# Print the critical points
print("Critical Points:")
for point in critical_points:
    print(point[x])
    print(point[y])