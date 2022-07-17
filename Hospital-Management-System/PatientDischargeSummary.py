from re import X


class PatientDischargeSummary:
    def __init__(self,patientHealth,DischargeTime,medicalHistory,diagnosis,drugPrescription,courseInHospital):
        self.patientHealth = patientHealth
        self.DischargeTime = DischargeTime
        self.medicalHistory = medicalHistory
        self.diagnosis = diagnosis
        self.drugPrescription = drugPrescription
        self.courseInHospital = courseInHospital

    def displayDischargeReport(self):
        pass

    def getDischargeReport(self):
        pass 
        