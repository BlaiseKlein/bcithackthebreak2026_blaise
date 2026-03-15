from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Header, Footer, TextArea, Static, ProgressBar
from textual.screen import Screen
from textual import on
from src.genai_service import get_ai_bot_response

class AIScreen(Screen):
    CSS_PATH = "../css/ping.tcss"
    TITLE = "AI"
    def __init__(self, initial_text: str = ""):
        super().__init__()
        self.initial_text = initial_text

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(
                Static("Input Log"),
                TextArea(self.initial_text,id ="inputText") ,
                Static("Output Log"),
                TextArea("",id ="outputText") ,
                Button("Ask", id="aiBtn"), 
                Button("Return", id="returnBtn") 
            )
        yield Footer()

    def on_mount(self) -> None:
        if self.initial_text != "":
            self.submitPrompt()


    @on(Button.Pressed, "#aiBtn")
    def submitPrompt(self, event: Button.Pressed = None) -> None:
        inputArea = self.query_one("#inputText")
        output = get_ai_bot_response(inputArea.text)
        outputArea = self.query_one("#outputText")
        outputArea.text = output


    
    @on(Button.Pressed,"#returnBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()


    
