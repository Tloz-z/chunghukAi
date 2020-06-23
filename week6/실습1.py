#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
num1 = int(input("첫 번째 정수 : "))
num2 = int(input("두 번째 정수 : "))
operator = input("연산자 : ")
result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "//":
    result = num1 // num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
else:
    print("잘못된 연산자 입니다.")
    sys.exit()

print(f"{num1} {operator} {num2} = {result}")


# In[ ]:




