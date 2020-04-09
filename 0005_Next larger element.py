"""
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1

Explanation:
Testcase1: In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.

"""


def Find (ele):
    res={}
    for i in range(len(ele)):
        res[ele[i]] =-1
    stack=[]
    for i in range(len(ele)):
        if(len(stack)>0):
            if(ele[i]>stack[-1]):
                while((ele[i]>stack[-1])):
                    res[stack[-1]]=ele[i]
                    stack.pop()
                    if(len(stack)==0):
                        break
                stack.append(ele[i])
            else:
                #if not greater
                stack.append(ele[i])
        else:
            #if no ele in stack-->Push
            stack.append(ele[i])

    RESULT=res.values()
    print(' '.join(map(str, RESULT)))
#Find([1, 3, 2, 4])
#Find([1,2,3,4])
#Find([7, 8, 1, 4])
#Find([1, 3, 2, 4])
#Find([10, 3, 12, 4, 2, 9, 13, 0, 8, 11, 1, 7, 5, 6])
#Find([7, 8, 1, 4])

test_cases=input()
for i in range(int(test_cases)):
    no_ele =int(input())
    ele =list()
    ele = list(map(int, input().split()))
    Find(ele)
