import re
url = input("Enter URL: ")
if re.match(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", url):
    print("URL is Valid")
else:
    print("URL is Invalid") 