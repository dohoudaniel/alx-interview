"""
n = input("Enter a number: ")
triangle = []
numRows = n
increase = int(numRows)
triangle.append([1])
for i in range(1, increase):
    row = [1]
    decrease = int(i - 1)
    for j in range(1, decrease):
        value = triangle[i-1][j-1] + triangle[i-1][j]
        row.append(value)
    row.append(1)
    triangle.append(row)

print(triangle)
"""
#
class Solution:
    def generate(numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            # print(temp)
            row = []
            # print(len(res[-1]))
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
                print(row)
            res.append(row)
            print(res)
            print()
        print(res)

print()
Solution.generate(3)
