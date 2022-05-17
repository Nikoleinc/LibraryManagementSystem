class Library(object):
    """Library class with library information"""
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Library name: {}\nAddress: {}\nPhone: {}\nEmail: {}\n".format(self.name, self.address, self.phone, self.email)
