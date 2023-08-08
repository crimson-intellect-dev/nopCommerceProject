import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    # tutorial used the name getApplicationURK
    @staticmethod
    def get_base_url():
        return config.get("common info", "base_url")

    # tutorial used the name useremail"
    @staticmethod
    def get_username():
        return config.get("common info", "username")

    @staticmethod
    def get_password():
        return config.get("common info", "password")

