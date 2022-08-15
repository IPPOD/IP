import pandas as pd
##import matplotlib.pyplot as plt 
##import numpy as np
import mysql.connector as cl

import time

Access = cl.connect(host = "localhost", user = "root", passwd = "root", database = "ip")

if Access.is_connected():
    print("Conenction Success...")
else:
    print("Connection is unstable:")


df=pd.read_sql("Select * from empl;",Access)


print ("Welcome User")
time.sleep(2)


print("Please enter your Option:")
print("1.View Employee Data")
print("2.Export Data")
print("3.Modify Data")
##print("4.Delete Data")
##print("5.Add Data")
##print("6.Generate Graph")
##print("7.Generate Report")
print("8.Sort Data")
print("10.Exit")






A=(input("Please enter your Option:"))



if A=="1":
    print (df)

elif A=="2":
    B=(input("Exporting data to which drive(C,D,E,F):"))
    df.to_csv (B+":\\all1.csv")
    B=B.capitalize()
    print("Data Successfully Grabed to:",B,"Drive")

elif A=="3":
    df=pd.read_sql("Select * from EMPL",Access)
    print (df)
    C=input ('''What you want to modify:
                1.Column Name
                2.Column Data
                ''')
    if C=="1":
        D=input("Which Field:")
        E=input("Enter new Field Name:")
        R="alter table EMPL RENAME COLUMN "+D+" TO "+E
        R=str(R)
        df=pd.read_sql(R,Access)
        print(df)

        
    elif C=="2":
        F=input ("Which Column:")
        G=input ("What new value you want to Modify ex- varchar(30):")
        df=pd.read_sql(" alter table EMPL MODIFY COLUMN " + F+" "+ G,Access)
        print(df)
        




elif A=="8":
    df=pd.read_sql("Desc Empl",Access)
    print (df)
    C=input("By Which column You want to sort:(COLUMN NAME)")
    D=input ("Do you want to sort in ascending(A) or descending(D):")
    if D=="A":
        df=pd.read_sql("SELECT * FROM EMPL ORDER BY "+C,Access)
        print(df)
        
    elif D=="D":
        df=pd.read_sql("SELECT * FROM EMPL ORDER BY "+C+" DESC",Access)
        print(df)
        
    else:
        print("No Table exist")




    
elif A=="10":
    exit()
else:
    print("Out of range")

