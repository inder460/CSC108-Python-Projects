class restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.num_served = 0

    def restaurant_type(self):
        print('the restaurant ' + self.name + ' serves ' + self.cuisine)

    def open_restaurant(self):
        print(self.name + ' is open.')

    def set_number_served(self, num_served):
        x = self.num_served = num_served
        x = str(x)
        print('People served: ' + x)

    def increment_number_served(self, more_served):
        y = self.num_served + more_served
        y = str(y)
        print('People Served: ' + y)


res1 = restaurant('pizza pizza', 'pizza')
res1.restaurant_type()
res1.open_restaurant()
res1.set_number_served(78)
res1.increment_number_served(22)

