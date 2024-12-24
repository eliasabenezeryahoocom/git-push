from typing import List
def compress(chars: List[str]) :
        x=""
        count=0
        left=0
        right=1
        while right<=len(chars)-1:
            if chars[left]==chars[right]:
                 right+=1
                 count+=1
            else:
                x+=chars[left]
                for i in str(count-left):
                    x+=i
                left=right
                right=left+1
        print(len(x)) 
        print(x)
compress(["a","a","b","b","c","c","c"])
    


        