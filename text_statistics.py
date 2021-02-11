# Author: Kale Fordham
def count_personal_pronouns(s):
    """Count personal pronouns I, my, me, you, we in string s

    The pronouns are counted regardless of capitalization.

    s (str): string to be searched for pronouns
    returns: (int) Number of personal pronouns
    """

    #TODO: implement function
    count = 0
    s_new = s.lower()
    s_new = s_new.replace('.',' ')
    s_new = s_new.replace(',',' ')
    s_new = s_new.replace('?',' ')
    s_new = s_new.replace('!',' ')
    
    
    for word in s_new.split():
        if (word == 'i') or (word == 'my') or (word == 'me') or (word == 'you') or (word == 'we'):
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
        if (words != '.') or (words != ',') or (words != '?') or (words != '!'):
            count += 1

    return count

def number_of_sentences(s):
    """Counts number of sentences (seprated by '.', '!' or '?') in string s

    s (str): string to count sentences in
    returns: (int) number of sentences
    """

    #TODO: implement function
    count = 0
    for word in s:
        if (word == '.') or (word == '!') or (word == '?'):
            count += 1

    return count

def print_text_statistics(filename):
    """Prints sentence, word, word-per-sentence and personal pronoun count

    Functions in this module are used for counting.
        
    filename (str): Name of file to analyze (UTF-8 encoded)
    returns: None
    """
    #TODO: Read text from UTF-8 encoded file. 
    fin = open(filename, mode = 'r', encoding = 'utf-8')
    string = ""
    for ele in fin:
        string += ele

    #TODO: Print results, use functions above for computations
    print('Number of words in document {}'.format( number_of_words_in_document(string)) )
    print('Number of sentences in document {}'.format( number_of_sentences(string)) )
    print('Number of words per sentence {}'.format( round(number_of_words_in_document(string)/number_of_sentences(string), 2)) )
    print('Number of personal pronouns {}'.format( count_personal_pronouns(string)) )

if __name__ == '__main__':
    
    print_text_statistics('feynman.txt')