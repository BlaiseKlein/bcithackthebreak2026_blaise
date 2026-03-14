from textual import App
from screens.menu import MainMenuScreen
from screens.ping import PingScreen
from screens.scp import SPCScreen
class Menu(App[str]):
    CSS_PATH = "css/button.tcss"
    
    SCREENS = {
        "main": MainMenuScreen,
        "pingScreen": PingScreen,
        # "curl_screen": CURLScreen,
        "scpScreen": SPCScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("main")

if __name__ == "__main__":
    app = Menu()
    print(app.run())
