from .models import Items
import pandas

def fetch_data():
    countries = [
        'GPRC_ARG',
        'GPRC_AUS',
        'GPRC_BEL',
        'GPRC_BRA',
        'GPRC_CAN',
        'GPRC_CHE',
        'GPRC_CHL',
        'GPRC_CHN',
        'GPRC_COL',
        'GPRC_DEU',
        'GPRC_DNK',
        'GPRC_EGY',
        'GPRC_ESP',
        'GPRC_FIN',
        'GPRC_FRA',
        'GPRC_GBR',
        'GPRC_HKG',
        'GPRC_HUN',
        'GPRC_IDN',
        'GPRC_IND',
        'GPRC_ISR',
        'GPRC_ITA',
        'GPRC_JPN',
        'GPRC_KOR',
        'GPRC_MEX',
        'GPRC_MYS',
        'GPRC_NLD',
        'GPRC_NOR',
        'GPRC_PER',
        'GPRC_PHL',
        'GPRC_POL',
        'GPRC_PRT',
        'GPRC_RUS',
        'GPRC_SAU',
        'GPRC_SWE',
        'GPRC_THA',
        'GPRC_TUN',
        'GPRC_TUR',
        'GPRC_TWN',
        'GPRC_UKR',
        'GPRC_USA',
        'GPRC_VEN',
        'GPRC_ZAF',
    ]
    # data = Items.objects.all()
    # data.delete()

    for country in countries:
        dates = pandas.read_excel('https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls', usecols=['month'])
        countries_risk_index = pandas.read_excel('https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls', usecols=[country])

        dates_dict = dates.to_dict()
        risk_index_list = []

        for key, value in countries_risk_index.items():
            for key1, value1 in value.items():
                risk_index_list.append(round(value1, 3))

        for key, value in dates_dict.items():
            for key1, value1 in value.items():
                date = value1.strftime('%Y-%m')
                country_id = country[5:8]
                risk_index = risk_index_list.pop(0)

                if int(date[0:4]) > 1988:
                    if not Items.objects.filter(date=date, country_id=country_id):
                        data = Items(date=date, country_id=country_id, risk_index=risk_index)
                        data.save()
    
                    
                    