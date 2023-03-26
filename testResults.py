import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 


def read_marks(student_id):
    '''Reads overall Grades for each assessment for an individual student id  '''
    try:
        #establishes a connection to talk to database
        sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
        #selects grade from each test table
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
                                  
                                """
        #stores in to a new dataframe
        df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
        #ends the connection
        sqliteConnection.close()
        global dfGrade
        #only stores the grade associated to the student id
        dfGrade = df[df['research_id'] == student_id]
        global results
        results = (dfGrade.iloc[0])[1:]
        marks = pd.DataFrame(results)
        marks.columns = ['Grade']
        return marks
    except:
        print("Enter an integer in the range 1 to 156")

def plot_marks():
    '''Plots a graph of an individuals test result
        against the form of assessment'''
    try:
        #discards student id from the plot
        x = dfGrade.columns[1:]
        y = results

        plt.bar(x, y)
        plt.title("Test Results")
        plt.ylabel("Grade(%)")
        plt.xlabel("Assessment")

        plt.show()
    except:
        print("Try another value")











    
