from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input
from textual.screen import Screen
from textual.validation import Number
from textual import on

class PingScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            VerticalScroll(
                SelectionList[int](
                    ("IPV4 Toggle", 0, ),
                    ("IPV6 Toggle", 1),
                    ("Audible Ping", 2),
                    ("Broadcast Toggle", 3),
                    ("Flood Toggle", 4),
                    ("Count", 5),
                    ("Interval", 6),
                    id="optionId"
                ),
                Input(placeholder = "Dest IP Address"),
                Input(placeholder = "Packet Count", validators=[Number()], disabled= True, id="countId"),
                Input(placeholder = "Interval", validators=[Number()], disabled= True, id="intervalId"),

            VerticalScroll(
                Button("Go to main Menu", id="menuBtn"),
                )
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
        self.query_one("#countId").disabled = 5 not in selectedIndices
        self.query_one("#intervalId").disabled = 6 not in selectedIndices





# class IPAddressValid(Validator):
#         def validate(self, value:str)->ValidationResult:
#             if self.isIpAddr(value):
#                 return self.success()
#             else:
#                 return self.failure("Is not a IP addr")

#         def isIpAddr(self, ip: str) -> bool:
#             try:
#                 ipaddress.ip_address(ip)
#                 return True
#             except ValueError:
#                 return False
    