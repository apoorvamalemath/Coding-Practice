"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No.

Sample Input 0

6 4
give me one grand today night
give one grand today

Sample Output 0

Yes

Sample Input 1

6 5
two times three is not four
two times two is four

Sample Output 1

No

Explanation 1

'two' only occurs once in the magazine.

Sample Input 2

7 4
ive got a lovely bunch of coconuts
ive got some coconuts

Sample Output 2

No

Explanation 2

Harold's magazine is missing the word

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
