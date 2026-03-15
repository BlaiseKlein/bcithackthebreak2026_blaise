from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll, Center
from textual.widgets import Button, Static, Header, Footer
from textual.screen import Screen
from textual import on

class MainMenuScreen(Screen):
    CSS_PATH = "../css/menu.tcss"
    TITLE = "Main Menu"
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Static("NETWORK TOOLS", classes="app-title")
        yield Horizontal(
            VerticalScroll(
                Static("SELECT A TOOL", classes="section-header"),
                Button("Ping", id="pingBtn"),
                Button("SCP", id="scpBtn"),
                Button("Curl", id="curlBtn"),
                Button("Profile", id="profileBtn"),
                Button("AI Helper", id="aiBtn"),
                classes="menu-panel"
            ),
            classes="menu-container"
        )
        yield Footer()
    
    @on(Button.Pressed,"#pingBtn")
    def go_to_ping(self, event: Button.Pressed) -> None:
        self.app.push_screen("pingScreen")

    @on(Button.Pressed,"#scpBtn")
    def go_to_scp(self, event: Button.Pressed) -> None:
        self.app.push_screen("scpScreen")

    @on(Button.Pressed,"#aiBtn")
    def go_to_ai(self, event: Button.Pressed) -> None:
        self.app.push_screen("aiScreen")

    @on(Button.Pressed,"#curlBtn")
    def go_to_curl(self, event: Button.Pressed) -> None:
        self.app.push_screen("curlScreen")

    @on(Button.Pressed,"#profileBtn")
    def go_to_profile(self, event: Button.Pressed) -> None:
        self.app.push_screen("profileScreen")
