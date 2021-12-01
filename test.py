import configparser
config = configparser.ConfigParser()
config.read('config.ini')

text = config['MAILER']['text']

print(text)