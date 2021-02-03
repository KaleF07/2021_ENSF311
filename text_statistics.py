# Author: Kale Fordham
def count_personal_pronouns(s):
    """Count personal pronouns I, my, me, you, we in string s

    The pronouns are counted regardless of capitalization.

    s (str): string to be searched for pronouns
    returns: (int) Number of personal pronouns
    """

    #TODO: implement function
    count = 0

    for word in s.split():
        if word == 'i' or 'I' or 'my' or 'My' or 'me' or 'Me' or 'you' or 'You' or 'we' or 'We':
            count += 1

    return count

def number_of_words_in_document(s):
    """Counts number of words (seprated by whitespace) in string s

    s (str): string to count words in
    returns: (int) number of words
    """

    #TODO: implement function
    count = 0
    for words in s.split():
        count += 1

    return count

def number_of_sentences(s):
    """Counts number of sentences (seprated by '.', '!' or '?') in string s

    s (str): string to count sentences in
    returns: (int) number of sentences
    """

    #TODO: implement function
    count = 0
    for word in s.split():
        if word == '.' or '!' or '?':
            count += 1

    return count

def print_text_statistics(filename):
    """Prints sentence, word, word-per-sentence and personal pronoun count

    Functions in this module are used for counting.
        
    filename (str): Name of file to analyze (UTF-8 encoded)
    returns: None
    """
    #TODO: Read text from UTF-8 encoded file. 
    fin = open(filename, 'r')
    lines = fin.readlines()

    #TODO: Print results, use functions above for computations
    count_personal_pronouns(lines)
    number_of_words_in_document(lines)
    number_of_sentences(lines)

if __name__ == '__main__':
    
    print_text_statistics('feynman.txt')