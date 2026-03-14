from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input, TextArea
from textual.screen import Screen
from textual.validation import Number
from textual import on
# from src.commands import cmd_ping

class PingScreen(Screen):
    CSS_PATH = "../css/ping.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="mainContainer"):
            with Horizontal(id="searchBar"):
                yield Input(placeholder = "Search", id="aiSearch")
            

            with Horizontal(id ="content"):
                    yield VerticalScroll(
                        SelectionList[int](
                            ("IPV4 Toggle", 0, ),
                            ("IPV6 Toggle", 1),
                            ("Broadcast Toggle", 2),
                            ("Flood Toggle", 3),
                            ("Count", 4),
                            ("Interval", 5),
                            ("Audible", 6),
                            id="optionId"
                        ),
                        Input(placeholder = "Dest IP Address", id="destId"),
                        Input(placeholder = "Packet Count", validators=[Number()], disabled= True, id="countId"),
                        Input(placeholder = "Interval", validators=[Number()], disabled= True, id="intervalId"),
                    )

                    yield VerticalScroll(
                        Button("Search", id="searchBtn"),
                        Button("Main Menu", id="menuBtn"),
                        Button("Submit", id="submitBtn"),
                    )
                    
                    yield TextArea("",id ="textArea") 
            
        
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
    
    @on(SelectionList.SelectedChanged, "#optionId")
    def onListChanged(self, event: SelectionList.SelectedChanged) ->None:
        selectionList = self.query_one("#optionId", SelectionList)
        selectedIndices = selectionList.selected
        self.query_one("#countId").disabled = 4 not in selectedIndices
        self.query_one("#intervalId").disabled = 5 not in selectedIndices

    @on(Button.Pressed, "#submitBtn")
    def onSubmit(self, event: Button.Pressed)-> None:
        allOptions = [
        {"index": 0, "label": "IPV4"},
        {"index": 1, "label": "IPV6"},
        {"index": 2, "label": "Broadcast"},
        {"index": 3, "label": "Flood"},
        {"index": 4, "label": "Count"},
        {"index": 5, "label": "Interval"},
        {"index": 6, "label": "Audible"},
        ]

        inputValues = {
            input.id: input.value 
            for input in self.query(Input)
            if input.value
        }

        selectedOptions = self.query_one("#optionId", SelectionList).selected 

        options = []   
        for option in allOptions:
            if option["index"] in selectedOptions:
                options.append(option["label"])
            
        inputValues["options"] = options
        
        inputStr = str(inputValues)

        textArea = self.query_one("#textArea", TextArea)
        textArea.text = inputStr

    @on(Button.Pressed, "#searchBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.push_screen("aiScreen")

        


