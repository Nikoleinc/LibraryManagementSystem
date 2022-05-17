import json
from Item import Item, Book, Article, DigitalMedia
from Staff import Staff
from Member import Member
from Transaction import Transaction
from Library import Library


def prompt_staff_user():
    """Function that prompts staff user for input operations"""
    print("Select an operation: ")
    print("1. Search Items by ID")
    print("2. Add Book")
    print("3. Add Article")
    print("4. Add Digital Media")
    print("5. Edit Book")
    print("6. Edit Article")
    print("7. Edit Digital Media")
    print("8. Delete Item")
    print("9: Exit")
    print()

    staff_user_choice = input("Enter number: ")
    return staff_user_choice

def create_new_book():
    """Function that creates a new book"""
    item_id = int(input("Enter ID: "))
    title = input("Enter title: ")
    author_artist = input("Enter author: ")
    publisher = input("Enter publisher: ")
    publication_year = input("Enter publication year: ")

    return Book(item_id, title, author_artist, publisher, publication_year)

def edit_book(book):
    """function to edit a book"""
    title = input("Enter new title: ")
    author_artist = input("Enter new author: ")
    publisher = input("Enter new publisher: ")
    publication_year = input("Enter new publication year: ")

    book.edit(title, author_artist, publisher, publication_year)

def create_new_article():
    """Function that creates a new article"""
    item_id = int(input("Enter ID: "))
    title = input("Enter title: ")
    author_artist = input("Enter author: ")
    publication_year = input("Enter publication year: ")
    journal_name = input("Enter journal name: ")
    journal_volume = input("Enter journal volume: ")
    journal_issue = input("Enter journal issue: ")

    return Article(item_id, title, author_artist, publication_year, journal_name, journal_volume, journal_issue)

def edit_article(article):
    """function to edit an article"""
    title = input("Enter new title: ")
    author_artist = input("Enter new author: ")
    publication_year = input("Enter new publication year: ")
    journal_name = input("Enter new journal name: ")
    journal_volume = input("Enter new journal volume: ")
    journal_issue = input("Enter new journal issue: ")

    article.edit(title, author_artist, publication_year, journal_name, journal_volume, journal_issue)

def create_new_digital_media():
    """Function that creates a new digital media"""
    item_id = int(input("Enter ID: "))
    title = input("Enter title: ")
    author_artist = input("Enter artist: ")
    publication_year = input("Enter publication year: ")
    digital_media_type = input("Enter Type: ")
    running_time = input("Enter running time: ")
    file_size = input("Enter file size: ")

    return DigitalMedia(item_id, title, author_artist, publication_year, digital_media_type, running_time, file_size)

def edit_digital_media(digital_media):
    """function to edit a digital media"""
    title = input("Enter new title: ")
    author_artist = input("Enter new artist: ")
    publication_year = input("Enter new publication year: ")
    digital_media_type = input("Enter new type: ")
    running_time = input("Enter new running time: ")
    file_size = input("Enter new file size: ")

    digital_media.edit(title, author_artist, publication_year, digital_media_type, running_time, file_size)


def update_json_file(filename, updated_list):
    """function that overwrites the file with items from the list"""
    openfile = open(filename, "w+")
    # from google, to correctly turn the object into json - https://pythonprinciples.com/ask/how-do-you-json-serialize-a-class-in-python/
    # set indentation on json https://tutorial.eyehunts.com/python/python-json-dumps-indent-example/
    openfile.write(json.dumps(updated_list, default=lambda obj: obj.__dict__, indent=4))
    openfile.close()

def update_items_json(updated_items):
    """function to update items json file """
    update_json_file("items.json", updated_items)

def search_item_by_id(search_id, books, articles, digital_medias):
    """function to search item by the id """
    for book in books:
        if int(search_id) == book.item_id:  #check book item_ids
            return book

    for article in articles:
        if int(search_id) == article.item_id: #check article item_ids
            return article

    for digitalmedia in digital_medias:
        if int(search_id) == digitalmedia.item_id: #check digital media item_ids
            return digitalmedia

