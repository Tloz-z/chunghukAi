#!/usr/bin/env python
# coding: utf-8

# In[16]:


id = int(input("번호 "))
korean = int(input("국어 점수 : "))
english = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
science = int(input("물리 점수 : "))

total = korean + english + math + science
ave = total / 4
grade = ""

if ave >= 90:
    grade = "A"
elif ave >= 80:
    grade = "B"
elif ave >= 70:
    grade = "C"
elif ave >= 60:
    grade = "D"
else:
    grade = "F"

print("===============================================================")
print(" 번호    국어    영어    수학    물리    총점     평균    학점")
print("===============================================================")
print(f"  {id}      {korean}      {english}      {math}      {science}      {total}     {ave}     {grade}")

