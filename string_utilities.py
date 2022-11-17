def divideparagraph(paragraph: str):
    result = []
    start_index = 0

    for i in range(len(paragraph)):
        if paragraph[i] == ' ' and i != 0:
            if paragraph[i - 1] == ('.' or '"') and (isupper(paragraph[i + 1]) or paragraph[i + 1] == '"'):
                result.append(paragraph[start_index:i])
                start_index = i + 1
    result.append(paragraph[start_index:])
    
    return result

def isupper(char: chr):
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    return False
