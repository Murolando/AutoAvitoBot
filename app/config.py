from configparser import ConfigParser

def get_token():
    config = ConfigParser()

    config.read("config/bot.ini")
    try:
        telegram_token = config["TOKEN"]["telegram_token"]
    except KeyError:
        print("Ошибка: такого ключа в конфигурационном файле нет")
        exit()
    else:
        return telegram_token

def main():
    get_token()

if __name__=="__main__":
    main()