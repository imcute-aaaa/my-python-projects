import requests
import easygui


response = requests.get('http://www.kada.com',
params='',
headers='')
print(response, response.url)
while easygui.ynbox('是否继续？', 'Codemao', ('', '')):
    pass
