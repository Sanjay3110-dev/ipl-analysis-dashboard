import pandas as pd
import sqlite3

matches = pd.read_csv('/Users/apple/Downloads/archive-2/matches_clean.csv')
deliveries = pd.read_csv('/Users/apple/Downloads/archive-2/deliveries_clean.csv')

conn = sqlite3.connect('ipl.db')

matches.to_sql('matches', conn, if_exists='replace', index=False)
deliveries.to_sql('deliveries', conn, if_exists='replace', index=False)

print("Tables created:")

cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")

for x in cursor.fetchall():
    print('-', x[0])
    
conn.close()
print("\nDatabase ready: ipl.db")