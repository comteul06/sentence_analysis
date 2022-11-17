import data_writer as dw
import string_utilities as su

character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ1234567890.,-!?/\"'():; "

# paragraph = input("Input paragraph (Must be divided with '.' and ' ')\n>> ").split('.')

paragraph = """Philip Kitcher and Wesley Salmon have suggested that
there are two possible alternatives among philosophical
theories of explanation. One is the view that scientific
explanation consists in the unification of broad bodies of
phenomena under a minimal number of generalizations.
According to this view, the (or perhaps, a) goal of science
is to construct an economical framework of laws or
generalizations that are capable of subsuming all observable
phenomena. Scientific explanations organize and systematize
our knowledge of the empirical world; the more economical
the systematization, the deeper our understanding of what
is explained. The other view is the causal/mechanical
approach. According to it, a scientific explanation of a
phenomenon consists of uncovering the mechanisms that
produced the phenomenon of interest. This view sees the
explanation of individual events as primary, with the
explanation of generalizations flowing from them. That is,
the explanation of scientific generalizations comes from
the causal mechanisms that produce the regularities."""

# remove all line changes.
paragraph = paragraph.replace('\n', ' ')

# remove all special characters
for character in paragraph:
    if character not in character_list:
        paragraph = paragraph.replace(character, '')

# divide string by '. '
# sentence_list = paragraph.split('. ')
# for i in range(len(sentence_list)):
#     sentence_list[i] += "."

sentence_list = su.divideparagraph(paragraph)

dw.add_snts(sentence_list)
