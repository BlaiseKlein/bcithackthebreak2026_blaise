from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Header, Footer, Static
from textual.containers import Horizontal, VerticalScroll
from textual.reactive import reactive
from textual import on

class TestScreen(Screen):
    INFO = reactive(0)  # start as number

    def compose(self) -> ComposeResult:
        yield Header()
        self.info_widget = Static(str(self.INFO), id="info_widget")
        yield Horizontal(
            VerticalScroll(
                self.info_widget,
                Button("Insert new info", id="testBtn"),
                VerticalScroll(
                    Button("Go to main Menu", id="menuBtn"),
                )
            )
        )
        yield Footer()

    def watch_INFO(self, new_value: int) -> None:
        # update the Static widget whenever INFO changes
        if self.is_mounted:
            self.info_widget.update(str(new_value))

    @on(Button.Pressed, "#testBtn")
    def on_test_pressed(self, event: Button.Pressed) -> None:
        self.INFO += 1

    @on(Button.Pressed, "#menuBtn")
    def on_menu_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
