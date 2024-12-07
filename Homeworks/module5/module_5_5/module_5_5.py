import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user.nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if any(vid_in_vids.title == video.title for vid_in_vids in
                   self.videos):
                continue
            else:
                self.videos.append(video)

    def get_videos(self, search_word):
        titles = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                titles.append(video.title)
        return titles

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title == title:
                    for user in self.users:
                        if user.nickname == self.current_user:
                            if user.age < 18 and video.adult_mode == True:
                                print(
                                    "Вам нет 18 лет, пожалуйста покиньте страницу")
                            else:
                                for _ in range(video.duration):
                                    video.time_now += 1
                                    print(video.time_now, end=' ')
                                    time.sleep(0.1)
                                print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# print("Videos",ur.videos)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
# print("User1",ur.current_user)
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# print("User2",ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# print("User3",ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
