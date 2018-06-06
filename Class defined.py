# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:49:30 2018

@author: perso
"""
#%%

class Product:
     
     Version = "Ver 1.2 Rev 3"
     
     def _init_(self,sku,name,brand,manu,dims,wt,wtunits):
          self.SKU = sku
          self.Name = name
          self.Brand = brand
          self.Manufacture = manu
          self.Dimensions = dims
          self.Weight = wt            #should have been weight
          self.Wtunits = wtunits
          
     def Print(self):
          out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+\
          "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacture"Dimensions\n"+\
          "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n\n"+\
          "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
     print out
     
     def Setphone(self.PhoneNum):
          # phone number format is XXX-XXX-XXXX
          
          dgts="0123456789"
       
          BadFmt =False
          if type(PhoneNum)!=type("abc") or len(PhoneNum)!=12:
               BadFmt=True
          
          if PhoneNum[3] = "-" or PhoneNum[7]!="-":
               BadFmt=True
               
          if not (PhoneNum[0] in dgts and PhoneNum[1] in dgts and \
                  PhoneNum[2] in dgts and PhoneNum[4] in dgts and \
                  PhoneNum[5] in dgts and PhoneNum[6] in dgts and \
                  PhoneNum[8] in dgts and PhoneNum[9] in dgts and \
                  PhoneNum[10] in dgts and PhoneNum[11] in dgts):
               BadFmt = True
               
          if BadFmt:
               print "Wrong phone number format. Use \"xxx-xxx-xxxx\"\n"
               return False
          
          self.__Phonenumber = PhoneNum
          
          return True 
     
     def GetPhone(self):
          return self._PhoneNumber
     
#%%
          
Milk23 = Product ("DAR023", "VG Skim Milk", "Very Good Brands", "Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
#%%               
               
               