import pandas as pd 
  
# to read csv file named "samplee" 
showTable = pd.read_csv("showTable.csv", encoding = "ISO-8859-1") 
showDB = pd.read_csv("showDB.csv", encoding = "ISO-8859-1") 
# to save as html file 
# named as "Table" 
showTable.to_html("./web/showTable.htm") 
showDB.to_html("./web/showDB.htm") 
