from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Header, Footer, TextArea, Static
from textual.screen import Screen
from textual import on

class AIScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(
                Static("Input Log"),
                TextArea("",id ="inputText") ,
                Static("Output Log"),
                TextArea("",id ="outputText") ,
                Button("Ask", id="aiBtn"), 
                Button("Return", id="returnBtn") 
            )
        yield Footer()

    @on(Button.Pressed, "#aiBtn")
    def submitPrompt(self, event: Button.Pressed) -> None:
        inputArea = self.query_one("#inputText")

        outputArea = self.query_one("#outputText")
    
    @on(Button.Pressed,"#returnBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()


    
