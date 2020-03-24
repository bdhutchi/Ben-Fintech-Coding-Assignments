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

    if option_type in ['C','P']:
        if option_type in ['C']:
            Opt_Price=S*ss.norm.cdf(d1)-K*np.exp(-r*T)*ss.norm.cdf(d2)
            Delta=ss.norm.cdf(d1)
            Gamma=ss.norm.cdf(d1)/(S*vol*np.sqrt(T))
            Vega=S*ss.norm.cdf(d1)*np.sqrt(T)
            Theta=-(S*ss.norm.cdf(d1)*vol)/(2*np.sqrt(T))-r*K*np.exp(-r*T)*ss.norm.cdf(d2)
            Rho=K*T*np.exp(-r*T)*ss.norm.cdf(d2)
        else:
            Opt_Price=K*np.exp(-r*T)*ss.norm.cdf(-d2)-S*ss.norm.cdf(-d1)
            Delta=-ss.norm.cdf(-d1)
            Gamma=ss.norm.cdf(d1)/(S*vol*np.sqrt(T))
            Vega=S*ss.norm.cdf(d1)*np.sqrt(T)
            Theta=-(S*ss.norm.cdf(d1)*vol)/(2*np.sqrt(T))+r*K*np.exp(-r*T)*ss.norm.cdf(-d2)
            Rho=-K*T*np.exp(-r*T)*ss.norm.cdf(-d2)
        else:
            Opt_Price= 'Error: option type incorrect. Choose P for a put option or C for a call option.'
        print Opt_Price
        print 'Delta = {}'.format(Delta)
        print 'Gamma = {}'.format(Gamma)
        print 'Vega = {}'.format(Vega)
        print 'Theta = {}'.format(Theta)
        print 'Rho = {}'.format(Rho)


