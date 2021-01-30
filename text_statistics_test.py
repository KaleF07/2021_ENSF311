import text_statistics

def test_personal_pronouns():
    assert text_statistics.count_personal_pronouns(" i, My, Me, You, We. ") == 5

def test_number_of_sentences():
    assert text_statistics.number_of_sentences("a! b, c. d? ") == 3

def test_number_of_words_in_document():
    assert text_statistics.number_of_words_in_document("a. b, c! ") == 3

def test_stdout(capsys):
    expected_out = ["Number of words in document 1071",
                    "Number of sentences in document 53",
                    "Number of words per sentence 20.21",
                    "Number of personal pronouns 36"] 

    text_statistics.print_text_statistics('feynman.txt')
    captured = capsys.readouterr()
    result = captured.out
    assert result.splitlines() == expected_out 