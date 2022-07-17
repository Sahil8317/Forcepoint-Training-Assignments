
from mimetypes import init

import User

class HospitalStaff(User):
    def __init__(self,fName,lName,userName,userNumber,userEmail,userAdd,userPass,isDoctor,salaryAmount,bankDetails):
        super.__init__(fName,lName,userName,userNumber,userEmail,userAdd,userPass)
        self.isDoctor = isDoctor
        self.salaryAmount = salaryAmount
        self.bankDetails = bankDetails
        self.patientsUnder = []
        self.appointments = []
        self.doctors = []


    def addPatient(self):
        pass

    def addDoctor(self):
        pass

    def updateStaffBankDetails(self):
        pass

    def addAppointment(self):
        pass

    def changeAppointment(self):
        pass

    def displayStaffInformation(self):
        pass
    
    def generatePatientBills(self):
        pass
    

    

