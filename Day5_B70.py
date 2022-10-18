#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introdustion to list datatype :


# In[ ]:


defination : A list is a collection of items maintained in a particular order.
    
classification : It is classifed as a mutable data type. 
    
how to declare the list datatype ------> []


# In[ ]:





# In[4]:


students = ['amreen','zaheer','tanveer','rasheed','abdul','yusra']


# In[5]:


print(students)


# In[ ]:


# how to access the elements from the above lists?


# In[ ]:





# In[ ]:


understanding the concept of indexing? 0,1,2,3.......


# In[ ]:


# req : i want acess zaheer name in the output.....


# In[6]:


print(students[1])


# In[7]:


print(students[1].title())


# In[8]:


# req : I want to access abdul name in the output..


# In[9]:


print(students[4].title())


# In[ ]:





# In[ ]:


get_ipython().set_next_input('1. how to add a new element in the list');get_ipython().run_line_magic('pinfo', 'list')

get_ipython().set_next_input('2. how to modify the element in the lis');get_ipython().run_line_magic('pinfo', 'lis')

get_ipython().set_next_input('3. how to delete the elements in the list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:





# In[ ]:


# req : I want to add Iqrah name in the above list...


# In[12]:


students.append('iqrah')


# In[13]:


print(students)


# In[ ]:


# req = to add neha


# In[15]:


students.append('neha')


# In[16]:


print(students)


# In[ ]:


# req : add sidiqa to the 2nd index position


# In[17]:


students.insert(2,'sidiqa')


# In[18]:


print(students)


# In[19]:


print(students[2])


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().set_next_input('how to modify elements in the list');get_ipython().run_line_magic('pinfo', 'list')


# In[22]:


print(students)


# In[ ]:


# i want to modify sidiqa name to mariyam.


# In[24]:


students[2] = 'mariyam'


# In[25]:


print(students)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('how to delete elements form the list');get_ipython().run_line_magic('pinfo', 'list')


# In[26]:


print(students)


# In[ ]:


# req : I want to delete mariyam


# In[27]:


del students[2]


# In[29]:


print(students)


# In[ ]:




