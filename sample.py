import sqlite3
world_db_path = r'C:\Users\suryavamsib\Desktop\SutiTexTrak\SutiTexTrak Master Build\world.sqlite3'
# 2. Function to get the country based on currency code
def get_country_by_currency(currency_code):
    global world_db_path
    conn = sqlite3.connect(world_db_path)  # Replace with your actual database path
    cursor = conn.cursor()
    try:
        query = '''
        SELECT name 
        FROM countries 
        WHERE currency = ?
        LIMIT 1
        '''
        cursor.execute(query, (currency_code,))
        results = cursor.fetchall()
        return results
    finally:
        conn.close()  # Ensuring the connection is closed


def get_country_and_currency_by_province(province_name):
    conn = sqlite3.connect(world_db_path)  # Replace with your actual database path
    cursor = conn.cursor()
    try:
        query = '''
        SELECT countries.name, countries.currency 
        FROM countries 
        LEFT JOIN states ON states.country_id = countries.id 
        WHERE states.name LIKE ?
        '''
        cursor.execute(query, ('%' + province_name + '%',))
        results = cursor.fetchall()
        if results:
            country = results[0][0]
            currency = results[0][1]
            return country, currency
        else:
            return '', ''
    finally:
        conn.close()  # Ensuring the connection is closed


# 1. Function to get the country and currency based on city name
def get_country_and_currency_by_city(city_name):
    conn = sqlite3.connect(world_db_path)  # Replace with your actual database path
    cursor = conn.cursor()
    try:
        query = '''
        SELECT countries.name, countries.currency 
        FROM countries 
        LEFT JOIN cities ON cities.country_id = countries.id 
        WHERE cities.name = ?
        '''
        # cursor.execute(query, ('%' + city_name + '%',))
        cursor.execute(query, (city_name,))

        results = cursor.fetchall()
        if results and len(results) == 1:
            country = results[0][0]
            currency = results[0][1]
            return country, currency
        else:
            return '', ''
    finally:
        conn.close()  # Ensuring the connection is closed


print(get_country_and_currency_by_city('Townsville'))