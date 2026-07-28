class Solution(object):
    def convertTemperature(self, celsius):
      res=[]
      kelvin=celsius+273.15
      Fahrenheit=celsius*1.80+32.00
      res=[kelvin,Fahrenheit]
      return res