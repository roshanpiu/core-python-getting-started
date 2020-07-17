from urllib.request import urlopen
# Generally better to write functions that doesn't produce side effects

def fetch_words():
  story = urlopen('http://sixty-north.com/c/t.txt')
  story_words = []
  for line in story:
      line_words = line.decode('utf8').split()
      for word in line_words:
        story_words.append(word)

  story.close()
  for word in story_words:
      print(word)

""" ___name___ is a specially named variable allowing us to detect 
    weather a module is run as a script or 
    imported into another module
"""

if __name__ == '___name___':
  fetch_words()

""" def is a statement that gets executed with the other top level module code
    causes the code within the function to be bound to the name of the function
"""

""" when modules are imported or run all the top level statements are run
    this is where the function within the module namespace is defined 
    
    Python modules - convenient import with API
    Python script - convenient execution from command line
    Python program - Perhaps composed of many modules

    It's better to add a post script to facilitate execution to modules
    ex - if __name__ == '___name___':
            fetch_words()
"""