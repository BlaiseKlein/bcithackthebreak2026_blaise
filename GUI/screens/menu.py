from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Header, Footer
from textual.screen import Screen
from textual import on

class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            VerticalScroll(
                Static("MAIN MENU", classes="header"),
                Button("Go to IP Screen", id="ipBtn"),
                Button("Go to CURL Screen", id="curlBtn"),
                Button("Go to SSH Screen", id="sshBtn"),
            )
        )
        yield Footer()
    
    @on(Button.Pressed,"#ipBtn")
    def go_to_ip(self, event: Button.Pressed) -> None:
        self.app.push_screen("ipScreen")

