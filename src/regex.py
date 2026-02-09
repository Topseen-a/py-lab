import re

sentence_one = "I am a boy I am 12 years old I live Yaba"

def check_string(string):
    pattern = r"[^a-zA-Z0-9 ]"
    find_string = re.findall(pattern, string)
    if not find_string:
        return True
    else:
        return False

print(check_string(sentence_one))


sentence_two = "I am a boy"
regex_pattern = r"[aeiouAEIOU]"

def split_sentence(sentence):
    return sentence.split()

def find_vowels(sentence):
    vowel_words = list([word for word in split_sentence(sentence) if regex_pattern.find])

def add_vowels_in_dictionary(sentence):
    pass
