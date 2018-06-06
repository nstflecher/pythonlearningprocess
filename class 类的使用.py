# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:05:57 2018

@author: perso
"""

# Product Structure
#
# SKU
# Product Name 
# Brand
# Manufacturer
# As a list [width, depth, height, units]
# Weight 
# Units 

#%%
class VGSM:
    SKU="DAR023"
    Name="VG Skim Milk"
    Brand="Very Good Brands"
    Manufaturer="georgia Diary, Inc."
    Dimensions=[8,8,10,"in"]
    Weight=2.2
    WtUnits="lbs"
    
#%%    
class Product:
     
     Version = "Ver 1.2 Rev 3"
     
    def _init_(self,sku,name,brand,manu,dim,wt,wtUnits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dim
        self.weight = wt
        self.WtUnits = wtUnits
        
Milk23 = Product ("DAR023", "VG Skim Milk", "Very Good Brands", "Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
     def Print(self):
          out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+\
          "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacture"Dimensions\n"+\
          "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n\n"+\
          "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
     print out
#%%
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)

print my_car.model
print my_car.color
print my_car.mpg




     




