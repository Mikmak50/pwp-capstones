class User(object):
    def __init__(self, name, email):
        self.name = name #string
        self.email = email #string
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "User " + self.name + " email address was updated to " + self.email

    def __repr__(self):
        print("User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books.update({book: rating})

    def get_average_rating(self):
        get_average_rating = 0
        for book,rating in self.books.items():
            if rating != None:
                get_average_rating += rating
        return get_average_rating / len(self.books)




class Book():
    def __init__(self, title, isbn):
        self.title = title #string
        self.isbn = isbn #number
        self.ratings = [] #list
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbnNumber):
        self.isbn = isbnNumber
        print("This book’s ISBN has been updated")

    def add_rating(self, rating):
        if type(rating) == int and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
            print("Rating added")
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        get_average_rating = 0
        for rating in self.ratings:
            get_average_rating += rating
        return get_average_rating / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author #string

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject #string
        self.level = level #string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject


class TomeRater():
    def __init__(self):
        self.users = {} #Fromat: email: User(obj)
        self.books = {} #Format: Book(obj): 3

    def create_book(self, title, isbn):
        create_book = Book(title, isbn)
        
        return create_book

    def create_novel(self, title, author, isbn):
        create_novel = Fiction(title, isbn, author)
        return create_novel

    def create_non_fiction(self, title, subject, level, isbn):
        create_non_fiction = Non_Fiction(title, isbn, subject, level)
        return create_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            objUser = self.users.get(email)
            objUser.read_book(book, rating)
            book.add_rating(rating)
            bookcurrentread = self.books.get(book)
            if bookcurrentread == None:
                self.books.update({book: 1})
            else:
                self.books.update({book: bookcurrentread + 1})
            
        else:
            print("No user with email " + email + "!")
    
    def add_user(self, name, email, user_books = None):
        emailExist = False
        if email.find("@") < 1:
            print("Email: " + email + " is not correctly formated. Please use xxx@yyy.xxx format")
            return "Error"
        
        if  email[-4:] == ".edu" or email[-4:] == ".com" or email[-4:] == ".org":

            for key in self.users.keys():
                if key == email:
                    emailExist = True
                    print("Email: " + email + " already exists! User not added")
                    return "Error"
                    
            userObj = User(name, email)
            self.users.update({email: userObj})
            
            if user_books != None:
                for bookobj in user_books:
                    self.add_book_to_user(bookobj, email)
        else:
            print("Email: " + email + " is not correct. Please use an .edu, .org or .com email")
            return "Error"

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def highest_rated_book(self):
        topRate = 0
        topBook = ""
        for book, rating in self.books.items():
            if rating > topRate:
                topBook = book.title
                topRate = rating
        return topBook

    def most_positive_user(self):
        topRatingAv = 0
        for key, user in self.users.items():
            if user.get_average_rating() > topRatingAv:
                topRatingAv = user.get_average_rating()
                topRateUser = user.name
        return topRateUser

    def get_most_read_book(self):
        topReaderBook = ""
        topReaderCount = 0
        for book, reader in self.books.items():
            if reader > topReaderCount:
                topReaderCount = reader
                topReaderBook = book.title
        print("Top read book: " + topReaderBook + " count: " + str(topReaderCount))
        return topReaderBook