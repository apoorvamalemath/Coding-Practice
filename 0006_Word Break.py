"""
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

Input:
First line is integer T denoting number of test cases. 1<=T<=100.
Every test case has 3 lines.
First line is N number of words in dictionary. 1<=N<=12.
Second line contains N strings denoting the words of dictionary. Length of each word is less than 15.
Third line contains a string S of length less than 1000.

Output:
Print 1 is possible to break words, else print 0.

Example:
Input:
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike
Output:
1
0
"""



def Find (words, input):
    words.sort(key=len)
    str=list(input)
    start=0
    count=0
    st=0
    n=len(words)-1
    maxlen=len(words[n])

    for i in range(st,len(input)+1):
        str1 = ""
        s=str[st:i]
        temp=str1.join(s)
        ind=0
        for j in range(len(words)):
            ind=ind+1
            if(len(temp)>len(words[j])):
                continue
            elif(len(temp)<len(words[j])):
                break
            else:
                flag=0
                while(len(temp)==len(words[j])):
                    if(temp==words[j]):
                        count=count+len(temp)
                        flag=1
                        st=i
                        break
                    if(flag==1):
                        break
                    if((j+1)<len(words)):
                        j=j+1
                    else:
                        break
                if(flag==1):
                    break
    if(count==len(input)):
        print("1")
    else:
        print("0")


test_cases=input()
for i in range(int(test_cases)):
    no_ele =input()
    words =list()
    words = list(input().split())
    inpt=input()
    Find(words,inpt)
