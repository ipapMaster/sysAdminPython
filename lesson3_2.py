import logging

logging.basicConfig(filename='bugs.txt',
                    level=logging.ERROR,
                    format='%(asctime)s: %(module)s - %(message)s')

try:
    with open('info1.txt', encoding='utf-8') as f:
        text = f.read()
        print(text)
except Exception as e:
    logging.error(str(e))
