import pandas as pd
import sqlalchemy

# Read Excel
df = pd.read_excel('test.xlsx')

# Connect to MySQL
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/database')

# Import to MySQL
df.to_sql('test_table', engine, if_exists='replace', index=False)