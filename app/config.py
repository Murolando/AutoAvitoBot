from configparser import ConfigParser

def get_tg_token():
    config = ConfigParser()
    config.read("config/bot.ini")

    try:
        tg_token = config["TOKEN"]["telegram_token"]
    except KeyError:
        print("Ошибка: такого ключа в конфигурационном файле нет")
        exit()
    else:
        return tg_token
    
def main():
    get_tg_token()

if __name__=="__main__":
    main()