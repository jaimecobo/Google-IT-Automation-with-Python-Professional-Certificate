def calculate_frequencies(file_contents): # Creates a dictionary with Key=word value=count
    new_string = (remove_punctuations(file_contents))
    new_string = (remove_numbers(new_string))
    new_string = (to_lowercase(new_string))
    new_list = (remove_words(new_string))
    dict_words = {}
    for word1 in new_list:
        counter = 0
        for word2 in new_list:
            if word2 == word1:
                counter += 1
            dict_words.update({word1: counter})
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict_words)
    return cloud.to_array()

    
def to_lowercase(file_contents): #Function to change to lowercase all the char in a string.
    return file_contents.lower()

def remove_punctuations(file_contents): #Function to remove punctuations marks.
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for punctuation in punctuations:
        file_contents = file_contents.replace(punctuation, "")
    return file_contents

def remove_numbers(file_contents): #Function to remove numbers.
    numbers = '0123456789'
    for number in numbers:
        file_contents = file_contents.replace(number, "")
    return file_contents

def remove_words(file_contents): #Funcion to remove unwanted words
    file_contents_list = file_contents.split()
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "in", "on"]
    for word in file_contents_list:
        for word in uninteresting_words:
            if word in file_contents_list:
                file_contents_list.remove(word)
    return file_contents_list