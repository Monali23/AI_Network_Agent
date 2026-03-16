import mysql.connector

def run_query(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="network_db"
    )

    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results