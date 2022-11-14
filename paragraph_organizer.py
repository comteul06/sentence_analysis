character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ1234567890.,-!?/\"'():; "

# paragraph = input("Input paragraph (Must be divided with '.' and ' ')\n>> ").split('.')

paragraph = """In spite of the likeness between the fictional and real
world, the fictional world deviates from the real one in one
important respect.
The existing world faced by the individual is in principle
an infinite chaos of events and details before it is organized
by a human mind. This chaos only gets processed and
modified when perceived by a human mind.
The author has selected the content according to his own
worldview and his own conception of relevance, in an
attempt to be neutral and objective or convey a subjective
view on the world. Whatever the motives, the author's
subjective conception of the world stands between the
reader and the original, untouched world on which the
story is based.
Because of the inner qualities with which the individual is
endowed through heritage and environment, the mind
functions as a filter; every outside impression that passes
through it is filtered and interpreted. However, the world
the reader encounters in literature is already processed
and filtered by another consciousness."""

# remove all line changes.
paragraph = paragraph.replace('\n', ' ')

# remove all special characters
for character in paragraph:
    if character not in character_list:
        paragraph = paragraph.replace(character, '')

# divide string by '. '
sentence_list = paragraph.split('. ')
for i in range(len(sentence_list)):
    sentence_list[i] += '.'

# remove all characters between brackets

print(sentence_list)
