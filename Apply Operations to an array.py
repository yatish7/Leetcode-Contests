class Solution(object):
    def applyOperations(self, a):
        n=len(a)
        for i in range(n-1):
            if a[i]==a[i+1]:
                a[i]=2*a[i]
                a[i+1]=0
            else:
                continue
        for i in range(n):
            if a[i]==0:
                a.remove(a[i])
                a.append(0)
        return a
                