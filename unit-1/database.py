import sqlite3 as lite
import pandas as pd
import csv

def refresh(cur):
    cities = []
    with open('cities.csv') as city_file:
        city_reader = csv.reader(city_file)
        for city in city_reader:
            cities.append(city)

    weather = []
    with open('weather.csv') as weather_file:
        weather_reader = csv.reader(weather_file)
        for weather_report in weather_reader:
            weather.append(weather_report)

    # Drop the tables for a clean slate
    cur.execute('DROP TABLE IF EXISTS cities')
    cur.execute('DROP TABLE IF EXISTS weather')

    # Create new tables to fill
    cur.execute('CREATE TABLE cities (name text, state text)')
    cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text)')

    # Insert the data into tables
    cur.executemany('INSERT INTO cities VALUES(?,?)', cities)
    cur.executemany('INSERT INTO weather VALUES(?,?,?,?)', weather)

    return cur

refresh_db = raw_input('Do you wish to refresh the DB? Y/N ')
month = raw_input('Which month would you like to see where it is warm? ')

con = lite.connect('getting-started.db')

with con:
    cur = con.cursor()

    if refresh_db == 'Y' or refresh_db == 'y':
        refresh(cur)

    # Join the tables together
    query = """
            SELECT * FROM cities
            INNER JOIN weather ON weather.city = cities.name
            """
    cur.execute(query)

    # Put it all in a dataframe
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    # Print the message
    filteredData = df[df['warm_month'] == month]
    print filteredData
    print len(filteredData)
    if len(filteredData) > 0:

        if len(filteredData) == 1:
            print filteredData['name'] + ' is the only warm city in ' + month
        else:
            msg = ''
            for city in filteredData:
                print city
                if len(filteredData) > 0:
                    msg += city['name'] + ', '
                else:
                    msg += 'and ' + city['name']
    else:
        print 'I do not know of any warm cities that time of year.'
