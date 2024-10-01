import time

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for nick in self.users:
            if nickname in nick:
                if nickname.password == hash(password):
                    self.current_user = nickname
                else:
                    print(f"Пароль не верный")

    def register(self, nickname, password, age):
        if nickname not in self.users:
            nickname = User(nickname, password, age)
            self.users.append(User)
            self.current_user = nickname
        else:
            print(f"Пользователь {nickname} уже зарегестрирован")

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
        return





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
        return self.password == other
    def __le__(self, other):
        return self.age < other

    def __contains__(self, nickname):
        return nickname in self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)
