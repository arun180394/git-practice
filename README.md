# git-practice

## 1. Question 1: Please write a Python script that:
- Written python script that reads the url and generated the o/p in desired format. Please run the [first point script](https://github.com/arun180394/git-practice/blob/master/first_point.py).

## 2. Reads the JSON located at [URL](https://data.cityofnewyork.us/api/views/25th-nujf/rows.json)
- Written the script that reads the url and do the following operations:

### 3. Maps the 'name' from each field in "columns", available at JSON_ROOT['meta']['view']['columns'], to each list inside JSON_ROOT['data']

- In that script it takes the all the `name` field values present in the JSON_ROOT['meta']['view']['columns'], and adding all these names to the JSON_ROOT['data'] each list.

### 4. Outputs a JSON file containing only data for the following fields: ["Child's First Name", "Gender", "Ethnicity", "Year of Birth", "Rank", "Count"] 

- Filtered the name field is having above values data from the columns dict and generated the json and csv output files.

### 5. Filters the aforementioned data to only the years 2012-2014, then groups by "Child's First Name" and "Ethnicity", and finally provides the sum of "Count" for each combination.
- Gone through the whole JSON data in that link, There is no years data at all. Can you please explain this with one example, How to map this data. 
