class Solution(object):
    def isHappy(self, n):
        def get_sum(n):
            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n=n//10
            return total 
        slow=n
        fast=n
        while  True:
            slow=get_sum(slow)
            fast=get_sum(get_sum(fast))
            if slow==1 or fast==1:
                return True
            if slow==fast:
                return False            

       
        