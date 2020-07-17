#!/usr/bin/env python

"""Retrieve and print words form a URL."""
# module doc strings should always be at the top
# doc string allows us to communicate how to use the module
from urllib.request import urlopen


def fetch_words():
    """Fetches a list of words form a URL"""
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(story_words):
    "Prints items form a list"
    for word in story_words:
        print(word)


def main():
    """The main function"""
    words = fetch_words()
    print_items(words)


if __name__ == '__main__':
    main()
