'''
*       *
**     **
***   ***
*********
***   ***
**     **
*       *
'''

n=int(input('enter the number of rows:'))
for i in range(1, n + 1):
    if i==n:
        print('*'*(2*n+1),end="")
    else:
        print('*'*(i)+' '*(2*(n-i)+1)+'*'*(i),end="")
    print()
for i in range(n - 1, 0 ,-1):
    print('*'*(i)+' '*(2*(n-i)+1)+'*'*(i))