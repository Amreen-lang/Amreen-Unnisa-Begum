#!/usr/bin/env python
# coding: utf-8

# In[ ]:


countinuation


# In[ ]:


organizing the list : 


# In[3]:


subjects = ['maths','science','english','hindi','arabic','comptuper','social']


# In[4]:


print(subjects)


# In[5]:


type(subjects)


# In[ ]:


# i want to arrange the above list in alphabetical order. 


# In[ ]:


two approaches:
    
    1. temp approach =====> sorted ====> we will be able to maintain the original order
    
    2. permanent approach ========> sort ====> changes will be implied permannently 


# In[7]:


print(sorted(subjects))


# In[8]:


print(subjects)      # here we can see that the list is not changed as we have used sorted


# In[10]:


subjects.sort()


# In[11]:


print(subjects)


# In[ ]:


# request : i want to reverse the above list in the reverse order.


# In[13]:


subjects.reverse()


# In[14]:


print(subjects)


# In[ ]:


# req : i want to calculate the no of elements?


# In[15]:


len(subjects)


# In[ ]:


zen  of python : 


# In[16]:


import this


# In[ ]:





# In[ ]:


slicing of lists : 


# In[ ]:


[startvalue : stop value : step count]


# In[ ]:


Note : stop value is always exclusive, to include the stop value we have to increase + 1. 


# In[ ]:





# In[17]:


colors = ['red','yellow','green','blue','purple','pink']


# In[ ]:


# req : i want to get the ncolors of red and yellow


# In[18]:


print(colors[0:2])


# In[19]:


print(colors[4:6])


# In[20]:


print(colors[0:6:2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