def prompt_member() -> str:
    """Function that prompts member user for input operations"""
    print("Select an operation: ")
    print("1. Search Items by Title")
    print("2: Display Items")
    print("3. Borrow an item")
    print("4. Return all items")
    print("5: Exit")
    print()

    member = input("Enter number: ")
    return member

#######################################################################

"""STAFF JSON FILE TO DICTIONARY"""
#opening staff json file
with open('staff.json', 'r') as openfile:
    staff_file = json.load(openfile)
    openfile.close()

#create staff dictionary from staff file
staff_dictionary = {}
for user in staff_file:
    staff_instance = Staff(**user)
    staff_dictionary[staff_instance.username] = staff_instance

"""MEMBER JSON FILE TO DICTIONARY"""
#opening members json file
with open('members.json', 'r') as openfile:
    members_file = json.load(openfile)
    openfile.close()

#create member dictionary from members file
members_dictionary = {}
for member_user in members_file:
    member_instance = Member(**member_user)
    members_dictionary[member_instance.username] = member_instance


"""ITEMS LISTS FROM JSON FILE"""
#opening items json file
with open('items.json', 'r') as openfile:
    items_file = json.load(openfile)
    openfile.close()

#create list of books
books = []
for book in items_file['Books']:
    book_instance = Book(**book) # Create an instance of Book class using details from the json file
    books.append(book_instance)

#create list of articles
articles = []
for article in items_file['Articles']:
    article_instance = Article(**article) # Create an instance of Article class using details from the json file
    articles.append(article_instance)

#create list of digitalmedia
digital_medias = []
for digital_media in items_file['DigitalMedia']:
    digital_media_instance = DigitalMedia(**digital_media) # Create an instance of DigitalMedia class using details from the json file
    digital_medias.append(digital_media_instance)


"""BORROWING JSON FILE TO LIST"""
#opening borrowing json file
transactions = []
with open('borrowing.json', 'r') as openfile:
    borrowing_json = json.load(openfile)
    openfile.close()

transactions = []
for transaction in borrowing_json:
    transaction_instance = Transaction(**transaction) # Create an instance of Transaction class using details from the json file
    transactions.append(transaction_instance)


"""READING LIBRARY JSON FILE"""
with open('library.json', 'r') as openfile:
    library_details = json.load(openfile)

    # use double asterisks to split the object into the different properties
    # https://stackoverflow.com/questions/2921847/what-does-the-star-and-doublestar-operator-mean-in-a-function-call
    library = Library(**library_details)

    openfile.close()


#######################################################################

print("Welcome")
print(library)

#check user
user_login = input("Are you a member or staff: ")

