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
                        ("Port", 0),
                        ("Limit Bandwidth", 1),
                        ("Compress Data", 2),
                        ("Copy Subdirectories", 3),
                        ("Verbose", 4),
                        ("Private Key", 5),
                        id="optionId"
                ),
                Input(placeholder = "Filename",),
                Input(placeholder = "Username",),
                Input(placeholder = "IP",),
                Input(placeholder = "Target Directory",),
                Input(placeholder = "Target Machine Password",),
                Input(placeholder = "Port", disabled=True, id="portId"),
                Input(placeholder = "Bandwidth Limit", disabled=True, id="bandwidthId"),
                Input(placeholder = "Private Key", disabled=True, id="privateKeyId")

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

    @on(SelectionList.SelectedChanged, "#optionId")
    def onListChanged(self, event: SelectionList.SelectedChanged) ->None:
        selectionList = self.query_one("#optionId", SelectionList)
        selectedIndices = selectionList.selected
        self.query_one("#portId").disabled = 0 not in selectedIndices
        self.query_one("#bandwidthId").disabled = 1 not in selectedIndices
        self.query_one("#privateKeyId").disabled = 5 not in selectedIndices
            









    