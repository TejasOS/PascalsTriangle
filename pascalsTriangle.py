# :)

import math
def pascalsTriangle(rowNums):
  numCounter = 1
  row = []
  for n in range(rowNums):
    for k in range(numCounter):
      row.append(math.comb(n, k))
    numCounter+=1
    numSpaces = rowNums-len(row)
    print(numSpaces*" "+" ".join(map(str, row)))
    row = []

pascalsTriangle(int(input("How many rows do you want to print of Pascal's triangle? ")))
