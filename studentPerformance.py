import pandas as pd
import sqlite3
import matplotlib.pyplot as plt 


   
def relative_analysis():
    '''Obtains the relative performance for a test. Relative performance
        is the difference between a students achieved mark and the average
        mark for the cohort in a particular question'''
    
    global rel_perform
    rel_perform = (marks.iloc[0])[1:]

    questions = df.columns[1:]
     #finds the average of each question and subtracts from achieved grade
    #in orderto calculate relative performance
    for i in range(len(questions)):
        base = df[questions[i]].mean()
        rel_perform[i] = rel_perform[i] - base

    
    return rel_perform
    

def mock_analysis(student_id):
    '''Obtains the absolute and relative performance for
        the Formative Mock Test for a given student ID'''
     #establishes a connection to talk to database
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    #selects grade and marks from the SQL table
    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10
                                        FROM Formative_Mock_Test"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    #ends connection
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform

##further functions are similar to mock_analysis so explanation is the same
def test1_analysis(student_id):
    '''Obtains the absolute and relative performance for
    the Formative Test 1 for a given student ID'''
        
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2,Q3,Q4,Q5,Q6
                                FROM Formative_Test_1"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform
    
def test2_analysis(student_id):
    '''Obtains the absolute and relative performance for
        the Formative Test 2 for a given student ID'''
    
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2,Q3,Q4,Q5,Q6
                                FROM Formative_Test_2"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform

def test3_analysis(student_id):
    '''Obtains the absolute and relative performance for
        the Formative Test 3 for a given student ID'''
    
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2,Q3,Q4,Q5,Q6
                                FROM Formative_Test_3"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform

def test4_analysis(student_id):
    '''Obtains the absolute and relative performance for
        the Formative Test 4 for a given student ID'''
    
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2
                                FROM Formative_Test_4"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform

def sumtest_analysis(student_id):
    '''Obtains the absolute and relative performance for
        the Summative Test for a given student ID'''
    
    sqliteConnection = sqlite3.connect('DataFiles\ResultDatabase.db')
    print("connection established")

    sqlite_read_record_query = """SELECT research_id,Grade,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13
                                FROM SumTest"""
    global df
    df=pd.read_sql(sqlite_read_record_query,sqliteConnection)
    sqliteConnection.close()

    global marks
    marks = df[df['research_id'] == student_id]

    global abs_perform
    abs_perform = (marks.iloc[0])[1:]

    abs_perform = pd.DataFrame(abs_perform)
    abs_perform.columns = ['AP']
    rel_perform =relative_analysis()
    rel_perform = pd.DataFrame(rel_perform)
    rel_perform.columns = ['RP']
    return abs_perform, rel_perform


def ap_plot():
    '''Generates a visualisation of absolute performance for each question'''
    x = marks.columns[1:]
    y = abs_perform

    plt.plot(x, y, 'r--*', label = "Absolute performace")
    plt.title("""Absolute performance across each question""")
    plt.ylabel("Grade Performace(%)")
    plt.xlabel("Question No.")
    plt.show()

def rp_plot():
    '''Generates a visualisation of relative performance for each question'''
    x = marks.columns[1:]
    y = rel_perform

    plt.plot(x, y, 'b--*', label = "Relative performace")
    plt.title("""Relative performance across each question""")
    plt.ylabel("Relative Performace(% difference)")
    plt.xlabel("Question No.")
    plt.show()
              
    
