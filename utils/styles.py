from colorama import Fore, Back, Style

class TextStyles:
    def __init__(self, nocolor):
        self.nocolor = nocolor
        if nocolor:
            self.TITLE = ""
            self.SETTING = ""
        else:
            self.TITLE = Fore.BLACK + Back.WHITE
            self.SETTING = Fore.CYAN + Style.BRIGHT
