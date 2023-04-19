import json
import pandas as pd
from base.models import CountryRiskPremiumItems
countries = ['2000.xls',
             '2001.xls', '2002.xls', '2003.xls', '2004.xls', '2005.xls', '2006.xls', '2007.xls', '2008.xls',
             '2009.xls', '2010.xls', '2011.xls', '2012.xls', '2013.xls', '2014.xls', '2015.xls', '2016.xls', '2017.xls',
             '2018.xls', '2019.xls', '2020.xls', '2021.xls']
countries_not_on_map = ['Alderney', 'Andorra', 'Bahamas - Off Shore Banking Center', 'Bahrain', 'Bahrain - Off Shore '
                        'Banking Center', 'Barbados', 'Cayman Islands', 'Cayman Islands - Off Shore Banking Center',
                        'Fiji Islands', 'Eurozone', 'Gibraltar', 'Guernsey', 'Hong Kong', 'Isle of Man', 'Jersey',
                        'Liechtenstein', 'Macau', 'Mauritius', 'Monaco', 'Bahrain-Off Shore Banking',
                        'Panama - Off Shore Banking Center', 'San Marino', 'Sark', 'Singapore', 'Jersey (States of)',
                        'Macao', 'Maldives', 'Montserrat', 'Ras Al Khaimah (Emirate of)','Turks and Caicos Islands',
                        'St. Vincent & the Grenadines', 'Cayman islands', 'Cayman Islands Off Shore Banking', 'Costa',
                        'Bahamas-Offshore', 'St. Maarten', 'Panama-Offshore Banks', 'Sharjah', 'Guernsey (States of)',
                        'Cook Islands', "Côte d'Ivoire", 'Curacao', 'Panama Off-shore Banking',
                        'Bahamas-Off Shore Banking Center', 'Bahamas-Off Shore Banking', 'Cape Verde', 'Aruba',
                        'Andorra (Principality of)', 'Alderny', 'Abu Dhabi', 'Ras Al Kaminah', 'St. Vincent',
                        'Bahrain-Offshore']


def add_country_risk_premium_data():
    with open('./countries_id.json', 'r') as countries_id:
        countries_id_dict = json.load(countries_id)
        for country in countries:
            year = country[0:4]
            data = pd.read_excel(f'./CRP_files/{country}', "Country premiums")
            for index, row in data.iterrows():
                if row["Country"] in countries_not_on_map:
                    continue
                if row["Country"] in countries_id_dict.keys():
                    country_id = countries_id_dict[row["Country"]]
                    country_risk_premium = round(float(row['Country Risk Premium'])*100, 2)
                    if not CountryRiskPremiumItems.objects.filter(year=year, country_id=country):
                        data = CountryRiskPremiumItems(year=year, country_id=country_id, country_risk_premium=country_risk_premium)
                        data.save()
                    # print(country, countries_id_dict[row["Country"]], round(float(row['Country Risk Premium'])*100, 2))
                else:
                    print(country, row["Country"], '   Duppppppppsssssssooooooonnnnnn')




# def add_country_risk_premium_db():
#     world_countries_id = {}
#     with open('./../world_map.json', 'r') as data, open('./../countries_id.json', 'w') as json_data:
#         for country in json.load(data)['objects']['countries1']['geometries']:
#             world_countries_id[country['properties']['name']] = country['id']
#         json.dump(world_countries_id, json_data)
#
#
# add_country_risk_premium_db()

# "https://raw.githubusercontent.com/lotusms/world-map-data/main/world.json"

