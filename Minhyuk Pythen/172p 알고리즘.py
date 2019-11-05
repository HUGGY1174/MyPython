a=[]
for b in range(8):
    n=input("단어:")
    a.append(n)
    print(n,"추가")
a.sort()
print(a)



def 순차(data,search):
    i=0
    while i<=7:
        if data[i]==search:
            return i+1
        else:
            i+=1

def 이진(data,search):
    left=0
    right=7
    count=0
    mid=int((left+right)/2)
    while left<=right:
        if data[mid]==search:
            return count+1
        elif data[mid]>search:
            count+=1
            right=mid-1
        else:
            count+=1
            left=mid+1
        mid=int((left+right)/2)
b=input("찾는 단어:")
print("순차 탐색 횟수",순차(a,b))
print("이진 탐색 획수",이진(a,b))
