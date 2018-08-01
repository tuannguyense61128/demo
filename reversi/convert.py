def convertToArray(string_input):
    """
    Convert string from user's input to address in array
    """
    d = dict(zip('abcdefgh', range(0, 9)))
    try:
        result = int(string_input[1]) - 1, d[string_input[0]]
    except IndexError:
        return string_input
    except ValueError:
        return string_input
    result = list(result)
    return result


def convertToAbc(move):
    """
    Convert address in array to string
    """
    d = dict(zip(range(0, 9), 'abcdefgh'))
    return '{}{}'.format(d[move[1]], move[0] + 1)
