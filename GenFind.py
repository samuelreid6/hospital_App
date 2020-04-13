import sqlite3
from function import Patient

conn = sqlite3.connect('database.db')
genFind = conn.cursor()
idFind = conn.cursor()

patient_Id = 1232
fname = "aaaa"
lname = "aaaa"
mother_Id = 000
father_Id = 0000
data = "data"
i = 1
patient_Id = input('Enter Client ID Number')


def main():    
    openconn()
    
    clientfunc()
    
    
  





def imputPatientfunc():
    patient_Id = input( "Enter Patient ID Number.  :")
    fname = input( "Enter Patient first name.  :")
    lname = input( "Enter Patient last name.  :")
    mother_Id = input( "Enter Patient mother's ID Number  :")
    father_Id = input( "Enter Patient father's ID Number  :")
    genFind.execute("INSERT INTO patient_tbl VALUES (:patient_Id, :fname, :lname, :mother_Id, :father_Id )", {'patient_Id': patient_Id, 'fname': fname, 'lname': lname, 'mother_Id': mother_Id, 'father_Id': father_Id})
    

def viewPatientfunc():
    genFind.execute("SELECT * FROM patient_tbl")
    print(genFind.fetchall())
    
    
def clientfunc():
    genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id = (:patient_Id)", {'patient_Id': patient_Id})
    #print(genFind.fetchall())
    data = genFind.fetchall()
    for i in data:
        print('Client Information')
        print(i)
    print('Mother Information')    
    genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id = (:mother_Id_col)", {'mother_Id_col': i[3]})
    print(genFind.fetchall())
    print('father Information')
    genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id = (:father_Id_col)", {'father_Id_col': i[4]})
    print(genFind.fetchall())
    print('Siblings Information')
    genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id != (:patient_Id_col) AND mother_Id = (:mother_Id_col) AND father_Id = (:father_Id_col)", 
    {'patient_Id_col':i[0],'mother_Id_col':i[3], 'father_Id_col':i[4] })

    print(genFind.fetchall()) 
    
    

# def motherfunc():
#     genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id = 1234")
#     print(genFind.fetchall())
    
    

# def fatherfunc():
#     genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id = 1235")
#     print(genFind.fetchall())

# def siblings():
#     genFind.execute("SELECT * FROM patient_tbl WHERE patient_Id != (:patient_Id) AND mother_Id = 1234 AND father_Id = 1235", {'patient_Id': patient_Id})
#     print(genFind.fetchall())   


    
def openconn():
    conn.commit()
def closeconn():
    conn.close()

if __name__ == '__main__': main()
