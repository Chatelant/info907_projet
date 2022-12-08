from querries import *
import requests
import csv
import json
import sys
import re


def make_request():
    # Check that the number of argument is 2
    if(len(sys.argv) != 3):
        print("Use 2 parameter: 1 for the source (wikidata or dbpedia), and 1 for the querry (1 to 4)")
        print("For exemple:")
        print("\"python main.py wikidata 1\"")
        exit()

    # Get the parameter
    source = sys.argv[1]
    num_querry = int(sys.argv[2])

    # Change the source depending on the paramter
    if(source == 'dbpedia'):
        url = 'https://dbpedia.org/sparql'
    elif(source == 'wikidata'):
        url = 'https://query.wikidata.org/sparql'
    else:
        print("Error, the source is not valid")
        exit()

    # Get the querry depending on the number
    query = get_querry(source, num_querry)

    if(query == "Error"):
        print("The query is not valid, make sure to read the README file")
        exit()
 
    # Create the csv writer
    f = open('temp.csv', 'w',newline='')
    writer = csv.writer(f)
    # Writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=',', quotechar='',escapechar='')

    if(source=="dbpedia"):
        # If the source is from dbpedia, we can get the csv directly
        r = requests.get(url, params = {'format': 'csv', 'query': query})
        decoded_content = r.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            if(row[0]!=''):
                row[0] = re.sub('[^A-Za-z0-9\s.!?]+', '', row[0])
                if(num_querry >= 2): 
                    row[1] = re.sub('[^A-Za-z0-9\s.!?]+', '', row[1])
                # Write a row to the csv file
                writer.writerow(row)
    else :
        # If it's wikidata, we get the json and transform it to csv
        r = requests.get(url, params = {'format': 'json', 'query': query})
        decoded_content = r.content.decode('utf-8')
        data = json.loads(decoded_content)

        # Write the header
        if(num_querry == 1):
            writer.writerow(['animeLabel'])
        else:
            if(num_querry == 2):
                writer.writerow(['studioLabel', 'animeLabel'])
            else:
                writer.writerow(['studioLabel', 'genreLabel'])
        
        for row in data['results']['bindings']:
            # Depending on the number of the querry, change the attribut name
            if(num_querry == 1):
                row['animeLabel']['value'] = re.sub('[^A-Za-z0-9\s.!?]+', '', row['animeLabel']['value'])
                writer.writerow([row['animeLabel']['value']])
            else:
                array = []
                row['studioLabel']['value'] = re.sub('[^A-Za-z0-9\s.!?]+', '', row['studioLabel']['value'])
                array.append(row['studioLabel']['value'])
                if(num_querry == 2):
                    row['animeLabel']['value'] = re.sub('[^A-Za-z0-9\s.!?]+', '', row['animeLabel']['value'])
                    array.append(row['animeLabel']['value'])
                else:
                    row['genreLabel']['value'] = re.sub('[^A-Za-z0-9\s.!?]+', '', row['genreLabel']['value'])
                    array.append(row['genreLabel']['value'])
                writer.writerow(array)

    # Close the file
    f.close()