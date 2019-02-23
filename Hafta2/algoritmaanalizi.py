
# coding: utf-8

# In[130]:

sayac = 0
def power(x,y):
    global sayac
    t = 1
    for i in range(y):
        sayac = sayac +1
        t = t*x
    return (t,sayac)
def call_report(x,y):
    global sayac
    sayac = 0
    r = power(x,y)
    print (x," üzeri ",y," degeri : ",r[0]," cagrim sayisi : ",sayac)
call_report(4,60)


# In[131]:

power(4,60)


# In[132]:

def power_recursive(x,y):
    global sayac 
    sayac = sayac + 1
    if( y == 0):
        return 1
    if(y == 1):
        return x
    if(y%2 == 0):
        return power_recursive(x*x,y//2)
    if(y%2 == 1):
        return (power_recursive(x*x,y//2))*x
def call_report_recursive(x,y):
    global sayac
    sayac = 0
    r = power_recursive(x,y)
    print(x," üzeri ",y,"degeri : ",r," cagrim sayisi : ",sayac)
call_report_recursive(4,60)


# In[127]:

power_recursive(4,60)


# In[128]:

def selectionSort(dizi):
    for i in range(len(dizi)):
        minindex = i
        for j in range(i+1, len(dizi)):
            if (dizi[minindex] > dizi[j]):
                minindex = j
            
        dizi[i], dizi[minindex] = dizi[minindex], dizi[i]
    
    for i in dizi:
        print (i)


# In[110]:

dizi = [34,68,23,12,90,44]
selectionSort(dizi)


# In[ ]:



