
import User
import uuid
import CreditCardDetails

class Patient(User):

    def __init__(self,fName,lName,userName,userNumber,userEmail,userAdd,userPass,patientQuery,patientMedicalRecords,cardNumber,cardCvv,cardExpiry):
        super.__init__(fName,lName,userName,userNumber,userEmail,userAdd,userPass)
        self.patientID = (uuid.uuid4())
        self.patientQuery = patientQuery
        self.patientMedicalRecords = patientMedicalRecords
        self.cardNumber = cardNumber
        self.creditCard = CreditCardDetails(cardNumber,cardCvv,cardExpiry)
        

    def getDoctorAppointment():
        pass

    def getlabTestSchedule():
        pass

    def updateMedicalRecords():
        pass

    def updateQuery():
        pass

    def displayDischargeReport():
        pass

    def payHospitalBills():
        pass

    def allocatedWard(self,ward):
        self.ward = ward
        pass 

    def addPrescription(self):
        pass

    def updatePrescription():
        pass