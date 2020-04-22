import json
import sys

currency = sys.argv[1]
quantity = sys.argv[2]

with open('/home/udalny/scripts/rate.json') as f:
    data = json.load(f)

for element in data:
    if element['Cur_Abbreviation'] == currency.upper():
        per_one = element['Cur_OfficialRate'] / element['Cur_Scale']

print(float(per_one) * float(quantity))
