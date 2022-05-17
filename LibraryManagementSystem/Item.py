class Item(object):
    """Items in the library, parent class of book, article, digital media """

    def __init__(self, item_id, title, author_artist, publication_year):
        self.item_id = item_id
        self.title = title
        self.author_artist = author_artist
        self.publication_year = publication_year

    #parent method to edit
    def edit(self, title, author_artist, publication_year):
        self.title = title
        self.author_artist = author_artist
        self.publication_year = publication_year


# inherit from Item
class Book(Item):
    """Book; subclass of Items"""

    def __init__(self, item_id, title, author_artist, publisher, publication_year):
        # call parent init
        Item.__init__(self, item_id, title, author_artist, publication_year)
        self.publisher = publisher

    # will be called when instance is printed to console
    def __str__(self):
        return "ID: {}\n" \
               "Title: {}\n" \
               "Author: {}\n" \
               "Publisher: {}\n" \
               "Publication Year: {}\n"\
            .format(self.item_id, self.title, self.author_artist, self.publisher, self.publication_year)

    def edit(self, title, author_artist, publisher, publication_year):
        # call parent init
        Item.edit(self, title, author_artist, publication_year)
        self.publisher = publisher


# inherit from Item
class Article(Item):
    """Article; subclass of Items"""

    def __init__(self, item_id, title, author_artist, publication_year, journal_name, journal_volume, journal_issue):
        # call parent init
        Item.__init__(self, item_id, title, author_artist, publication_year)
        self.journal_name = journal_name
        self.journal_volume = journal_volume
        self.journal_issue = journal_issue

    # will be called when instance is printed to console
    def __str__(self):
        return "ID: {}\n" \
               "Title: {}\n" \
               "Author: {}\n" \
               "Publication Year: {}\n" \
               "Journal Number: {}\n" \
               "Journal Volume: {}\n" \
               "Journal Issue\n"\
            .format(self.item_id, self.title, self.author_artist, self.publication_year, self.journal_name, self.journal_volume, self.journal_issue)

    def edit(self, title, author_artist, publication_year, journal_name, journal_volume, journal_issue):
        # call parent edit method
        Item.edit(self, title, author_artist, publication_year)
        self.journal_name = journal_name
        self.journal_volume = journal_volume
        self.journal_issue = journal_issue


# inherit from Item
class DigitalMedia(Item):
    """DigitalMedia: subclasses of Items"""

    def __init__(self, item_id, title, author_artist, publication_year, digital_media_type, running_time, file_size):
        # call parent init
        Item.__init__(self, item_id, title, author_artist, publication_year)
        self.digital_media_type = digital_media_type
        self.running_time = running_time
        self.file_size = file_size

    # will be called when instance is printed to console
    def __str__(self):
        return "ID: {}\n" \
               "Title: {}\n" \
               "Author: {}\n" \
               "Publication Year: {}\n" \
               "Type: {}\n" \
               "Running Time: {}\n" \
               "File Size: {}\n"\
            .format(self.item_id, self.title, self.author_artist, self.publication_year, self.digital_media_type, self.running_time, self.file_size)

    def edit(self, title, author_artist, publication_year, digital_media_type, running_time, file_size):
        # call parent init
        Item.edit(self, title, author_artist, publication_year)
        self.digital_media_type = digital_media_type
        self.running_time = running_time
        self.file_size = file_size
