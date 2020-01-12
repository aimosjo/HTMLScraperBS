# use CSV file to write to new database
# use pandas to create dataframe from csv to push to the sql
import pandas as pd
import sqlite3

# user needs to pass database name, path, and csvfile to the function

def csvToDB(dbname, csvfile, path=None):

	conn = sqlite3.connect("{}.db".format(dbname))

	df = pd.read_csv(csvfile + ".csv")
	
	df.to_sql(csvfile, conn, if_exists='append', index=False)

	conn.close()
