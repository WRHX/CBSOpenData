import numpy as np



class dataObject():
    '''

    '''
    def __init__(self, filepath):
        self.t = 't'
        self.filepath = filepath

        self.data = None
        self.rows = None
        self.columns = None
        self.rowRange = None
        self.colRange = None
        self.headerDict = {}

    def fillDataArray(self):
        ''' self.data : self.data[row][col] '''
        self.data = np.genfromtxt(self.filepath, delimiter = ';', dtype = None)

        self.rows = len(self.data)
        self.columns = len(self.data[0])
        self.rowRange = range(0,self.rows)
        self.colRange = range(0,self.columns)

    def decodeData(self):
        ''' Creating self.data with dtype = None, elements byte format, use .decode('UTF-8') '''
        for row in self.rowRange:
            for col in self.colRange:
                self.data[row][col] = self.data[row][col].decode('UTF-8')

    def createHeaderDict(self):
        ''' Make dict that connects column title to their column index '''
        for col in self.colRange:
            self.headerDict.append


    def printFirstRow(self):
        print(self.data[0])
