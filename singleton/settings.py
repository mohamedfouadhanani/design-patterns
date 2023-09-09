class Settings:
    instance: "Settings" = None

    def __new__(cls, is_darktheme: bool, is_full_screen: bool, language: str = "EN") -> "Settings":
        if Settings.instance is None:
            instance = super().__new__(cls)

            instance.is_darktheme = is_darktheme
            instance.is_full_screen = is_full_screen
            instance.language = language

            Settings.instance = instance

        return Settings.instance
