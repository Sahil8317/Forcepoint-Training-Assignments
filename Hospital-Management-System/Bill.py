
class Bill:
    def __init__(self,billAmount,patientID,billContents):
        self.billAmount = billAmount
        self.patientID = patientID
        self.billContents = billContents
        self.isBillPaid = False

    def getBillDetails(self):
        pass

    def updateBillStatus(self):
        pass