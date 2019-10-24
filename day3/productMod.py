class Product:

    #모듈로 만들어서 TestClass1에서 호출해서 사용해 보세요...
    
    def __init__(self, sn, proName, price, maker):
        self.sn = sn
        self.proName = proName
        self.price = price
        self.maker = maker

    def setPrice(self, price):
        self.price = price
        
    def getPrice(self):
        return self.price

    def showProductInfo(self):
        print("serialNo :", self.sn, "name :",self.proName, "price :", self.price, "maker :", self.maker)
