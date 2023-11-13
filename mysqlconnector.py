import mysql.connector

def english_to_sql(english_query):
    query_mappings = {
        'select': 'SELECT',
        'from': 'FROM',
        'where': 'WHERE',
        'and': 'AND',
        'or': 'OR',
        'equals': '=',
        'greater than': '>',
        'less than': '<',
        'not equals': '!=',
        'like': 'LIKE',
    }

    words = english_query.split()
    sql_query = []

    for word in words:
        sql_query.append(query_mappings.get(word.lower(), word))

    return ' '.join(sql_query)

def execute_sql_query(sql_query):
    try:
        connection = mysql.connector.connect(
            host="localhost:3306",
            user="root",
            password="your_password",
            database="Hospital_Relation"
        )

        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

        for row in result:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    english_query = input("Enter your English query: ")
    sql_query = english_to_sql(english_query)
    print(f"Generated SQL query: {sql_query}")

    execute_sql_query(sql_query)
