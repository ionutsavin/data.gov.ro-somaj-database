import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_params = {
    'dbname': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
}


def connect_to_database():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    return conn, cursor


def get_judet_id(cursor, judet_name):
    select_query = '''
    SELECT id FROM judete WHERE judet = %s;
    '''
    cursor.execute(select_query, (judet_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None


def extract_month_year(filename):
    filename_parts = os.path.splitext(os.path.basename(filename))[0].split('_')
    month = filename_parts[-3]
    year = int(filename_parts[-2])
    return month, year


def map_judet_name(judet_name):
    judet_name = judet_name.strip()

    if "BUC" in judet_name:
        return "BUCURESTI"
    elif "CARA" in judet_name:
        return "CARAS-SEVERIN"
    elif "SATU" in judet_name:
        return "SATU-MARE"
    elif "BISTRITA" in judet_name:
        return "BISTRITA-NASAUD"
    elif "total" in judet_name.lower():
        return "TOTAL"
    return judet_name
