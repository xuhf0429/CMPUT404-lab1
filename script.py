import requests

print("> requests version: %s" % requests.__version__)

get_new_link = requests.get("https://www.google.com")
print(get_new_link.content)
print(get_new_link.status_code)

new_repo_url = requests.get('https://raw.githubusercontent.com/xuhf0429/CMPUT404_lab1/main/script.py')
print(new_repo_url.status_code)
print(new_repo_url.text)




