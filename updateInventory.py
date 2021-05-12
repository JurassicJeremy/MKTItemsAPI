import requests
import json
from openpyxl import load_workbook

file = ("D:\Documents\Python stuff\Projects\MKTItemsAPI\items.xlsx")

wb = load_workbook(file, data_only=True)
ws = wb.active

# Need to loop through column, add to each itemNumber
for row in ws.rows:
    item = (row[0].value)
    print(item)


    payload = json.dumps([
        {
            "nextAvailableDate": None,
            "isAvailable": True,
            "qtyAvailable": 666,
            "itemNumber": item
        },
        {
            "nextAvailableDate": None,
            "isAvailable": True,
            "qtyAvailable": 555,
            "itemNumber": item
        },
        {
            "nextAvailableDate": None,
            "isAvailable": True,
            "qtyAvailable": 444,
            "itemNumber": item
        },
        {
            "nextAvailableDate": None,
            "isAvailable": False,
            "qtyAvailable": 333,
            "itemNumber": item
        },
        {
            "nextAvailableDate": None,
            "isAvailable": True,
            "qtyAvailable": 222,
            "itemNumber": item
        }
    ])
headers = {
    'x-api-key': 'd843ec7a50cf568b220e3ec6fb2bc795',
    'Content-Type': 'application/json'
}
inventoryUrl = "https://api.reptimeqa.com/reptime/public/api/import/manufacturers/M32685/inventory"

response = requests.request("POST", inventoryUrl, headers=headers, data=payload)

print(response.text)
