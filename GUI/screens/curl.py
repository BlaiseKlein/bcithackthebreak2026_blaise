from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input, TextArea, Static
from textual.screen import Screen
from textual import on
from screens.ai import AIScreen
from src.commands.cmd_curl import CommandCurl

class CurlScreen(Screen):
    CSS_PATH = "../css/ping.tcss"
    TITLE = "CURL"

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="mainContainer"):
            with Horizontal(id="searchBar"):
                yield Input(placeholder = "Search", id="aiSearch")
                yield Button("Search", id="searchBtn")
            

            with Horizontal(id ="content"):
                    yield VerticalScroll(
                        SelectionList[int](
                            ("Save File", 0, ),
                            ("Follow Redirect", 1),
                            ("HTTP Header Only", 2),
                            ("POST", 3),
                            ("Server Auth", 4),
                            id="optionId"
                        ),
                        Input(placeholder = "URL", id="urlId"),
                        Input(placeholder = "Data to send", disabled= True, id="postId"),
                        Input(placeholder = "UserName", disabled= True, id="userId"),
                        Input(placeholder = "Password", disabled= True, id="passwordId"),
                        id="optionsPanel"
                    )

                    yield VerticalScroll(
                        Button("Main Menu", id="menuBtn"),
                        Button("Submit", id="submitBtn"),
                        Static("WARNING\nCommands May Take Time to Load", id ="warning"),
                        id="buttonsPanel"
                    )
                    
                    yield TextArea("",id ="textArea", read_only=True) 
            
        
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
    
    @on(SelectionList.SelectedChanged, "#optionId")
    def onListChanged(self, event: SelectionList.SelectedChanged) ->None:
        selectionList = self.query_one("#optionId", SelectionList)
        selectedIndices = selectionList.selected
        self.query_one("#postId").disabled = 3 not in selectedIndices
        self.query_one("#userId").disabled = 4 not in selectedIndices
        self.query_one("#passwordId").disabled = 4 not in selectedIndices

    @on(Button.Pressed, "#submitBtn")
    async def onSubmit(self, event: Button.Pressed)-> None:
        allOptions = [
        {"index": 0, "label": "Save File"},
        {"index": 1, "label": "Follow Redirect"},
        {"index": 2, "label": "HTTP Header Only"},
        {"index": 3, "label": "POST"},
        {"index": 4, "label": "Server Auth"},
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
        
        curl = CommandCurl()
        curl.parse(inputValues)

        outputText = ""
        
        try:
            outputText = await curl.run_cmd()
            if "Save File" in inputValues.get("options") and len(inputValues.get("options")) == 1:
                outputText = "File Saved!"
        except ValueError as e:
            outputText = str(e)

        textArea = self.query_one("#textArea", TextArea)
        textArea.text = outputText

    @on(Button.Pressed, "#searchBtn")
    def onSearch(self, event: Button.Pressed) -> None:
        search_value = self.query_one("#aiSearch", Input).value
        self.app.push_screen(AIScreen(initial_text=search_value))
        

        


