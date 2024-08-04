class UserManager:
    def __init__(self):
        self.users = {}
        self.current_id = 1

    def addUser(self, name):
        user_id = self.current_id
        self.users[user_id] = name
        self.current_id += 1
        return user_id

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

def main():
    manager = UserManager()

    while True:
        print("1: Добавить пользователя")
        print("2: Получить пользователя по ID")
        print("3: Удалить пользователя по ID")
        print("4: Найти пользователей по имени")
        choice = input("Введите номер операции: ")

        if choice == '1':
            name = input("Введите имя пользователя: ")
            user_id = manager.addUser(name)
            print(f"Пользователь '{name}' добавлен с ID: {user_id}")
        elif choice == '2':
            user_id = int(input("Введите ID пользователя: "))
            user = manager.getUser(user_id)
            if user is not None:
                print(f"Пользователь с ID {user_id} имеет имя '{user}'")
            else:
                print(f"Пользователь с ID {user_id} не найден")
        elif choice == '3':
            user_id = int(input("Введите ID пользователя: "))
            if manager.deleteUser(user_id):
                print(f"Пользователь с ID {user_id} удален")
            else:
                print(f"Пользователь с ID {user_id} не найден")
                print(None)
        elif choice == '4':
            name = input("Введите имя пользователя: ")
            user_ids = manager.findUserByName(name)
            if user_ids:
                print(f"Пользователи с именем '{name}': {user_ids}")
                print(user_ids)
            else:
                print(f"Пользователи с именем '{name}' не найдены")
                print([])
        else:
            print("Недопустимый выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()