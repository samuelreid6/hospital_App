
# patient Class

class Patient:
    def __init__(self, patient_Id, fname, lname, mother_Id, father_Id ):
        self.patient_Id = patient_Id
        self.fname = fname
        self.lname = lname
        self.mother_Id = mother_Id
        self.father_Id = father_Id

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)   

