import sqlite3
conn = sqlite3.connect('database.db')

genFind = conn.cursor()

# patient_Id = 1232
# fname = "aaaa"
# lname = "aaaa"
# mother_Id = 000
# father_Id = 0000
def main():  
    viewPatientfunc()
    viewPatientfunc()
    





def viewPatientfunc():
    genFind.execute("SELECT * FROM patient_tbl")
    print(genFind.fetchall())

def openconn():
    conn.commit()
def closeconn():
    conn.close()

if __name__ == '__main__': main()

conn.commit()
conn.close()
