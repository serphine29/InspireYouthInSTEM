#make a table to solve quadratic equation 
from prettytable import prettytable

#specify the column while initializing the table
myTable = pretty table(["variables","value of x","equation","result"])

#add rows
myTable.add-row(["x","0","5x^3 2 x^2 +8x +9","9"])
myTable.add-row(["x","1","5x^3 2 x^2 +8x +9","26"])
myTable.add-row(["x","2","5x^3 2 x^2 +8x +9","73"])
myTable.add-row(["x","3","5x^3 2 x^2 +8x +9","180"])
myTable.add-row(["x","4","5x^3 2 x^2 +8x +9","377"])
myTable.add-row(["x","5","5x^3 2 x^2 +8x +9","694"])
myTable.add-row(["x","6","5x^3 2 x^2 +8x +9","1161"])
myTable.add-row(["x","7","5x^3 2 x^2 +8x +9","1808"])
myTable.add-row(["x","8","5x^3 2 x^2 +8x +9","2665"])
myTable.add-row(["x","9","5x^3 2 x^2 +8x +9","3762"])

print(myTable)
