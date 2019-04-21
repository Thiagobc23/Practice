class Products:

    def __init__(self, name, category, value):
        self.name = name
        self.category = category
        self.value = value

    def __repr__(self):
        return "Products('{}','{}','{}')".format(self.name, self.category, self.value)
