class IdentifiableEntity (object): #in Python all new classes must be subclass of the generic class object
    def __init__(self, identifiers):
        self.id = set()
        for identifier in identifiers:
            self.id.add(identifier)
    def getIds(self):
        result=[]
        for identifier in self.id:
            result.append(identifier)
        result.sort()
        return result

class Person (IdentifiableEntity):
    def __init__(self, identifiers, givenName, familyName):
        self.givenName= givenName
        self.familyName = familyName
        #we recall the constructor of the superclass to handle the 
        #input parameters as done in the superclass
        super().__init__(identifiers)

class Organization (IdentifiableEntity):
    def __init__(self, identifiers, name):
        self.name = name
        super().__init__(identifiers)
        
class Venue (IdentifiableEntity):
    def __init__(self, identifiers, title, publisher):
        self.title= title
        self.pubisher=publisher
        super().__init__(identifiers)

class Publication (IdentifiableEntity):
    def __init__(self, identifiers, publicationYear, title, author, publicationVenue):
        self.publicationYear= publicationYear
        self.title= title
        self.author =author
        self.publicationVenue = publicationVenue
        super().__init__(identifiers)

class JournalArticle (Publication):
    def __init__(self, identifiers, publicationYear, title, author, publicationVenue, issue, volume):
        self.issue = issue
        self.volume = volume
        super().__init__(identifiers, publicationYear, title, author, publicationVenue)

class BookChapter (Publication):
    def __init__(self, identifiers, publicationYear, title, author, publicationVenue, chapterNumber):
        self.chapterNumber = chapterNumber
        super().__init__(identifiers, publicationYear, title, author, publicationVenue)

class ProceedingsPaper (Publication):
    pass

class Journal (Venue):
    pass

class Book (Venue):
    pass

class Proceedings (Venue):
    def __init__(self, identifiers, title, publisher, event):
        self.event = event
        super().__init__(identifiers, title, publisher)