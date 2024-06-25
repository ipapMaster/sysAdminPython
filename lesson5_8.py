# Сериализация в JSON (JavaScript Object Notation)
import json

capitals = {'Russia': 'Moscow',
            'Belorussia': 'Minsk',
            }

content_string = json.dumps(capitals)

with open('capitals.json', 'w') as s:
    s.write(content_string)