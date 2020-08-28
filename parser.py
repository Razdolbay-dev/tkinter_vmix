import xml.etree.ElementTree as ET
import os
#import requests
os.system('curl -o vmix.xml http://10.1.0.8:8088/API')
root = ET.parse('vmix.xml').getroot()
# Учим парсить файл в корне проекта
# Переменные
list_input = []
guid = ()
key = None
def pars(value):
    root_find = root.findall('inputs/')
    for tag in root_find:
        title = tag.get('title')
        key = tag.get('key')
        duration = tag.get('duration')
        input = tag.get('number')
        data = {'Input': input,'Title': title, 'GUID': key, 'Time': duration}
        list_input.append(data)

result = pars(list_input)
for s in list_input:
    print(s)

def change(key):
    name = input('Введите название: ')
    for i in list_input:
        title = i['Title']
        if title == name:
            key = i['GUID']
            return key

guid = change(key)
print('Ваш ключ: ',guid)
