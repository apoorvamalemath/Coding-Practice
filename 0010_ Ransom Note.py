"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""

def Find(str1,str2):
    str1=list(str1.split())
    str2=list(str2.split())
    index={}
    flag=0

    for i in range(len(str1)):
        if str1[i] in index:
            index[str1[i]]+= 1
        else:
            index[str1[i]] =1

    #print(index)

    count=0
    for i in range(len(str2)):
        if(str2[i] in index):
            if(index[str2[i]]>=1):
                index[str2[i]]-=1
                count=count+1
            #print(str2[i])

    if(count==len(str2)):
        print("Yes")
    else:
        print("No")

#Find("ive got a lovely bunch of coconuts", "ive got some coconuts")
#Find("two times three is not four", "two times two is four")
n=list(map(int, input().split()))
str1=input()
str2=input()
Find(str1,str2)
