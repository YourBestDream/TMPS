class ConfigurationManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConfigurationManager, cls).__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def get_setting(self, key):
        return self.__instance.settings.get(key, None)

    def set_setting(self, key, value):
        self.__instance.settings[key] = value
