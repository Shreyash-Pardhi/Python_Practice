from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc
import pandas as pd

app = Flask(__name__)
CORS(app)  # This will allow all origins

def get_employee_data():
    conn = pyodbc.connect(
        driver="ODBC Driver 13 for SQL Server",
        host="dPSYS125\SQLEXPRESS",
        database="employee",
        trusted_connection="yes"
    )

    query = 'SELECT * FROM dbo.emp'
    df = pd.read_sql_query(sql=query, con=conn)
    conn.close()

    # Convert DataFrame to JSON
    json_data = df.to_dict(orient='records')  # 'records' gives a list of dictionaries
    return json_data

@app.route('/employees', methods=['GET'])
def employees():
    data = get_employee_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)