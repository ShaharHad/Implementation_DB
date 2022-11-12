import sqlite3
db = 'media_store.db'

def read_file(file):
    f = open(file, 'r')
    file = f.read()
    f.close()
    return file

def get_data_from_db(query):
    conn = sqlite3.connect(db)
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def customers_count():
    query = read_file('ex1.sql')
    rows = get_data_from_db(query)
    return rows[0][0]

def most_productive_artist():
    query = read_file('ex2.sql')
    rows = get_data_from_db(query)
    return rows[0][0]

def get_income_for_2010():
    query = read_file('ex3.sql')
    rows = get_data_from_db(query)
    return rows[0][0]

def customer_that_likes_classical():
    query = read_file('ex4.sql')
    rows = get_data_from_db(query)
    return rows[0][0] + " " + rows[0][1]

def most_successful_artist():
    query = read_file('ex5.sql')
    rows = get_data_from_db(query)
    return {"Artist": rows[0][0], "Album": str(rows[0][1])}

def who_is_the_boss():
    query = read_file('ex6.sql')
    rows = get_data_from_db(query)
    return rows[0][0] + " " + rows[0][1]

def costumers_that_like_quality():
    query = read_file('ex7.sql')
    rows = get_data_from_db(query)
    return rows[0][0]



def get_income_for(year):
    query = read_file('ex2.2.sql')
    conn = sqlite3.connect(db)
    cursor = conn.execute(query, (year,))
    rows = cursor.fetchall()
    conn.close()
    return rows[0][0]

# if __name__ == "__main__":
    # print(type(customers_count()))
    # print(type(most_productive_artist()))
    # print(type(get_income_for_2010()))
    # print(type(customer_that_like_classical()))
    # print(type(most_successful_artist()))
    # print(type(who_is_the_boss()))
    # print(f"costumers_that_likes_quality type: {type(costumers_that_likes_quality())}")

    # print(f"customers_count: {customers_count()}")
    # print(f"most_productive_artist: {most_productive_artist()}")
    # print(f"get_income_for_2010: {get_income_for_2010()}")
    # print(f"customer_that_like_classical: {customer_that_like_classical()}")
    # print(f"most_successful_artist: {most_successful_artist()}")
    # print(f"who_is_the_boss: {who_is_the_boss()}")
    # print(f"costumers_that_likes_quality: {costumers_that_likes_quality()}")

    # year = '2013'
    # print(f"get_income_for_{year}: {get_income_for(year)}")
    # print(type(get_income_for(year)))

