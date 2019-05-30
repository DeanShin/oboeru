# oboeru
Japanese Flashcards

A program that utilizes bootstrap, flask, and the [tatoeba database](https://tatoeba.org/eng/downloads) in order to create interactive Japanese flashcards.

Currently, the program selects a random sentence from the tatoeba database then generates a flashcard from the grammatical items present within the sentence. However, this may be subject to change, as randomly chosen grammar items may not be as intuitive for learning purposes.

# dependencies
[Flask](http://flask.pocoo.org/), [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/), [bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/), [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

# usage
Open Windows Powershell in the webapp folder.
```
python .\main.py 
```
Open a web browser and go to your IPv4 address
You can find this address by typing
```
ipconfig
```
Into Windows Powershell.

# todo
## forseeable
* Generate new flashcard after flashcard answered.
* Clean up sentences (remove {} things and |1 stuff)
* Create database of user-submitted sentences
* Upvote and downvote system for user-submitted sentences
* Prioritize long grammar items over particles
## ambitions
* Search for grammar function
* Sentences tailored to user settings.
* Look up unknown words and grammar
* Generate random sentences around grammar items
