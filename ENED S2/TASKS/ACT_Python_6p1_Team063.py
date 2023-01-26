# Open files
DataFile = open('TempC.txt','r')
ResultsFile = open('TempF.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
for k in range(len(Data)):
    DataN = float(Data[k])
    DataF = (DataN*9/5)+32
    ResultsFile.write('{:0.0f}\t\n'.format(DataF))

# Close files
DataFile.close()
ResultsFile.close()