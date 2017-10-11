from profanity import profanity
 
def read_text():
    quotes = open("C:\learn python\movie_quotes.txt")
    contents_of_file = quotes.read()
    result_of_profanity_check = check_profanity(contents_of_file)
    if (result_of_profanity_check):
        print("Profanity Alert!!! The message cannot be sent")
    else:
        print("All is well! Your message is being sent")
    quotes.close()
 
def check_profanity(text_to_check):
    result = profanity.contains_profanity(text_to_check)
    return result
  
read_text()
