import numpy as np
from matplotlib import pyplot as plt

#datatypes =  [('myint','i8'),('myfloat','f8'),('mystring','S5')]
data = np.genfromtxt('data.csv', delimiter = ';', dtype = None)

print(data[0])
rows = len(data) # 2342
columns = len(data[0]) # 22

rowRange = range(0,rows)
colRange = range(0,columns)

yearList = ['2012 MAN','2012 VROUW','2013 MAN','2013 VROUW','2014 MAN','2014 VROUW','2015 MAN','2015 VROUW','2016 MAN','2016 VROUW']
yearDict = {
'2012 MAN':12,
'2012 VROUW':13,
'2013 MAN':14,
'2013 VROUW':15,
'2014 MAN':16,
'2014 VROUW':17,
'2015 MAN':18,
'2015 VROUW':19,
'2016 MAN':20,
'2016 VROUW':21,
}
OPLEIDINGSNAAM = 'B Bedrijfskunde'
totaal = 0
YearSex = '2012 MAN'
menArray = np.array([])
womenArray = np.array([])
arrayIndex = 0

for YearSex in yearList:
    for row in rowRange:
        if row == 0:
            continue
        if data[row][9].decode('UTF-8') == OPLEIDINGSNAAM:
            numberOfStudents = int(data[row][yearDict[YearSex]].decode('UTF-8'))
            totaal = totaal + numberOfStudents
            if 'MAN' in YearSex:
                menArray = np.append(menArray,numberOfStudents)
            if 'VROUW' in YearSex:
                womenArray = np.append(womenArray,numberOfStudents)
            arrayIndex += 1

            #print(data[row][yearDict[YearSex]].decode('UTF-8'))
    print('Total number of students @ ' + str(YearSex) + ': ' + str(totaal))
print(menArray)
print(womenArray)

plt.plot(menArray, color = 'b')
plt.plot(womenArray, color = 'r')
plt.plot(menArray - womenArray, color = 'y')
plt.show()

'''
for n in colRange:
    print(data[0][n])
    if data[0][n] == b'OPLEIDINGSNAAM ACTUEEL':
        print(n)
ans 9
'''
