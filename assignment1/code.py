import sqlite3

def read_file(file):
    f = open(file, 'r')
    file = f.read()
    f.close()
    return file

def get_data_from_db(query):
    db = 'media_store.db'
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

def customer_that_like_classical():
    query = read_file('ex4.sql')
    rows = get_data_from_db(query)
    return rows[0][0] + " " + rows[0][1]

def most_successful_artist():
    query = read_file('ex5.sql')
    rows = get_data_from_db(query)
    return {"Name": rows[0][0], "Album": str(rows[0][1])}

def who_is_the_boss():
    query = read_file('ex6.sql')
    rows = get_data_from_db(query)
    return rows[0][0] + " " + rows[0][1]

def costumers_that_likes_quality():
    pass




if __name__ == "__main__":
    print(type(customers_count()))
    print(type(most_productive_artist()))
    print(type(get_income_for_2010()))
    print(type(customer_that_like_classical()))
    print(type(most_successful_artist()))
    print(type(who_is_the_boss()))
    print(type(costumers_that_likes_quality()))


    # print(customers_count())
    # print(most_productive_artist())
    # print(get_income_for_2010())
    # print(customer_that_like_classical())
    # print(most_successful_artist())
    # print(who_is_the_boss())
    # print(costumers_that_likes_quality())
