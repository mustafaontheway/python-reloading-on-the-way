import pandas as pd 

weekly_sales_by_employee = {"aysel": 15_000, "hakan": 22_400, "kağan": 12_700, "bengü": 24_300, "bilge": 22_478}

ws = pd.Series(weekly_sales_by_employee)

print(ws > 15_000)

print("**********************")

print(ws[ws > 15_000])

"""
aysel    False
hakan     True
kağan    False
bengü     True
bilge     True
dtype: bool
**********************
hakan    22400
bengü    24300
bilge    22478
dtype: int64

"""
