from Transaction import Transaction


class Member(object):
    """Member of the library """

    def __init__(self, username, password, fname, lname, email):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email

    def borrow(self, item):
        # create new transaction and add it to the transactions list
        new_transaction = Transaction(None, self.username, item.item_id)

        return new_transaction

    def __str__(self):
        return "Username: {}\nFirstName: {}\nLastName: {}\nEmail: {}\n".format(self.username, self.fname, self.lname, self.email)
