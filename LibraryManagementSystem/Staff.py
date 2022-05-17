class Staff(object):
    """Staff of the library, with their information. Username as the key"""
    def __init__(self, username, password, fname, lname, email):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Username: {}\nFirstName: {}\nLastName: {}\nEmail: {}\n".format(self.username, self.fname, self.lname, self.email)
