import json

def get_country_city_code(country, city, docu):
    country_code = 0
    city_code = 0
    doc_code = 0

    with open('countries.json') as json_file:
        data = json.load(json_file)
        try:
            country_code = data[country]
        except KeyError:
            country_code = 101

    with open('cities.json') as cities:
        data = json.load(cities)
        try:
            city_code = data[country][city]
        except KeyError:
            city_code = 12

    with open('doc_type.json') as doc_type:
        data = json.load(doc_type)
        try:
            doc_code = data[docu]
        except KeyError:
            doc_code = 1

    return country_code, city_code, doc_code

    
