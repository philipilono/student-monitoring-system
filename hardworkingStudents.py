import pandas as pd
import sqlite3


def hard_work():
        #establishes connection to talk to database
        sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
        #selects student id and grade for summative test where the grade is below 60
        sqlite_read_record_query = """ SELECT research_id, Grade
                                       FROM SumTest
                                       WHERE Grade > 60"""
        global df2
        df2=pd.read_sql(sqlite_read_record_query,sqliteConnection)
        #ends connection
        sqliteConnection.close()

        #reads StudentRate csv file from file path 
        dfStudentRate = pd.read_csv('DataFiles\StudentRate.csv')
        dfRate = dfStudentRate.copy()
        #cleans column names to display better
        dfRate.rename(columns = {'What level programming knowledge do you have?' :
                                 'Rates',
                                 'research id': 'research_id'}, inplace = True)

        #filters to find out students with not much coding experience
        df = dfRate[(dfRate['Rates'] == 'Beginner') | (dfRate['Rates'] == 'Below beginner') ]
        #only care about student id and rates (prior coding level)
        df = df[['research_id', 'Rates']]

        #inner joins both data frames based on student id
        df_hardworkers = pd.merge(df, df2, on = 'research_id', how ='inner')
        #sorts dataframe by Grade in descending order
        df_hardworkers = df_hardworkers.sort_values('Grade', ascending = False)

        return df_hardworkers
