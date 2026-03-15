from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input, TextArea, Static
from textual.screen import Screen
from textual.validation import Number
from textual import on
from screens.ai import AIScreen
from src.commands.cmd_ping import CommandPing

class PingScreen(Screen):
    CSS_PATH = "../css/ping.tcss"
    TITLE = "PING"

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="mainContainer"):
            with Horizontal(id="searchBar"):
                yield Input(placeholder = "Search", id="aiSearch")
                yield Button("Search", id="searchBtn")
            

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
                        id="optionsPanel"
                    )

                    yield VerticalScroll(
                        Button("Main Menu", id="menuBtn"),
                        Button("Submit", id="submitBtn"),
                        Static("WARNING\nCommands May Take Time to Load", id ="warning"),
                        id="buttonsPanel"
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
    async def onSubmit(self, event: Button.Pressed)-> None:
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
        
        ping = CommandPing()

        ping.parse(inputValues)

        outputText = ""

        try:
            ping.validate_params()
            outputText = await ping.run_cmd()
        except ValueError as e:
            outputText = str(e)

        textArea = self.query_one("#textArea", TextArea)
        textArea.text = outputText

    @on(Button.Pressed, "#searchBtn")
    def onSearch(self, event: Button.Pressed) -> None:
        search_value = self.query_one("#aiSearch", Input).value
        self.app.push_screen(AIScreen(initial_text=search_value))