# Wikipedia Game

The Wikipedia Game is a computer game played on wikipedia.org.
Players start on a given Wikipedia article and then traverse the site using only
the hyperlinks in the articles to get to some destination article. The game can
be played for speed or for fewest links used.

The `wiki_game` function plays a simple version of this game, taking a depth-first approach to go from a given starting article to a given end goal article.

For example, the code fragment
```
path = wiki_game('Alan Turing', 'The Most Honourable')
print(' -> '.join(path))
```

will yield
`Alan Turing -> Turing (disambiguation) -> Alan Turing -> Turing Award -> Stephen Kettle -> Turing (cipher) -> Stream cipher -> Keystream -> Cryptography -> Secret Code -> Album -> Album (disambiguation) -> Phonograph record#78 rpm disc developments -> Phonograph Record (magazine) -> Music magazine -> List of music magazines -> Magazine -> Magazine (disambiguation) -> Quartering (heraldry) -> Impalement (heraldry) -> George Nugent-Temple-Grenville, 1st Marquess of Buckingham -> The Most Honourable`


## Eventual improvements
- Breadth-first search for the shortest path
- Tokenizing each webpage to estimate its distance from the end goal article, and intelligently choosing the next article to click on
