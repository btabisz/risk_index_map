import csv
import pandas_datareader
from pandas_datareader.stooq import StooqDailyReader
from base.models import RiskIndexItems
import yfinance as yf

# blob:https://www.investing.com/04943203-6001-42f0-b0da-227160b91ffb



stooq_markets = {
    "POL": ["POL", "WIG20.PL", "WIG20"],
    "USA": ["USA", "^DJI", "DJI"],
    "ARG": ["ARG", "^MRV", "MRV"],
    "HUN": ["HUN", "^BUX", "BUX"],
    "NLD": ["NLD", "^AEX", "AEX"],
    "PRT": ["PRT", "^PSI20", "PSI20"],
    "ESP": ["ESP", "^IBEX", "IBEX"],
    "TUR": ["TUR", "^XU100", "XU100"],
    "HKG": ["HKG", "^HSI", "HSI"],
    "CHL": ["CHL", "^IPSA", "IPSA"],
    "NOR": ["NOR", "^OSEAX", "OSEAX"],
    "RUS": ["RUS", "^RTS", "RTS"],
    "SWE": ["SWE", "^OMXS", "OMXS"],
    "UKR": ["UKR", "^UX", "UX"],
    "ITA": ["ITA", "^FMIB", "FMIB"],
    "CHN": ["CHN", "^SHC", "SHC"],
    "KOR": ["KOR", "^KOSPI", "KOSPI"],
    "PHL": ["PHL", "^PSEI", "PSEI"],
    "TWN": ["TWN", "^TWSE", "TWSE"],
    "IND": ["IND", "^SNX", "SNX"],
    }

yahoo_markets = {
    "CAN": ["CAN", "^GSPTSE", "GSPTSE"],
    "MEX": ["MEX", "^MXX", "MXX"],
    "BRA": ["BRA", "^BVSP", "BVSP"],
    "GBR": ["GBR", "^FTSE", "FTSE"],
    "BEL": ["BEL", "^BFX", "BFX"],
    "FRA": ["FRA", "^FCHI", "FCHI"],
    "DEU": ["DEU", "^GDAXI", "GDAXI"],
    "CHE": ["CHE", "^SSMI", "SSMI"],
    "ISR": ["ISR", "TA35.TA", "TA-35"],
    "AUS": ["AUS", "^AXJO", "AXJO"],
    "JPN": ["JPN", "^N225", "N225"],
    "IDN": ["IDN", "^JKSE", "JKSE"],
    # "SAU": ["SAU", "^TASI", "TASI"],
    }


def stooq_add_to_db():
    for country in stooq_markets.values():
        country_id = country[0]
        market_index = country[1]
        market_index_name = country[2]
        stooq_fetch_data(market_index)
        filter_data()
        count_change_monthly(country_id, market_index_name)


def yahoo_add_to_db():
    for country in yahoo_markets.values():
        country_id = country[0]
        market_index = country[1]
        market_index_name = country[2]
        yahoo_fetch_data(market_index)
        filter_data()
        count_change_monthly(country_id, market_index_name)


def yahoo_fetch_data(market_index):
    data = yf.download(market_index, start="1988-12-01", end="2023-04-03")
    data.drop(['Open', 'High', 'Low', 'Volume', 'Adj Close'], axis=1, inplace=True)
    data = data[::-1]
    data.to_csv("market_data.csv", index=True)


def stooq_fetch_data(market_index):
    data = pandas_datareader.stooq.StooqDailyReader(symbols=market_index, start='12/1988').read()
    try:
        data.drop(['Open', 'High', 'Low', 'Volume'], axis=1, inplace=True)
    except KeyError:
        data.drop(['Open', 'High', 'Low'], axis=1, inplace=True)
    data.to_csv("market_data.csv", index=True)


def filter_data():
    counter = 0
    month = 0
    with open('market_data.csv', 'rt') as raw_data, open('filtered_market_data.csv', 'wt', newline='') as filtered:
        writer = csv.writer(filtered)
        for row in csv.reader(raw_data):
            if counter == 0:
                month = row[0][5:7]
                counter += 1
            if row[0][5:7] != month:
                writer.writerow(row)
                month = row[0][5:7]


def count_change_monthly(country, market_index_name):
    counter = 0
    close = 0
    with open('filtered_market_data.csv', 'r') as filtered:
        for row in reversed(list(csv.reader(filtered))):
            if counter == 0:
                close = row[1]
                counter += 1
                continue
            else:
                date = row[0][0:7]
                change = round(((float(row[1]) / float(close)) - 1)*100, 2)
                close = row[1]
                # print(f'{date} : {change}, {market_index_name}')
                RiskIndexItems.objects.filter(country_id=country, date=date).update(market_change=change, market_index_name=market_index_name)

#
# add_to_db()
# stooq_add_to_db()
# yahoo_add_to_db()

