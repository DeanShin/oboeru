# Oboeru
Japanese Flashcards

A program that utilizes bootstrap, flask, and the [tatoeba database](https://tatoeba.org/eng/downloads) in order to create interactive Japanese flashcards.

Currently, the program selects a random sentence from the tatoeba database then generates a flashcard from the grammatical items present within the sentence.

# Dependencies
[Flask](http://flask.pocoo.org/), [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/), [bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/), [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

# Usage
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
## Future Steps
* Generate new flashcard after flashcard answered.
* Clean up sentences (remove {} things and |1 stuff)
* Create database of user-submitted sentences
* Upvote and downvote system for user-submitted sentences
* Prioritize long grammar items over particles
* Derandomize incorrect answer grammar items
## Far Future
* Search for grammar function
* Sentences tailored to user settings.
* Look up unknown words and grammar
* Generate random sentences around grammar items
* Change randomization into pseudo randomization
