"""
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.

Output:
For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.

Constraints:
1 <= T <= 100
1 <= N, M, X <= 106
-106 <= A, B <= 106
Example:
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1

Explanation:
Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.

"""

def Find (ele1,ele2,sum):
    ele1.sort()
    ele2.sort(reverse=True)
    temp=0
    z=0
    for i in range(len(ele1)):
        for j in range(temp,len(ele2)):
            if((ele1[i]+ele2[j])==sum):
                if(z!=0):
                    print(",",end=" ")
                print(ele1[i], ele2[j],end="")
                temp=j+1
                z=z+1
                break
            elif((ele1[i]+ele2[j])<sum):
                temp=j
                break

    if(z==0):
        print("-1")
    else:
        print()


Find([1, 2, 4, 5, 7],[5, 6, 3, 4, 8],9)
#Find([0,2],[1,3],3)

#Find([1, 23, 12, 9, 30, 2, 50],3)

test_cases=input()
for i in range(int(test_cases)):
    no_ele1,no_ele2 ,sum =(map(int, input().split()))
    ele1 =list()
    ele1 = list(map(int, input().split()))
    ele2 =list()
    ele2 = list(map(int, input().split()))
    Find(ele1,ele2, sum)
