Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

    int arr: an array of integers

Returns

    float: the resulting float value rounded to 3 places after the decimal

Input Format

The first line contains the integer,
, the size of .
The second line contains the space-separated integers,

.

Constraints

Sample Input

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

Sample Output

169.375


def average(array):
    # your code goes here
    arr1 = set(array)
    return (sum(arr1)/len(arr1))

    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
