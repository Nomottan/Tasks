import time

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for nick in self.users:
            if nickname in nick:
                if nick == password:
                    self.current_user = nickname
                else:
                    print(f"Пароль не верный")

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user:
                print(f"Пользователь {nickname} уже зарегестрирован")
                return
        nickname = User(nickname, password, age)
        self.users.append(nickname)
        self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for Video in args:
            if Video not in self.videos:
                self.videos.append(Video)
            else:
                print(f"Смените название ролика '{Video}' для добавления")

    def get_videos(self, title):
        my_lyst = []
        for Video in self.videos:
            if title in Video:
                my_lyst.append(str(Video))
        return my_lyst

    def watch_video(self, title):
        if self.current_user != None:
            for Video in self.videos:
                if Video == title:
                    if Video.adult_mode and self.current_user <= 18:
                            print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                            break
                    for sec in range(0, len(Video)):
                        print(sec)
                        time.sleep(1)
                    print('Конец видео')
                    break
        else:
            print(f'Войдите в аккаунт, чтобы смотреть видео')



class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __len__(self):
        return self.duration

    def __contains__(self, title):
        return title.lower() in self.title.lower()

    def __eq__(self, other):
        return self.title == other


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.password == hash(other)

    def __le__(self, other):
        return self.age <= other

    def __contains__(self, nickname):
        return nickname == self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
