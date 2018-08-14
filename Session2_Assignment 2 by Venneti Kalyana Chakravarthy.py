
# coding: utf-8

# # Date 11th August 2018 - Session 2 - Assignment 2

# In[1]:


#Question 1
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list

a=input('enter the numbers:')
l=[]
l=a.split(",")
print("The generated list is:", l)


# In[2]:


#Question 2
#Create the below pattern using nested for loop in Python.

s=''
i=0
while i <= 5:
    print(s.center(i,'*'))
    i=i+1
while i>0:
    print(s.center(i-2,'*'))
    i=i-1


# In[3]:


#Question 3
#Write a Python program to reverse a word after accepting the input from the user.
#Sample Output:
#Input word: AcadGild
#Output: dilGdacA

a=str(input("Input word: "))
print("Output Word:",a[::-1])


# In[4]:


#Question 4
#Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

print("WE,THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t   and to secure to all its citizens")

