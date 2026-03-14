from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Header, Footer, Input, SelectionList
from textual.screen import Screen
from textual import on

class SPCScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            VerticalScroll(
                SelectionList[int](
                    [
                        ("-r", 0),
                        ("IPV6 Toggle", 1),
                        ("Audible Ping", 2),
                        ("Broadcast Toggle", 3),
                        ("Flood Toggle", 4),
                    ],
                    id="optionID"
                ),
                Input(placeholder = "Filename",),
                Input(placeholder = "Username",),
                Input(placeholder = "IP",),
                Input(placeholder = "Target Directory",),
                Input(placeholder = "Target Machine Password",)
            ),
            VerticalScroll(
                Button("Go to main Menu", id="menuBtn"),
                Button("Start", id="startBtn"),
            )
        )
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

    @on(Button.Pressed, "startBtn")
    def onStartPressed(self, event: Button.Pressed) ->None:
        selectionList = self.query_one("#optionID", SelectionList)





    