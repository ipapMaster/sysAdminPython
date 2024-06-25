# Сериализация в JSON (JavaScript Object Notation)
import json

with open('fruits.json', 'r') as s:
    json_content = s.read()

content = json.loads(json_content)

print(content)

