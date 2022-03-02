#!/usr/bin/env python
# coding: utf-8

# # 🐍 Kurz Python Jupyter - 9. časť

# PIP, Moduly, Scope, Scipy, Power BI

# # 01. PIP

# In[19]:


# !pip help                      
get_ipython().system('pip show cowsay')


# In[2]:


get_ipython().system('pip list')


# In[40]:


import cowsay as c
c.cow("Python je super")
# cowsay.cow("Java je super")
c.beavis(" . ")
c.dragon("....")
c.ghostbusters("...")
c.cheese("Cauko")
c.tux("Lol")


# In[41]:


get_ipython().system('pip install camelcase')


# In[42]:


get_ipython().system('pip show camelcase')


# In[44]:


import camelcase as c
tmp = c.CamelCase()

print(tmp)
print(type(tmp))

cele_meno = "adam sangala"

print(tmp.hump(cele_meno))


# In[47]:


# !pip install mysql-connector
get_ipython().system('pip install pymongo')


# # 02. Scope (Obor platnosti/Rozsah)

# In[64]:


# Globalny Scope/rozsah
level = 60
print(level)

def vypis_smajlik():
    # Lokalny Scope/rozsah
    text = "Usmej sa"
    print(":-)")
    print(text)

# Globalny Scope/rozsah
 
def vykresli_had():
    print("🐍")  
    
def vypis_prva_uroven():
    print("1. uroven - 🚗")
    global a 
    a = "1. uroven - 🚗"
    print(a)
    print(level)
    
    def vypis_druha_uroven():
        print("2. uroven - 🚕")
        a = "2. uroven - 🚕"
        print(a)
        print(level)
        
    vypis_druha_uroven()
    

# Globalny Scope/rozsah  
    
# vypis_smajlik()    
# vykresli_had()
vypis_prva_uroven()
print(a)

# NameError: name 'text' is not defined
# print(text)


# # 03. Vlastne moduly

# In[ ]:


def vypocitaj_obsah_stvorca(a):
    """
    a strana stvorca v cm
    """
    return a * a

# Slovnik/Dictionary
# Kluc : Hodnota
profil_osoba = {
    "meno" : "Adam",
    "email": "adam.sangala@gmail.com",
    "krajina": "Slovensko"
}

