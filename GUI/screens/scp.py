from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Header, Footer, Input
from textual.screen import Screen
from textual import on

class SPCScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            VerticalScroll(
                Input(placeholder = "Options",),
                Input(placeholder = "Filename",),
                Input(placeholder = "Username",),
                Input(placeholder = "IP",),
                Input(placeholder = "Target Directory",),
                Input(placeholder = "Target Machine Password",)
            ),
            VerticalScroll(
                Button("Go to main Menu", id="menuBtn"),
            )
        )
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()





    