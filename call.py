from database_connector import get_database_connection, run_query
from API_request import ask_chatdb 
from detect import detect_database #imports from other script to detect database


#in this script I am pulling it all together and having the user ask a question about the databases. 
question = input("Ask your database a question: ")

db_name = detect_database(question) 
print(f" Using database: {db_name}")


database_connection = get_database_connection(db_name)


sql_query = ask_chatdb(question)
print("\nGPT-generated SQL:\n", sql_query)


column_names, results = run_query(sql_query, database_connection)

print("\n Query Results:")
if results:
    print(" | ".join(column_names))
    for row in results:
        print(" | ".join(str(val) for val in row))
else:
    print("No results or an error occurred.")