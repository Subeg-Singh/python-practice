#rotate array-Leetcode 189
def rotator(k):
   global array
   array=eval(input('enter an array'))
   for i in range(1,k+1):
       array.insert(0,array[-1])
       array.pop()

k=eval(input('how many times u wnna rotate the array?'))
rotator(k)
k%=len(array)
print(array)
