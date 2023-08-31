#!/usr/bin/env python
# coding: utf-8

# # Write a program to create a 5 dimensional array with all Zeros & Ones.

# In[1]:


import numpy as np


# In[2]:


np.array([[1,0,1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1,0,1]],ndmin=5)


# 
# # Write a program to create an array of 10 Zeros, 10 Ones and 10 Fives in row 1,2 and 3 which create a new array of shape (3,10).

# In[3]:


np.array([[[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1],[5,5,5,5,5,5,5,5,5,5]]])


# 
# # Write a program to create a 3x4 matrix filled with values from 10 to 21.

# In[5]:


arr1 = np.arange(10,22).reshape(3,4)


# In[6]:


print(arr1)


# 
# # Write a program to create a 10x10 Zero matrix with elements on the main diagonal equal to 0,1,2,3,4,5,6,7,8,9

# In[9]:


np.arange(0,10,1)
np.diag([0,1,2,3,4,5,6,7,8,9])


# 
# # Write a program to create a 4x4 array. Create an array from below array by swapping first and last, second and third columns.

# In[11]:


arr2 = np.arange(1,17).reshape(4,4)
arr2[:,[0,-1]] = arr2[:,[-1,0]]
arr2[:,[1,2]] = arr2[:,[2,1]]
arr2


# 
# # What a program to reverse an array (The First Element Becomes the Last).
# 
# # [51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66]

# In[12]:


arr3 = int(input())
arr4 = int(input())
x = np.arange(arr3,arr4+1)
x[::-1]


# 
# # Write a program to access all the elements greater than 30 and less than 80 and multiples of 5 from an array of shape 10,10. Elements range from 1 to 100.

# In[14]:


arr5 = np.arange(1,101).reshape(10,10)
arr5 = arr5[arr5%5==0]
arr5 = arr5[arr5>30]
arr5 = arr5[arr5<80]
arr5


# 
# # Write a program to create a 2D array with 1 on the border and 0 inside.

# In[16]:


arr6 = np.ones((9,9),dtype=int)
arr6[1:8,1:8] = 0
arr6


# 
# # Write a program to create a checkerboard pattern .Don't use default array function
# 
# # Checkerboard pattern:                     
# ## [0 1 0 1 0 1 0 1]
# ## [1 0 1 0 1 0 1 0]
# ## [0 1 0 1 0 1 0 1]
# ## [1 0 1 0 1 0 1 0]
# ## [0 1 0 1 0 1 0 1]
# ## [1 0 1 0 1 0 1 0]

# In[18]:


arr7 = np.zeros((8,8),dtype=int)

arr7[[0,0,0,0],[1,3,5,7]] = 1
arr7[[1,1,1,1],[0,2,4,6]] = 1
arr7[[2,2,2,2],[1,3,5,7]] = 1
arr7[[3,3,3,3],[0,2,4,6]] = 1
arr7[[4,4,4,4],[1,3,5,7]] = 1
arr7[[5,5,5,5],[0,2,4,6]] = 1
arr7[[6,6,6,6],[1,3,5,7]] = 1
arr7[[7,7,7,7],[0,2,4,6]] = 1
arr7


#  # Write a program to find common values between two arrays.
#  
#  ## Expected Output :
#  ## array1 : [10 20 40 60]
#  ## array2 : [10 30 40 50]

# In[19]:


array1 = np.array([[1,2,3,4,5,6]])
array2 = np.array([[4,5,6,7,8,9]])
np.intersect1d(array1,array2)


# 
# #  Write a program to create an array 2D array and then reshape into 1D array.

# In[23]:


i = np.arange(1,21).reshape(4,5)
i.flatten()

