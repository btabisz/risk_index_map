from .models import RiskIndexItems
import csv

import pandas

countries = ['GPRC_ARG',
             'GPRC_AUS', 'GPRC_BEL', 'GPRC_BRA', 'GPRC_CAN', 'GPRC_CHE', 'GPRC_CHL', 'GPRC_CHN', 'GPRC_COL',
             'GPRC_DEU', 'GPRC_DNK', 'GPRC_EGY', 'GPRC_ESP', 'GPRC_FIN', 'GPRC_FRA', 'GPRC_GBR', 'GPRC_HKG', 'GPRC_HUN',
            'GPRC_IDN', 'GPRC_IND', 'GPRC_ISR', 'GPRC_ITA', 'GPRC_JPN', 'GPRC_KOR', 'GPRC_MEX', 'GPRC_MYS', 'GPRC_NLD',
             'GPRC_NOR', 'GPRC_PER', 'GPRC_PHL', 'GPRC_POL', 'GPRC_PRT', 'GPRC_RUS', 'GPRC_SAU', 'GPRC_SWE', 'GPRC_THA',
            'GPRC_TUN', 'GPRC_TUR', 'GPRC_TWN', 'GPRC_UKR', 'GPRC_USA', 'GPRC_VEN', 'GPRC_ZAF'
             ]


def add_risk_index_data():
    data = RiskIndexItems.objects.all()
    data.delete()
    for country in countries:
        data = pandas.read_excel('https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls', usecols=['month', country])
        data.to_csv("risk_data.csv")
        filter_data()
        add_to_db(country)


def filter_data():
    counter = 0
    with open('risk_data.csv', 'rt') as raw_data, open('filtered_risk_data.csv', 'wt',
                                                         newline='') as filtered:
        writer = csv.writer(filtered)
        for row in csv.reader(raw_data):
            if counter == 0:
                counter += 1
            else:
                if int(row[1][0:4]) >= 1988:
                    writer.writerow(row[1:3])


def add_to_db(country):
    counter = 0
    last_month_index = 0
    country = country[5:8]
    with open('filtered_risk_data.csv', 'r') as filtered:
        for row in csv.reader(filtered):
            if counter == 0:
                last_month_index = float(row[1])
                counter += 1
                continue
            else:
                date = row[0][0:7]
                risk_index = round(float(row[1]), 3)
                delta = round(abs(risk_index - last_month_index), 3)
                if risk_index == 0:
                    change = -100
                    last_month_index = risk_index
                elif last_month_index == 0:
                    change = 100
                    last_month_index = risk_index
                else:
                    change = round((((float(row[1])) / (float(last_month_index))) - 1) * 100, 2)
                    last_month_index = risk_index

                # print(f'{date} : {risk_index}, {delta}, {change}%')
                if not RiskIndexItems.objects.filter(date=date, country_id=country):
                    data = RiskIndexItems(date=date, country_id=country, risk_index=risk_index, risk_change=change, risk_delta=delta)
                    data.save()



        # dates = pandas.read_excel('https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls', usecols=['month'])
        # countries_risk_index = pandas.read_excel('https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls', usecols=[country])
        #
        # dates_dict = dates.to_dict()
        # risk_index_list = []
        #
        # for key, value in countries_risk_index.items():
        #     for key1, value1 in value.items():
        #         risk_index_list.append(round(value1, 3))
        #
        # for key, value in dates_dict.items():
        #     for key1, value1 in value.items():
        #         date = value1.strftime('%Y-%m')
        #         country_id = country[5:8]
        #         risk_index = risk_index_list.pop(0)
        #
        #         if int(date[0:4]) > 1988:
        #             if not Items.objects.filter(date=date, country_id=country_id):
        #                 data = Items(date=date, country_id=country_id, risk_index=risk_index)
        #                 data.save()
        #

# add_risk_index_data()