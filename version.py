import requests

# print(requests.__version__)
r = requests.get('https://raw.githubusercontent.com/cmput404-F21-labs/lab1/master/version.py')
print(r.text)