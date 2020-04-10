"""

Given an array with positive number the task to find the largest subsequence from array that contain elements which are Fibonacci numbers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array.
Output:
For each test case in a new line print the space separated elements of the  longest fibonacci subsequence.

Constraints:
1<=T<=100
1<=N<=100
1<=A[]<=1000

Example:
Input:
2
7
1 4 3 9 10 13 7
9
0 2 8 5 2 1 4 13 23

Output:
1 3 13
0 2 8 5 2 1 13 

"""

def Find (arr, n):
    temp=[]
    temp.extend(arr)
    arr.sort()
    
    max=arr[n-1]
    FS=[1,1]
    for i in range(2,n):
        FS.append(FS[i-1]+FS[i-2])
    #print(FS)
    start=0
    for i in range(n):
        for j in range(start,len(FS)):
            if(temp[i]==FS[j]):
                print(temp[i], end=" ")
                break
    print()
    
test_cases=input()
for i in range(int(test_cases)):
    no_ele =int(input())
    arr = list(map(int,input().split()))
    Find(arr,no_ele)
