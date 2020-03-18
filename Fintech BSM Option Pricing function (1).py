#!/usr/bin/env python
# coding: utf-8

# In[12]:


def BSMOptionPrice(option,S,K,T,r,vol):
    #S = Spot Price
    #K = Strike Price
    #T = Time to Maturity
    #r = Risk Free Rate
    #Vol= Asset Volatility

    import numpy as np
    import scipy.stats as si
    


# In[13]:


    d1 = (np.log(S / K) + (r + 0.5 * vol ** 2) * T) / (vol * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * vol ** 2) * T) / (vol * np.sqrt(T))


# In[10]:


    if option == 'call':
    result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif option == 'put':
    result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    return result


# In[14]:


print(BSMOptionPrice('call',100.0,75.0,0.5,.0125,.35))


# In[ ]:




