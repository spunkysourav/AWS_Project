class Customer:
    list_cus=[]
    def __init__(self):
        self.id=0
        self.name=" "
        self.address=" "
        self.mobileno=" "
    def __str__(self):
        return "Customer Details: Id={0}, Name={1}, Address={2}, Mobile No={3}".format(self.id,self.name,self.address,self.mobileno)
    def addCustomer(self):
        Customer.list_cus.append(self)
        return
    def searchCustomer(self,id):
        for e in Customer.list_cus:
            if e.id==id:
                self.id=e.id
                self.name=e.name
                self.address=e.address
                self.mobileno=e.mobileno
                return
        print("Id Not Found!!")
    def deleteCustomer(self,id):
        for e in Customer.list_cus:
            if e.id==id:
                Customer.list_cus.remove(e)
                return
    def modifyCustomer(self,id):
        for e in Customer.list_cus:
            if e.id==id:
                e.name=self.name
                e.address=self.address
                e.mobileno=self.mobileno
                return
    @staticmethod
    def showallCustomer():
        return Customer.list_cus
    @staticmethod
    def sortallCustomer():
        return Customer.list_cus.sort(key=lambda e:e.id,reverse=False)