#STAFF LOGIN
if user_login == "staff" or user_login == "Staff":
    #Staff login check
    while True:
        print("Enter your login details")
        input_username = input("Username: ")
        input_password = input("Password: ")


        if input_username in staff_dictionary.keys():
            user = staff_dictionary.get(input_username)
            if input_password == user.password:
                print("You are now logged in.")
            break
        else:
            print("Incorrect login details. Try again")

    # keep prompting staff user for operations until they exit
    print(user)
    staff_user_input = ""
    while staff_user_input != "9":  #(9 for exit)
        staff_user_input = prompt_staff_user()

        #operation 1: search items
        if staff_user_input == "1":
            search_id = input("Input item ID: ")
            item = search_item_by_id(search_id, books, articles, digital_medias)
            print(item)

        #operation 2: add book
        if staff_user_input == "2":
            new_book = create_new_book() #call create new book function
            books.append(new_book) #append new book to books list
            items_file["Books"] = books # update the books in the items file

            update_items_json(items_file) #call function to convert to JSON

        #operation 3: add article
        if staff_user_input == "3":
            new_article = create_new_article() #call create new article function
            articles.append(new_article)
            items_file["Articles"] = articles

            update_items_json(items_file) #call function to convert to JSON

        #operation 4: add digital media
        if staff_user_input == "4":
            new_digital_media = create_new_digital_media() #call create new digital media function
            digital_medias.append(new_digital_media)
            items_file["DigitalMedia"] = digital_medias

            update_items_json(items_file)

        #operation 5: edit book
        if staff_user_input == "5":
            item_id = int(input("Enter book ID to edit: "))
            for book in books:
                if book.item_id == int(item_id): #check input ID against existing item ID
                    edit_book(book) #call edit book function
                    break

            items_file["Books"] = books
            update_items_json(items_file)

        #operation 6: edit article
        if staff_user_input == "6":
            item_id = int(input("Enter article ID to edit: "))
            for article in articles:
                if article.item_id == int(item_id): #check input ID against existing item ID
                    edit_article(article) #call edit article function
                    break

            items_file["Articles"] = articles # update the articles in the items file
            update_items_json(items_file) #call function to convert to JSON

        #operation 7: edit digital media
        if staff_user_input == "7":
            item_id = int(input("Enter digital media ID to edit: "))
            for digitalmedia in digital_medias:
                if digitalmedia.item_id == int(item_id): #check input ID against existing item ID
                    edit_digital_media(digitalmedia) #call edit digital media function
                    break

            items_file["DigitalMedia"] = digital_medias
            update_items_json(items_file)

        #operation 8: delete an item based on their ID
        if staff_user_input == "8":
            item_id = int(input("Enter item ID to delete: "))
            for book in books:
                if int(item_id) == book.item_id: #checking if id match
                    books.remove(book) #remove
                    items_file["Books"] = books # update the books in the items file

            for article in articles:
                if int(item_id) == article.item_id:
                    articles.remove(article)
                    items_file["Articles"] = articles # update the articles in the items file

            for digitalmedia in digital_medias:
                if int(item_id) == digitalmedia.item_id:
                    digital_medias.remove(digitalmedia)
                    items_file["DigitalMedia"] = digital_medias # update the digitalmedias in the items file

            update_items_json(items_file) #call function to convert to JSON


#MEMBER LOGIN
elif user_login == "member" or user_login == "Member":
    #member login check
    while True:
        print("Enter your login details")
        input_username = input("Username: ")
        input_password = input("Password: ")

        if input_username in members_dictionary.keys():
            member = members_dictionary.get(input_username)
            if input_password == member.password:
                print("Your are now logged in.")
                break
        else:
            print("Incorrect login details. Try again")

    # keep prompting member user for operations until they exit
    print(member)
    member_input = ""
    while member_input != "5":  #(5 for exit)
        member_input = prompt_member()

        #operation 1: search items
        if member_input == "1":
            search_id = input("Input item ID: ")
            search_item_by_id(search_id, books, articles, digital_medias)

        #operation 2: display items
        if member_input == "2":
            for book in books:
                print(book)

            for article in articles:
                print(article)

            for digital_media in digital_medias:
                print(digital_media)

        #operation 3: borrow an item
        if member_input == "3":
            item_id = int(input("Enter item id to borrow: "))

            #setting it as false because we do not know if it is borrowed or not (i.e. check if it is there)
            item_is_already_borrowed = False
            for t in transactions:
                if t.item_id == item_id and t.member_username == member.username:
                    item_is_already_borrowed = True
                    break

            #if it is borrowed
            if item_is_already_borrowed:
                print("Item is already borrowed\n")
            else:
                item = search_item_by_id(item_id, books, articles, digital_medias)
                new_transaction = member.borrow(item) #call borrow method

                # Add new transaction to the list
                transactions.append(new_transaction)

                update_json_file("borrowing.json", transactions) #update json

        #operation 4: return all items
        if member_input == "4":
            for t in transactions:
                if t.member_username == member.username: #check if it is the member
                    transactions.remove(t) #remove transaction

            print("All items returned\n")
            update_json_file("borrowing.json", transactions) #update json





