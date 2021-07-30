REMOVE PUNCTUATION

main_string = "Google, LLC,() is an ()-[]{}; American #$ multinational. ' ;  [ { ] ) ( # ! technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the Big Four technology companies, alongside Amazon, Apple, and Microsoft."

new_string = main_string

new_string += '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


print (main_string)
print(" ")
print(new_string)
print(" ")
print(" ")
import string
out_string = main_string.translate(str.maketrans('', '', string.punctuation))

print("This is out_string: " + out_string)

print(" ")
print(" ")
print(" ")


characters_to_remove = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for character in characters_to_remove:
  new_string = new_string.replace(character, "")

print("This is new_string: " + new_string)

