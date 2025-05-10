import streamlit as st
import pandas as pd
import mysql.connector
from database_connector import get_database_connection, run_query
from API_request import ask_chatdb

# this function helps detect which database ChatGPT needs to use based on some keywords

def detect_database(question):
    q = question.lower()

    if any(word in q for word in ["netflix", "watch", "show", "movie", "series", "subscription", "plan", "genre", "streaming"]):
        return "entertainment"
    elif any(word in q for word in ["gym", "fitness", "workout", "trainer", "membership", "visits", "exercise", "group class"]):
        return "GYM"
    elif any(word in q for word in ["shopping", "purchase", "order", "cart", "product", "item", "customer", "store", "receipt"]):
        return "shopping"
    else:
        return "entertainment"

#  App Title
st.set_page_config(page_title="ChatDB", page_icon="💬")
st.title(" ChatDB Chatbot")

#  Chat-like input
st.markdown("### Ask your database a question:")
question = st.chat_input(placeholder="E.g. How many users like horror movies?")

if question:
    st.chat_message("user").write(question)

    #  Detect database based on the question
    db_name = detect_database(question)
    st.chat_message("assistant").write(f"Using database: **{db_name}**")

    # Generate SQL
    sql_query = ask_chatdb(question)
    st.chat_message("assistant").write("Generated SQL:")
    st.code(sql_query, language="sql")

    #  Connect to DB and run query
    try:
        conn = get_database_connection(db_name)
        column_names, results = run_query(sql_query, conn)

        if results:
            df = pd.DataFrame(results, columns=column_names)
            st.chat_message("assistant").write("Query Results:")
            st.dataframe(df)

            # Optional CSV export
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results as CSV", csv, "results.csv", "text/csv")
        else:
            st.chat_message("assistant").write("No results found or an error occurred.")

    except Exception as e:
        st.chat_message("assistant").write(f"Database error: {e}")

