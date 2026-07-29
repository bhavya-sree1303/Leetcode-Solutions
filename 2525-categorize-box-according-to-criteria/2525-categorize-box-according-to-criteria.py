class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        bulky = length>=10000 or width>=10000 or height>=10000 or length*width*height>=1000000000
        heavy = mass>=100
        
        if bulky and heavy: return "Both"
        if bulky: return "Bulky"
        if heavy: return "Heavy"
        return "Neither"