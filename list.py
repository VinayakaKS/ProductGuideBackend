
import pandas as pd
Chemicals_dataframe = pd.read_excel('Chemicals.xls', sheet_name=0) 
chemicals_list = Chemicals_dataframe['Chemical Name'].tolist()
print(chemicals_list)
