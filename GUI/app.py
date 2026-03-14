from textual.app import App
from screens.menu import MainMenuScreen
from screens.ip import IPScreen
class Menu(App[str]):
    CSS_PATH = "css/button.tcss"
    
    SCREENS = {
        "main": MainMenuScreen,
        "ip_screen": IPScreen,
        # "curl_screen": CURLScreen(),
        # "ssh_screen": SSHScreen(),
    }

    def on_mount(self) -> None:
        self.push_screen("main")

if __name__ == "__main__":
    app = Menu()
    print(app.run())
