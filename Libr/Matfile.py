# // File Manager For Python //
# 1. Could have errors, Sorry pal.
# 2. Available for UTF-8 & JSON right now.




#                    This is a learning sheet... 

###################################################################

#                              WITH
# 1. with command automatically closes the file after using it.
# 2. 'w' = Overwrite / Create file and write.
# 3. 'r' = Read.
# 4. 'a' = Append / add at last line.
# 5. \n = new line
#
#                              Usage
#                               'w'
#       with open("notes.txt", "w", encoding="utf-8") as file1:
#           file1.write("Started this project\n")
#           file1.write("Might leave it half.")
#
#                               'r'
#       with open("notes.txt", "r", encoding="utf-8") as file1:
#           content = file1.read()
#           print(content)
#
#                               'a'
#       with open("history.txt", "a", encoding="utf-8") as file1:
#           file1.write(f"Searched city: {city}\n")
#
#

###################################################################

#                              JSON
# 1. import json (required) 
#
#                              Usage
#               SAVING A DICTIONARY TO A JSON FILE
#        settings = {"theme": "dark", "lang": "en"}
#        with open(settings.json, "w") as f:
#            json.dump(settings, f) 
#
#               READING A DICTIONARY FROM A JSON FILE 
#        with open(settings.json, "r") as f:
#            data = json.load(f)
#            print(data["theme"])

###################################################################


