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
                Button("Go to Ping Screen", id="pingBtn"),
                Button("Go to CURL Screen", id="curlBtn"),
                Button("Go to SSH Screen", id="scpBtn"),
            )
        )
        yield Footer()
    
    @on(Button.Pressed,"#pingBtn")
    def go_to_ping(self, event: Button.Pressed) -> None:
        self.app.push_screen("pingScreen")

    @on(Button.Pressed,"#scpBtn")
    def go_to_scp(self, event: Button.Pressed) -> None:
        self.app.push_screen("scpScreen")

