import mysql.connector

#created functions to one connect to mysql. Had to learn how to use mysqlconnector 
#Had to create a function to run a mysql query each time so we didnt have to repat our code over and over. 

def get_database_connection(db_name):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mars2422",
        database=db_name, 
        auth_plugin='mysql_native_password'
    )

def run_query(sql_query, database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute(sql_query)

        # If it's a SELECT query, fetch results
        if sql_query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
        else:
            database_connection.commit()
            results = [("✅ Query executed successfully!",)]
            column_names = ["Message"]

        cursor.close()
        database_connection.close()

        return column_names, results

    except mysql.connector.Error as err:
        column_names = ["Error"]
        results = [(f" MySQL Error: {err}",)]
        return column_names, results