class Solution(object):
    def constructRectangle(self, area):
        w=int(area**0.5)
        while(w>0):
            if(area%w==0):
                break
            w=w-1
        return [area/w,w]
        