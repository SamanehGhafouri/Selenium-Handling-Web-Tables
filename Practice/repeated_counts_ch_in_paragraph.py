from collections import Counter


def counts_of_characters_in_paragraph(paragraph):

    return Counter(paragraph.casefold())


if __name__ == '__main__':
    parag = "Hello there my name is Samaneh. I am a Software Engineer, so let's solve this problem."
    result = counts_of_characters_in_paragraph(parag)
    print(result)