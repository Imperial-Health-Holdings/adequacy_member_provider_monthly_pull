import configparser
config = configparser.ConfigParser()
config.read('config_mailer.ini')

text = config['RECIPIENT']['recipient']

# Need a function to read recipient list and put into string seperated by "; "
item = [i.strip() for i in text.splitlines()]
item = filter(None, item)
item2 = '; '.join(item)

print(text)

print(item)

print(item2)