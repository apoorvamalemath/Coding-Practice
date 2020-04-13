"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring
. The words "be" and "cat" do not share a substring. 

Sample Input

2
hello
world
hi
world

Sample Output

YES
NO


"""

def Find(str1,str2):
    str1=list(str1)
    str2=list(str2)
    index={}
    flag=0

    for i in range(len(str1)):
        index[str1[i]] =[i]

    for i in range(len(str2)):
        if(str2[i] in index):
            flag=1
            print("YES")
            break
    if(flag==0):
        print("NO")

#Find("hello","world")
#Find("hi","world")

tc=int(input())
for i in range(tc):
    str1=input()
    str2=input()
    Find(str1,str2)

