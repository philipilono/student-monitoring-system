import pandas as pd
from tkinter import *
from tkinter import scrolledtext
import matplotlib.pyplot as plt 

import testResults as t
import studentPerformance as s
import underperformingStudent as u
import hardworkingStudents as h



def check_id1():
    global student_id
    #converts string input into an integer
    student_id = int(studentid_entry.get())
    
            
def test_results():
    check_id1()
    global testMarks
    testMarks = t.read_marks(student_id)
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0",testMarks.to_string(index=True))#displays in box

def plot_results():
    check_id1()
    t.read_marks(student_id)
    t.plot_marks()

def check_id2():
    global student_id2
    student_id2 = int(studentid2_entry.get())

def txt1():
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0", "Now choose a form of analysis")#displays in box
    
def mock_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.mock_analysis(student_id2)
    txt1()

def test1_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.test1_analysis(student_id2)
    txt1()

def test2_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.test2_analysis(student_id2)
    txt1()

def test3_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.test3_analysis(student_id2)
    txt1()

def test4_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.test4_analysis(student_id2)
    txt1()

def sumtest_performance():
    check_id2()
    global abs_perform
    global rel_perform
    abs_perform, rel_perform = s.sumtest_analysis(student_id2)
    txt1()

def absolute_peformance():
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0",abs_perform.to_string(index=True))#displays in box

def relative_peformance():
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0",rel_perform.to_string(index=True))#displays in box

def underperform():
    check1 = u.under_perform()
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0",check1.to_string(index=False))#displays in box    
    
def underperform_plot():
    u.under_perform()
    u.plot_under_perform()

def hardwork():
    df = h.hard_work()
    StartPoint="1.0"
    txt_display.delete(StartPoint,END)#clear the box first
    txt_display.insert("1.0",df.to_string(index=False))
    
##################################################
#------------------MAIN---------------------------#
###################################################
        
window = Tk()
window.title("Student Monitoring System")
window.geometry("700x500")

####Test Results#####
lbl1 = Label(window, text="----Test Results----")
#.grid is used when defining location of component
lbl1.grid(row=0, column=0)

lbl2 = Label(window, text="Student ID:")
lbl2.grid(row=1, column=0)

studentid_entry = Entry(window)# the Entry widget is for getting a user input. 
studentid_entry.grid(row=2, column=0)

btn1=Button(window, text = "Student Test Results", command = test_results)
btn1.grid(row = 3, column = 0)

btn2=Button(window, text = "Plot Test Results", command = plot_results)
btn2.grid(row = 4, column = 0)


####Student Performance######
lbl2 = Label(window, text="----Student Performance----")
lbl2.grid(row=0, column=1, columnspan =2)

lbl3 = Label(window, text="Student ID:")
lbl3.grid(row=1, column=1, columnspan =2)

studentid2_entry = Entry(window)# the "Entry" widget is for getting a user input. 
studentid2_entry.grid(row=2, column=1, columnspan = 2)

mock_btn=Button(window, text = "Mock Test", command = mock_performance )
mock_btn.grid(row = 3, column = 1)

test1_btn=Button(window, text = "Test 1", command = test1_performance)
test1_btn.grid(row = 4, column = 1)

test2_btn=Button(window, text = "Test 2", command = test2_performance)
test2_btn.grid(row = 5, column = 1)

test3_btn=Button(window, text = "Test 3", command = test3_performance)
test3_btn.grid(row = 6, column = 1)

test4_btn=Button(window, text = "Test 4", command = test4_performance)
test4_btn.grid(row = 7, column = 1)

sumtest_btn=Button(window, text = "Sum Test", command = sumtest_performance)
sumtest_btn.grid(row = 8, column = 1)

lbl4 = Label(window, text="""Enter ID and choose a test before
selecting an analysis option""")
lbl4.grid(row=3, column=2, rowspan = 2)

ap_btn=Button(window, text = "Absolute Performance(AP)", command=absolute_peformance)
ap_btn.grid(row = 5, column = 2)

rp_btn=Button(window, text = "Relative Performance(RP)", command=relative_peformance)
rp_btn.grid(row = 6, column = 2)

ap_btn2=Button(window, text = "AP Visualisation", command = s.ap_plot)
ap_btn2.grid(row = 7, column = 2)

rp_btn2=Button(window, text = "RP Visualisation", command = s.rp_plot)
rp_btn2.grid(row = 8, column = 2)




###Underperforming Students###
lbl4 = Label(window, text ="----Underperforming Students----")
lbl4.grid(row = 9, column =0)

btn4=Button(window, text = "Check", command = underperform)
btn4.grid(row = 10, column = 0) 

btn5=Button(window, text = "Visualize", command = underperform_plot)
btn5.grid(row = 11, column = 0)

###Hardworking Students##
lbl5 = Label(window, text ="----Hardworking Students----")
lbl5.grid(row = 9, column = 1)

btn6=Button(window, text = "Check", command = hardwork)
btn6.grid(row = 10, column = 1) 





####Text Display######
txt_display = scrolledtext.ScrolledText(window,width = 80, height = 30)
txt_display.grid(column = 5, row =0, rowspan = 16, columnspan= 4)

            

window.mainloop()
