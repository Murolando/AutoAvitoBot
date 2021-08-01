import sqlite3


class AutoBotDB:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # Проверяем есть ли пользователь
    def user_exist(self, chat_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `users` WHERE `chat_id` = ?", (chat_id,)).fetchall()
            return bool(len(result))

    # Добавляем пользователя
    def add_user(self, chat_id):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `users` VALUES(?,?)", (None, chat_id))

    # Проверяем есть ли подписка 
    def follow_exist(self,chat_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `follows` WHERE `chat_id` = ?", (chat_id,)).fetchall()
            return bool(len(result))
        
    # Добавляем новую подписку
    def add_follow(self, chat_id, mark_id=1, price_id=1):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `follows` VALUES(?, ?, ?, ?)", (None, mark_id, price_id, chat_id))

    # Редактируем подписку
    def red_follow(self, chat_id, mark_id, price_id):
        with self.connection:
            return self.cursor.execute(f"UPDATE `follows` SET `price_id` = ? AND `mark_id` = ? WHERE chat_id=`?`", (price_id, mark_id, chat_id))
    
    # Удаляем подписку
    # def del_follow(self,id_follow):
    #     with self.connection:
    #         return self.cursor.execute(f"DELETE FROM `follows` WHERE `id_follow`=?", (id_follow,))

    # Вывод подписок
    def show_subs(self, chat_id):
        result = self.cursor.execute(f"SELECT * FROM `follows` WHERE `chat_id` = ?", (chat_id,)).fetchall()
        vivod = []
        i = 0
        for line in result:
            mark = self.cursor.execute(f"SELECT `name` FROM `marks` WHERE `id_mark` = ?", (result[i][1],)).fetchall()
            price = self.cursor.execute(f"SELECT `price` FROM `prices` WHERE `id_price` = ?", (result[i][2],)).fetchall()
            vivod.append([*mark, *price])
            print(vivod[i])
            i += 1
        return vivod
