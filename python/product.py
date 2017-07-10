class product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        if price > 1000:
            self.tax = .20
        else:
            self.tax = .10
    
    def returned(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box, like new":
            self.status = "sale"
        elif reason == "Opened":
            self.status = "opened"
        return self

    def display_all(self):
        print 'Price:' +str(self.price)
        print 'Item Name:' +str(self.item_name)
        print 'Weight:' +str(self.weight)
        print 'Brand:' +str(self.brand)
        print 'Cost:' +str(self.cost)
        print 'Status:' +str(self.status)
        print 'Tax:' +str(self.tax)
        return self

car1 = product(500, "Apple", 30, "Nike", 200)
car1.returned("defective").display_all()