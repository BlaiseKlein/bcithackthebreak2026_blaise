from textual.app import App

from screens.sshkey import SSHKeyScreen
from screens.menu import MainMenuScreen
from screens.ping import PingScreen
from screens.scp import SPCScreen
from screens.ai import AIScreen
from screens.curl import CurlScreen
from screens.profile import ProfileScreen
class Menu(App[str]):
    CSS_PATH = "css/button.tcss"
    
    SCREENS = {
        "main": MainMenuScreen,
        "pingScreen": PingScreen,
        "aiScreen": AIScreen,
        "scpScreen": SPCScreen,
        "sshkeyScreen": SSHKeyScreen,
        "curlScreen": CurlScreen,
        "profileScreen": ProfileScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("main")

if __name__ == "__main__":
    app = Menu()
    print(app.run())
