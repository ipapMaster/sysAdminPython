import configparser

cfg = configparser.ConfigParser()
cfg.read('main.ini')
sects = cfg.sections()
print(sects)
sect = cfg.options('one')
print(sect)
print(cfg.get('one', 'first'))
