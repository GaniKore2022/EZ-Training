l=[[1,2,3],[4,4,6],[7,8,9]]
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==j and l[i][j]%2!=0:
            s=s+l[i][j]
print(s)
# n=int(input())
# s=0
# while(n>0):
#     r=n%10
#     s=s+r
#     n=n//10
# print(s)