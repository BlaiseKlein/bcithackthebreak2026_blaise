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
                Button("Ping", id="pingBtn"),
                Button("SCP", id="scpBtn"),
                Button("SSH Keygen", id="sshkeyBtn"),
                Button("Ai Helper", id="aiBtn"),
            )
        )
        yield Footer()

    @on(Button.Pressed,"#pingBtn")
    def go_to_ping(self, event: Button.Pressed) -> None:
        self.app.push_screen("pingScreen")

    @on(Button.Pressed,"#scpBtn")
    def go_to_scp(self, event: Button.Pressed) -> None:
        self.app.push_screen("scpScreen")

    @on(Button.Pressed, "#sshkeyBtn")
    def go_to_scp(self, event: Button.Pressed) -> None:
        self.app.push_screen("sshkeyScreen")

    @on(Button.Pressed,"#aiBtn")
    def go_to_ai(self, event: Button.Pressed) -> None:
        self.app.push_screen("aiScreen")
