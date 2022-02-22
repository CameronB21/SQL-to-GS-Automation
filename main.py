# import modules and files
import pandas as pd
import arrow
import time
import pygsheets
import json
from data import query_helper

# set size of dataframe
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# google sheets class
class SaveGS:
    def __init__(self, doc_name: str):
        gc = pygsheets.authorize(
            service_file='/YOUR PATH/client-secret.json')

        self.sheet = gc.open(doc_name)

# clear existing data on google sheet
    def clear_update_workbook(self, df, tab_name, start_cell):
        wks = self.sheet.worksheet('title', f'{tab_name}')
        wks.clear(start=f'{start_cell}')
        wks.set_dataframe(df, f'{start_cell}', copy_head=False)
        wks.update_value('S3', 'Latest Auto Update:')
        wks.update_value('S4', f'{arrow.now().date()}')

# clear two columns of data that aren't needed. This is only for this the HVO
    def finishing_touches(self, tab_name):
        wks = self.sheet.worksheet('title', f'{tab_name}')
        wks.clear(start='J1', end='K1000')


def gs_automation():
    start_time = time.time() # needed for timestamp
    users = list()
    with open('/YOUR PATH/Users/Jen_H.json') as f:
        users.append(json.load(f)) # reference SQL query. Can be expanded for many SQL queries


    for user in users: # runs query_helper from data file for each user.
        for doc, values in user.items():
            cell_start = values['cell_start']
            sheet = SaveGS(doc)
            for tab, query in values['tabs'].items():
                if ';' in query:
                    queries = query.split(';')
                    initial_query = query_helper(queries[0])
                    second_query = query_helper(queries[1])
                    df = initial_query.append(second_query).reset_index(drop=True)
                    sheet.clear_update_workbook(df, tab, cell_start)
                else:
                    df = query_helper(query)
                    sheet.clear_update_workbook(df, tab, cell_start)

                    # This line is only for HVO, comment out or remove for your own
                    sheet.finishing_touches(tab)

                print(f'{doc}: done with {tab}')


    done_time = (time.time() - start_time) / 60 #time stamp
    print(f"\nDone in --- {round(done_time, 2)} minutes ---")


if __name__ == '__main__':
    gs_automation()
