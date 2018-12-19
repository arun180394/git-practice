import json
import csv
import requests

def json_to_csv(json_file_path, outfile_path):
    """Convert a file containing a list of flat JSON objects to a csv.
    What's a DictWriter, you say? Never heard of it!
    """
    with open(json_file_path) as f:
        data = json.load(f)
    with open(outfile_path, 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())


## First point Reads the JSON located at https://data.cityofnewyork.us/api/views/25th-nujf/rows.json
url = 'https://data.cityofnewyork.us/api/views/25th-nujf/rows.json'
data = requests.get(url).json()

## 2. Maps the 'name' from each field in "columns", available at JSON_ROOT['meta']['view']['columns'], to each list inside JSON_ROOT['data']. (e.g. the name of the first field listed in "columns" is the name of the first item in each list in "data")
names = [i['name'] for i in data['meta']['view']['columns']]

list_data = data['data']
for i in list_data:
    for j in names:
        i.insert(0, j)

# Saving the json file:
fp = open('second_point.json', 'w')
fp.write(json.dumps(list_data))
fp.close()


## 3. Outputs a JSON file containing only data for the following fields: ["Child's First Name", "Gender", "Ethnicity", "Year of Birth", "Rank", "Count"] 
final_data = []
default_list_data = ["Child's First Name", "Gender", "Ethnicity", "Year of Birth", "Rank", "Count"]
for i in columns_data:
    if i['name'] in default_list_data:
        final_data.append(i)

# Saving the json file:
fp = open('third_point.json', 'w')
fp.write(json.dumps(final_data))
fp.close()

json_to_csv('third_point.json', 'third_point.csv')

## 4. Filters the aforementioned data to only the years 2012-2014, then groups by "Child's First Name" and "Ethnicity", and finally provides the sum of "Count" for each combination.
## I didn't understand how to map this data, can you please explain me with one example.

## 5. Writes the resulting data to both JSON and CSV.
### Already converted the json to csv in possible places.
