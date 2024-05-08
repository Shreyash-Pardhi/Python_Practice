n=int(input())
# num=[]
# for i in range(n):
#     num.append(int(input()))
num = list(map(int,input().split()))

def ex(n, num):
    for j in range(n):
        for i in range(n):
            if i<(n-1) and num[i] > num[i+1]:
                num[i], num[i+1]=num[i+1], num[i]      
    return num

print(ex(n, num))