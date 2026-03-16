from tools.db_tool import run_query

def analyze_network():
    query = "SELECT * FROM alarms LIMIT 10"
    data = run_query(query)
    return data