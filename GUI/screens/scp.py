from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Header, Footer, Input, SelectionList,TextArea
from textual.screen import Screen
from textual import on

class SPCScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            VerticalScroll(
                SelectionList[int](
                        ("Port (-P)", 0),
                        ("Limit Bandwidth (-L)", 1),
                        ("ompression (-C)", 2),
                        ("Copy Subierctories Recursive (-r)", 3),
                        ("Verbose(-v)", 4),
                        ("Private Key(-i)", 5),
                        id="optionId"
                ),
                Input(placeholder = "Filename",id="file"),
                Input(placeholder = "Username",id="user"),
                Input(placeholder = "IP",id="ip"),
                Input(placeholder = "Target Directory",id="directory"),
                Input(placeholder = "Target Machine Password",id="passwpr"),
                Input(placeholder = "Port", disabled=True, id="portId"),
                Input(placeholder = "Bandwidth Limit", disabled=True, id="bandwidthId"),
                Input(placeholder = "Private Key", disabled=True, id="privateKeyId")

            ),
            VerticalScroll(
                Button("Go to main Menu", id="menuBtn"),
                Button("Submit", id="submitBtn"),
            ),

            TextArea("",id ="textArea")
            
        )
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def onButtonPressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

    @on(SelectionList.SelectedChanged, "#optionId")
    def onListChanged(self, event: SelectionList.SelectedChanged) ->None:
        selectionList = self.query_one("#optionId", SelectionList)
        selectedIndices = selectionList.selected
        self.query_one("#portId").disabled = 0 not in selectedIndices
        self.query_one("#bandwidthId").disabled = 1 not in selectedIndices
        self.query_one("#privateKeyId").disabled = 5 not in selectedIndices
    
    @on(Button.Pressed, "#submitBtn")
    def onSubmit(self, event: Button.Pressed)-> None:
        allOptions = [
        {"index": 0, "label": "Port"},
        {"index": 1, "label": "Bandwidth"},
        {"index": 2, "label": "Compression"},
        {"index": 3, "label": "Recursive"},
        {"index": 4, "label": "Verbose"},
        {"index": 5, "label": "Private Key"},
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
                options.append(option[""])
            
        inputValues["options"] = options
        
        inputStr = str(inputValues)

        textArea = self.query_one("#textArea", TextArea)
        textArea.text = inputStr
        
            









    