import csv
from collections import defaultdict

AviationData = [x for x in open("AviationData.txt","r")]

aviation_list = [x.split("|") for x in AviationData]
lax_code = [i for i in aviation_list if i=="LAX94LA336"]
#print(lax_code)

#implementing hash table
lax = [x for x in open("AviationData.txt","r") if "LAX94LA336" in x]
#print(lax)
#Creating Dictionaries 

headers = AviationData[0].split(" | ")
aviation_dict_list = [dict(zip(headers, row.split(" | "))) for row in AviationData[1:]]
lax_dict = [row for row in aviation_dict_list if "LAX94LA336" in row.values()]
print(lax_dict)

#Accidents by US State

state_accidents = defaultdict(int)
for row in AviationData:
    if row['Country'] == 'United States' and ',' in row['Location']:
        state = row['Location'].split(',')[1]
        state_accidents[state] +=1
state_accidents = dict(state_accidents)
most_accident_state = max(state_accidents.items(),
                          key=operator.itemgetter(1))[0]
print(state_accidents)
print(most_accident_state)

monthly_injuries = defaultdict(lambda: [0,0])
for row in aviation_dict_list:
    month = row['Event Date'].split("/")[0]
    for ix, field in enumerate(['Total Fatal Injuries', 'Total Serious Injuries']):
        if row[field] != '':
            monthly_injuries[month][ix] += int(row[field])
        else:
            monthly_injuries[month][ix] += 0

print(monthly_injuries)






