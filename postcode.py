def space_stripper(raw_postcode: str) -> str:
    raw_postcode = raw_postcode.upper()
    no_space = ""

    for letter in raw_postcode:
        if letter == " ":
            pass
        else:
            no_space += letter
    return no_space


def extract_outer(postcode: str) -> str:

    postcode = space_stripper(postcode)
    length = len(postcode)
    outgoing = ""
    count = 0

    for letter in postcode:
        if count == (length - 3):
            break
        else:
            count += 1
            outgoing += letter

    return outgoing


def extract_inner(postcode: str) -> str:

    postcode = space_stripper(postcode)
    length = len(postcode)
    outgoing = ""
    count = 0

    for letter in postcode:
        if count > (length - 4):
            outgoing += letter

        else:
            count += 1

    return outgoing
