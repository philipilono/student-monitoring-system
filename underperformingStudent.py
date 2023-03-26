import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def under_perform():
    '''Finds underperforming students and their grades'''
    
    #establishes a connection to talk to database
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    
    sqlite_read_record_query = """ SELECT SumTest.research_id,
                                Formative_Mock_Test.Grade AS 'Mock Test',
                                Formative_Test_1.Grade AS 'Test 1',
                                Formative_Test_2.Grade AS 'Test 2',
                                Formative_Test_3.Grade AS 'Test 3',
                                Formative_Test_4.Grade AS 'Test 4',
                                SumTest.Grade AS 'Sum Test'
                                FROM SumTest
                                 LEFT JOIN Formative_Mock_Test ON SumTest.research_id = Formative_Mock_Test.research_id
                                 LEFT JOIN Formative_Test_1 ON Formative_Mock_Test.research_id = Formative_Test_1.research_id
                                 LEFT JOIN Formative_Test_2 ON Formative_Test_1.research_id = Formative_Test_2.research_id
                                 LEFT JOIN Formative_Test_3 ON Formative_Test_2.research_id = Formative_Test_3.research_id
                                 LEFT JOIN Formative_Test_4 ON Formative_Test_3.research_id = Formative_Test_4.research_id
                                 WHERE ( Formative_Mock_Test.Grade <50 OR Formative_Mock_Test.Grade IS NULL)
                                 AND (Formative_Test_1.Grade < 50 OR Formative_Test_1.Grade IS NULL)
                                 AND (Formative_Test_2.Grade < 50 OR Formative_Test_2.Grade IS NULL)
                                 AND (Formative_Test_3.Grade < 50 OR Formative_Test_3.Grade IS NULL)
                                 AND (Formative_Test_4.Grade < 50 OR Formative_Test_4.Grade IS NULL)
                                 AND (SumTest.Grade < 50 OR SumTest.Grade IS NULL)
                                    """
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    #ends cpnnection
    sqliteConnection.close()
    global df_under
    df_under = []
    #only allows students that didn't leave out 3 tests
    for i in range(len(df)):
        df_na = df.iloc[i].isna().sum()
        if df_na <= 3:
            df_under.append(df.iloc[i])

    df_under = pd.DataFrame(df_under)
    #sorts by sum test grade
    df_under = df_under.sort_values('Sum Test')
    #turns float to an integer
    df_under['research_id'] = df_under['research_id'].astype(int)
    df_under = pd.DataFrame(df_under)
    
    return df_under
    

def plot_under_perform():
    #each y represents each row of teh dataframe
    y1 = (df_under.iloc[0])[1:]
    y2 = (df_under.iloc[1])[1:]
    y3 = (df_under.iloc[2])[1:]
    x = df_under.columns[1:]

    #3 subplots generated
    fig, axs = plt.subplots(2,2, figsize=(8,6))
    axs[0,0].plot(x,y1)
    axs[1,0].plot(x, y2)
    axs[0,1].plot(x, y3)                      
    

    plt.show()
    
