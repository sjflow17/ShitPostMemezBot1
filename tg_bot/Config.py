from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1047796551  # my telegram ID
    OWNER_USERNAME = "SJflow_17"  # my telegram username
    API_KEY = "1762928259:AAHIB6951EGlnZ-YMGZlkMxgky-EPub_dcg"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001230732953' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [746435802]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
