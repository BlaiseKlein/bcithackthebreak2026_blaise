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
                Input(placeholder = "Dest IP Address"),
                SelectionList[int](
                    ("IPV4 Toggle", 0, ),
                    ("IPV6 Toggle", 1),
                    ("Audible Ping", 2),
                    ("Broadcast Toggle", 3),
                    ("Flood Toggle", 4),
                ),
                Input(placeholder = "Packet Count", validators=[Number()]),
                Input(placeholder = "Interval Seconds", validators=[Number()]),
                
            VerticalScroll(
                Button("Go to main Menu", id="menuBtn"),
                )
            )
        )
        yield Footer()

    @on(Button.Pressed,"#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
    





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
    