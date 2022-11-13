import pandas as pd
import numpy as np

character_list = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ1234567890.,-!?/"'():;"""

# paragraph = input("Input paragraph (Must be divided with '.' and ' ')\n>> ").split('.')

paragraph = """The above graphs show the percentage share of the global
middle class by region in 2015 and its projected share in
2025. ¨ç It is projected that the share of the global middle
class in Asia Pacific will increase from 46 percent in 2015 to
60 percent in 2025. ¨è The projected share of Asia Pacific in
2025, the largest among the six regions, is more than three
times that of Europe in the same year. ¨é The shares of
Europe and North America are both projected to decrease,
from 24 percent in 2015 to 16 percent in 2025 for Europe, and
from 11 percent in 2015 to 8 percent in 2025 for North
America. ¨ê Central and South America is not expected to
change from 2015 to 2025 in its share of the global middle
class. ¨ë In 2025, the share of the Middle East and North
Africa will be larger than that of sub-Saharan Africa, as it was
in 2015."""

# remove all line changes.
paragraph = paragraph.replace('\n', ' ')

# remove all special characters
for character in paragraph:
    if not character in character_list:
        paragraph.replace(character, '')

# divide string by '. '
# paragraph = paragraph.split('. ')

# remove all characters between brackets

print(paragraph)
