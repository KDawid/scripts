import json


class ConfigReader:
    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as config_file:
            self.CONFIG = json.load(config_file)

    def get_chrome_driver_path(self):
        return self.CONFIG["chromeDriverPath"]

    def get_pickle_file(self):
        return self.CONFIG["pickleFile"]

    def get_credentials_file(self):
        return self.CONFIG["credentialsFile"]

    def get_imax_url(self):
        return self.CONFIG["imaxUrl"] % self.CONFIG["premierDate"]

    def get_user_id(self):
        return self.CONFIG["userId"]

    def get_user_email(self):
        return self.CONFIG["userEmail"]

    def get_recipients(self):
        return self.CONFIG["recipients"]

    def get_movie_title(self):
        return self.CONFIG["movieTitle"].lower().strip()

    def get_premier_date(self):
        return self.CONFIG["premierDate"]

    def get_subject(self):
        return self.CONFIG["subject"]

    def get_body_text(self):
        return self.CONFIG["bodyText"]

    def get_html_body(self):
        return self.CONFIG["htmlBody"]
