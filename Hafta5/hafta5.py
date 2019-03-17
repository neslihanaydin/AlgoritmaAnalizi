
# coding: utf-8

# In[1]:



#normal fonk Paraustu 
def minparabul(para,paralist):
    kacfarkli=0
    while(para):
        for i in range(len(paralist)-1,-1,-1):
            if(paralist[i]<=para):
                para=para-paralist[i]
                print("1 Tane",paralist[i])
                kacfarkli=kacfarkli+1
                break
    return kacfarkli

print("Kullanılan para sayısı:",minparabul(293,[1,5,10,25,50]))



#recursive paraustu
def recMC(coinValueList,change):
    minCoins=change
    if(change in coinValueList): 
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if(numCoins<minCoins):
                minCoins=numCoins
    return minCoins

recMC([1,5,10,25,50],43)


def rec_fb(n,result):#recursive fibonacci
    if n<2:
        return n
    elif(result[n]!=0):
        return result[n]
    else:
        result[n]=rec_fb(n-1,result)+rec_fb(n-2,result)
        return result[n]
    
rec_fb(20,[0]*21)
for i in range(13,50):
    print(rec_fb(i,[0]*(i+1)),end=" ")


#Fibonaccide uyguladigimizi para ustu fonka uygulayalim
def recMC2(coinValueList,change,knownResults):
    minCoins=change
    if(change in coinValueList): 
        knownResults[change]=1
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC2(coinValueList,change-i,knownResults)
            if(numCoins<minCoins):
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins

for i in range(8,20):
    print(i," ",recMC2([1,5,10,25,50],i,[0]*(i+1)))

