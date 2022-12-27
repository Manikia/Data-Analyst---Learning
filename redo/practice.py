import pandas as pd
import numpy as np

wellsdata = './redo/csv_files/creditWells.csv'
#wellsdata2 = pd.DataFrame(wellsdata, columns = ['Date', 'Transaction', 'delete1', 'delete2', 'Transaction Name'])
dataformat = pd.read_csv(wellsdata, index_col = 0, names = ['Date', 'Transaction', 'delete1', 'delete2', 'Transaction Name'])
print(dataformat)

#print(np.loadtxt('./redo/csv_files/creditWells-NAN.csv'))
datagen = "./redo/csv_files/creditWells-NAN.csv"
genfromtxt = np.genfromtxt(datagen, delimiter = ',', names = True, dtype = None, encoding = None)
print(genfromtxt)

#using dtype will reformat everything as the type we are initializing as and if we use loadtxt it can work since its looking for a type but cant find it so we are setting everything even the empty cells as a type which will work when working with loadtxt
loadtxt = np.loadtxt(datagen, delimiter = ',', dtype = np.str)
print(loadtxt)



