from querries import *
import requests
import csv
import json
import sys

# Check that the number of argument is 2
if(len(sys.argv) != 3):
    print("Use 2 parameter: 1 for the source (wikidata or dbpedia), and 1 for the querry (1 to 3)")
    print("For exemple:")
    print("\"python main.py wikidata 1\"")
    exit()

# Load the file
source = sys.argv[1]
num_querry = int(sys.argv[2])

if(source == 'dbpedia'):
    url = 'https://dbpedia.org/sparql'
elif(source == 'wikidata'):
    url = 'https://query.wikidata.org/sparql'
else:
    print("Error, the source is not valid")
    exit()

query = get_querry(source, num_querry)

# print(query)

f = open('temp.csv', 'w')
# create the csv writer
writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=',', quotechar='',escapechar='')
# writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=',', quotechar='',escapechar='')

if(source=="dbpedia"):
    r = requests.get(url, params = {'format': 'csv', 'query': query})
    decoded_content = r.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        if(row[0]!=''):
            # row[0] = row[0].replace(".", '')
            row[0] = row[0].replace(",", '')
            # row[1] = row[1].replace(".", '')
            row[1] = row[1].replace(",", '')
            # write a row to the csv file
            writer.writerow(row)
else :
    r = requests.get(url, params = {'format': 'json', 'query': query})
    decoded_content = r.content.decode('utf-8')
    print(decoded_content)
    data = json.loads(decoded_content)

    for row in data['results']['bindings']:
        if(num_querry == 1):
            print(row['animeLabel']['value'])
            writer.writerow([row['animeLabel']['value']])
        else:
            array = []
            array.append(row['studioLabel']['value'].replace(",", ''))
            if(num_querry == 2):
                array.append(row['animeLabel']['value'].replace(",", ''))
            else:
                array.append(row['genreLabel']['value'].replace(",", ''))
            writer.writerow(array)

# close the file
f.close()
