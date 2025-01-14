# Flask API

```python
from flask import Flask, send_file
import matplotlib.pyplot as plt
import psycopg2
import pandas as pd
import io

app = Flask(__name__)
plt.switch_backend('Agg')

def get_db_connection():
    return psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_database_host"
    )

@app.route('/temperature_trends')
def temperature_trends():
    # Connect to the database
    connection = get_db_connection()
    query = "SELECT * FROM weather_forecasts;"  # Fetch the data dynamically
    df = pd.read_sql_query(query, connection)
    connection.close()

    # Generate the plot
    fig, ax = plt.subplots()
    ax.plot(df['forecast_period'], df['temperature'], marker='o')
    ax.set(title='Temperature Trends', xlabel='Forecast Period', ylabel='Temperature')
    ax.grid(True)

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return send_file(buf, mimetype='image/png')
```
