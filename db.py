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

    # Проверяем есть ли вообще подписки
    def follows_exists(self, chat_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `follows` WHERE `chat_id` = ?", (chat_id,)).fetchall()
            return bool(len(result))

    # Проверяем есть ли уже такая конкретная подписка
    def this_follow_exist1(self, chat_id, mark_id, price_id):
        with self.connection:
            result = self.cursor.execute(
                f"SELECT * FROM `follows` WHERE `mark_id` = ? AND `chat_id` = ?",
                (mark_id, chat_id)).fetchall()
            return bool(len(result))

    # Проверяем есть ли уже такая конкретная подписка c id_follow
    def this_follow_exist2(self, id_follow):
        with self.connection:
            result = self.cursor.execute(
                f"SELECT * FROM `follows` WHERE `id_follow` = ? ", (id_follow,)).fetchall()
            return bool(len(result))

    # Добавляем новую подписку
    def add_follow(self, chat_id, mark_id=1, price_id=1):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `follows` VALUES(?, ?, ?, ?)", (None, mark_id, price_id, chat_id))

    # Редактируем подписку
    def red_follow(self, chat_id, mark_id, price_id):
        with self.connection:
            return self.cursor.execute(f"UPDATE `follows` SET `price_id` = ? AND `mark_id` = ? WHERE `chat_id` =?",
                                       (price_id, mark_id, chat_id))

    # Удаляем конкретную подписку
    def del_this_follow(self, id_follow):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM `follows` WHERE `id_follow`=?", (id_follow,))

    # Удалить все подписки после /stop
    def del_follow(self, chat_id):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM `follows` WHERE `chat_id` = ?", (chat_id,))

    # Вывод подписок
    def show_subs(self, chat_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `follows` WHERE `chat_id` = ?", (chat_id,)).fetchall()
            vivod = []
            i = 0
            for line in result:
                id_follow = result[i][0]

                mark = self.cursor.execute(f"SELECT `name` FROM `marks` WHERE `id_mark` = ?",
                                           (result[i][1],)).fetchall()
                price = self.cursor.execute(f"SELECT `price` FROM `prices` WHERE `id_price` = ?",
                                            (result[i][2],)).fetchall()
                price_up = self.cursor.execute(f"SELECT `price_up` FROM `prices` WHERE `id_price` = ?",
                                            (result[i][2],)).fetchall()
                price[0] = list(price[0])
                mark[0] = list(mark[0])
                price_up[0]=list(price_up[0])
                vivod.append([id_follow, mark, price,price_up])

                i += 1
        return vivod

    # Вывод всех марок
    def show_marks(self):
        vivod = []
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `marks`").fetchall()
            for mark in result:
                vivod.append(mark)
        return vivod

    # Вывод всех цен
    def show_prices(self):
        vivod = []
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `prices`").fetchall()
            for price in result:
                vivod.append(price)
        return vivod
    
