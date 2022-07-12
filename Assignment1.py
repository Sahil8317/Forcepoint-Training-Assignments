
#Assignment 1
class ContactDetails:
    def __init__(self,contactID,contactType,contactemail):
        self.ContactDetailsId = contactID
        self.contactType = contactType
        self.Contactemail = contactemail

class Contact:
    isActive = True
    def __init__(self,contactID,firstName,lastName):
        self.contactID = contactID
        self.firstName = firstName
        self.lastName = lastName


class User:
    isActive = True
    isAdmin = False
    Usercontacts = []
    def __init__(self,userID,firstName,lastName,isAdmin):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin

    def createUser(self,userID,fName,LName):
        if self.isAdmin ==False:
            print("you are not a admin you cannot create a new user")
            return 
        newUser = User(userID,fName,LName,False)
        return newUser    

    def readUser(self,user):
        if self.isAdmin == False:
           print("you are not a admin you cannot read a user's data")
           return    
        if user.isActive == False:
            print("user is not active")
            return 
        print("user First Name "+user.firstName)
        print("user Last Name "+user.lastName)
        print("user userId "+user.userID)
        if user.isAdmin == False:
            print("user is staff")
        else:
            print("user is Admin")
        
    def updateUser(self,user,fName,LName,userId,isAdmin,isActive):
        if self.isAdmin == False:
           print("you are not admin you cannot update a user's data")
           return  
        if user.isActive == False:
           print("user is not active")
           return  
        user.firstName = fName
        user.lastName = LName
        user.userId = userId
        user.isAdmin = isAdmin
        user.isActive = isActive

    def deleteUser(self,user):
        if self.isAdmin == False:
           print("you are not admin you cannot delete a user")
           return  
        user.isActive = False
        return 

    def addContact(self,contactId,firstName,lastName):
        if self.isAdmin == True or self.isActive==False:
            print("you cannot add contacts")
            return 
        newContact =  Contact(contactId,firstName,lastName)
        self.Usercontacts.append(newContact)
        
# how to define crud operation on contacts if you don't know which contact is to be used.


admin = User("12","sahil","kesharwani",True)
newUser = admin.createUser("254","ab","cd")
admin.readUser(newUser)