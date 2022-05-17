class Transaction(object):
    """Transactions class of members borrowing, has a transaction key"""
    def __init__(self, transaction_id, member_username, item_id):
        # create new id if there is no existing one
        if transaction_id is None:
            # set the id as the combination of the member username and item id
            # the same member shouldn't be able to borrow the same item multiple times
            self.transaction_id = "{}{}".format(member_username, item_id)
        else:
            self.transaction_id = transaction_id

        self.member_username = member_username
        self.item_id = item_id

    def __str__(self):
        return "transaction_id: {}\n" \
               "item: {}\n" \
               "member: {}\n"\
            .format(self.transaction_id, self.item_id, self.member_username)

