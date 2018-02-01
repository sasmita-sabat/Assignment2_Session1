
# coding: utf-8

# In[2]:


#Print the numbers in a comma separated values  which are divisible by 7 and not multiple of 5 .
#Range of numbers from 2000 to 32000
l=[]
for i in range(2000,3200):
       if i % 7 == 0 and i % 5 == 1:
               l.append(str(i))
#To print the comma separated list.                
print("The numbers which are divisible by 7 and not multiple of 5:\n"+",".join(l)) 

