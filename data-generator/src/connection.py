import os
import urllib

#cnx = psycopg2.connect(user="pgadmin", password="{your_password}", host="rpendergraph-adf-prototype.postgres.database.azure.com", port=5432, database="")

db_name = os.environ.get('PGDATABASE', 'moveit')
user = os.environ['PGUSER']
host = os.environ['PGHOST']
password = os.environ['PGPASSWORD']
port = os.environ.get('PGPORT', '5432')
ssl = os.environ.get('SSLMODE', 'require')


def get_url_string():
    safe_pass = urllib.parse.quote_plus(password)
    return f'postgresql://{user}:{safe_pass}@{host}:{port}/{db_name}?sslmode={ssl}'
