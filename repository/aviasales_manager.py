from config_reader import config
from utils.aviasales import AviasalesManager

aviasales_manager = AviasalesManager(config.AVIASALES_TOKEN.get_secret_value())