
# coding: utf-8

# In[2]:


import ctypes # provides low-level arrays
import sys
#from pympler import asizeof
class DynamicArray:
    def __init__ (self):
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array
    def __len__(self):
        return self._n
    def getitem (self, k):
        #”””Return element at index k.”””
        if not 0 <=k < self._n:
            raise IndexError('invalid index')
        return self._A[k] # retrieve from array
    def append(self, obj):
        #”””Add object to end of the array.”””
        if self._n == self._capacity: # not enough room
            self._resize(2*self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c): # nonpublic utitity
        #”””Resize internal array to capacity c.”””
        print("Şuan worst case durumunda, liste dolu iken ekleme yapılıyor.")
        print("Başka yerden n*2lik yer ayrılıp taşıma yapılacak")
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c
    def _make_array(self, c): # nonpublic utitity
        #”””Return new array with capacity c.”””
        return (c*ctypes.py_object)( )
    def getsize(self):
        return sys.getsizeof(self._A)
    def getLength(self):
        return self._capacity


# In[28]:

c=DynamicArray()
for i in range(10):
    c.append(" add an item"+str(i))
    print(str(i)+ " eklendi, dizi boyutu:",str(c.getLength()))

