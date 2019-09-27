from config_reader import ConfigReader
from email_sender import EmailSender
from movie_watcher import MovieWatcher

import time


class MovieNotifier:
    def __init__(self):
        self.sleep_time = 60
        self.config_file_path = "config.json"
        self.config = ConfigReader(self.config_file_path)

        self.watcher = MovieWatcher(self.config)
        self.sender = EmailSender(self.config)

    def run(self):
        found_movie = False
        while not found_movie:
            if self.watcher.check_movie():
                self.sender.notify()
                found_movie = True
            else:
                print("Sleep %i seconds" % self.sleep_time)
                time.sleep(self.sleep_time)


if __name__ == '__main__':
    movie_notifier = MovieNotifier()
    movie_notifier.run()
