import html
import requests
from random import choice
from sentence import sentence
from findTemperatureLive import findTemperatureLive


def createHomePage(emailuser):
    firstname, lastname = emailuser.split(".")
    firstname = firstname.capitalize()
    fileName = f"{firstname}.{lastname}.html"
    file = open(fileName, 'w')
    file.write(createDocType())
    file.write(startHTML())
    file.write(createHead("Home Page for " + firstname + " " + lastname))
    file.write(startBody())
    file.write(createHeading("Home Page for " + firstname + " " + lastname))
    file.write(createParagraph("""This is the home page for """ + firstname + " " + lastname + """.\n"""))
    file.write(createParagraph("Here is a picture of Max Zhou.\n"
    + createImage(f"{emailuser}.jpg", "picture of Max Zhou")))
    file.write(createParagraph("We can also include links to other pages, such "
    + "as\n" + createLink("https://360.gordon.edu/myprofile",
    "Gordon's \nstudent")
    + ". Likewise, we can link to specific locations on a\npage, such as the "
    + createLink("#bottom","bottom of the page") + "."
    ))
    file.write(createParagraph("Here is a random sentence: " + sentence()))
    file.write(createParagraph("Here is the current temperature in Wenham: " + findTemperatureLive()))

    



    file.write(endBody())
    file.write(endHTML())
    file.close()

def createDocType():
    """Return standard html5 DOCTYPE string."""
    return '<!DOCTYPE html>\n'

def startHTML():
    """Return html start tag."""
    return '<html>\n\n'

def endHTML():
    """Return html end tag."""
    return '</html>\n'

def startBody():
    """Return body start tag."""
    return '<body>\n\n'

def createHeading(text):
    """Return a heading tag with the given text."""
    return '<h1>' + text + '</h1>\n'

def createParagraph(text):
    """Return a paragraph tag with the given text."""
    return '<p>' + text + '</p>\n'

def createImage(src, alt):
    """Return an image tag with the given src and alt text."""
    return '<img src="' + src + '" alt="' + alt + '">\n'

def createLink(href, text):
    """Return a hyperlink tag with the given href and text."""
    return '<a href="' + href + '">' + text + '</a>\n'

def endBody():
    """Return body end tag."""
    return '</body>\n'

def createHead(title):
    """Return head tag with the given title."""
    return '<head>\n<title>' + title + '</title>\n</head>\n'




    

def findTemperatureLive():  
    """Print the current temperature in Wenham using data from localconditions.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!
    """

    # Get the weather page
    weather = requests.get("https://www.localconditions.com/weather-boston-massachusetts/01984/").text

    # The temperature can be found near the top of the page after the word "Wenham" and
    # immediately before the HTML code &deg; (the degree symbol)
    curLoc = weather.find("Wenham")
    if curLoc != -1:
        # Now, find the degree symbol ("&deg;") following the temperature
        degLoc = weather.find("&deg;", curLoc)
        # The temperature number is preceded by a pipe
        tempLoc = weather.rfind("|", 0, degLoc)
        # Temperature value is everything between the pipe (and space) and the degree symbol
        print("Current temperature in Wenham is",weather[tempLoc+2:degLoc], "degrees")
        return "Current temperature in Wenham is " + weather[tempLoc+2:degLoc] + " degrees"
    else:
        print("Page format has changed; cannot find the temperature")

        return "Page format has changed; cannot find the temperature"
    

    


    
    

    

def sentence():
    """Generate a random sentence from a select set."""
    nouns = [
        "Mark",
        "Adam",
        "Angela",
        "Larry",
        "Jose",
        "Matt",
        "Jim"
        ]
    verbs = [
        "runs",
        "skips",
        "sings",
        "leaps",
        "jumps",
        "climbs",
        "fires a Civil War cannon",
        "swims",
        "argues",
        "giggles"
        ]
    phrases = [
        "in a tree",
        "through every room in the house",
        "very loudly",
        "around the bush",
        "while reading the newspaper",
        "very badly",
        "while skipping",
        "instead of grading",
        "while programming Python"
        ]
    print(choice(nouns), choice(verbs), choice(phrases)+".")
    return f"{choice(nouns)} {choice(verbs)} {choice(phrases)}."

if __name__ == "__main__":
    createHomePage("Max.Zhou")
    #sentence()