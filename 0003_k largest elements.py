"""Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed in decreasing order.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and k, N is the size of array and K is the largest elements to be returned. The second line of each test case contains N input C[i].

Output:
Print the k largest element in descending order.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
K ≤ N
1 ≤ C[i] ≤ 1000

Example:
Input:
2
5 2
12 5 787 1 23
7 3
1 23 12 9 30 2 50

Output:
787 23
50 30 23

Explanation:
Testcase 1: 1st largest element in the array is 787 and second largest is 23.
Testcase 2: 3 Largest element in the array are 50, 30 and 23.
"""

#code
def Find (ele,no):
    ele.sort()
    no=len(ele)-no
    l=ele[no:]
    #print(no)
    l.sort(reverse=True)
    print(' '.join(map(str, l)))

#Find([12, 5, 787, 1, 23],2)
#Find([1, 23, 12, 9, 30, 2, 50],3)

test_cases=input()
for i in range(int(test_cases)):
    no_ele,no =(map(int, input().split()))
    ele =list()
    ele = list(map(int, input().split()))
    Find(ele,no)
