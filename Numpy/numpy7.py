import numpy as np
import pandas as pd

lending_co_lt = np.genfromtxt("./redo/csv_files/lending-co-LT.csv", delimiter = ',')
#lending_co_lt = pd.read_csv("./redo/csv_files/lending-co-LT.csv")

print(lending_co_lt)

#based on what dtpe we set it as, it will alter our output so its better to not assume a datatype of the data

