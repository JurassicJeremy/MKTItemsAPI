import requests
import json
from openpyxl import load_workbook

file = ("D:\Documents\Python stuff\Projects\MKTItemsAPI\items.xlsx")

wb = load_workbook(file, data_only=True)
ws = wb.active

for row in ws.rows:
    item = (row[0].value)
    print(item)
