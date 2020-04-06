"""Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15"""

def sum_arr( ele, sum ):
    s=0
    start=0
    end=0
    flag=0
    i=0
    while i<(len(ele)):
        if(s<=sum):
            s=s+ele[i]
            end=i
            if(s==sum):
                flag=1
                break
            elif(s>sum):
                while(s>sum):
                    s=s-ele[start]
                    start=start+1
                if(s==sum):
                    flag=1
                    break
        i=i+1

    if(flag==1):
        print(start+1,end+1)
    else:
        print("-1")



#sum_arr([1 ,2 ,3 ,7 ,5],12)
#sum_arr([1, 2 ,3 ,4 ,5, 6, 7, 8, 9, 10],15)
test_cases=input()
for i in range(int(test_cases)):
    no_ele, sum=map(int, input().split())
    ele =list()
    ele = list(map(int, input().split()))
    sum_arr(ele,sum)
