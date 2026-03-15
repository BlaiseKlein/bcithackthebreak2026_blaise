from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input, TextArea
from textual.screen import Screen
from textual.validation import Number
from textual import on
from screens.ai import AIScreen

class ProfileScreen(Screen):
    CSS_PATH = "../css/ping.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="mainContainer"):
            with Horizontal(id="searchBar"):
                yield Input(placeholder = "Search", id="aiSearch")
                yield Button("Search", id="searchBtn")
            

            with Horizontal(id ="content"):
                    yield VerticalScroll(
                       
                    id="optionsPanel"
                    )

                    yield VerticalScroll(
                        Button("Main Menu", id="menuBtn"),
                        id="buttonsPanel"
                    )
                    
                    yield TextArea("",id ="textArea") 
            
        
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
    
    @on(Button.Pressed, "#searchBtn")
    def onSearch(self, event: Button.Pressed) -> None:
        search_value = self.query_one("#aiSearch", Input).value
        self.app.push_screen(AIScreen(initial_text=search_value))

        


