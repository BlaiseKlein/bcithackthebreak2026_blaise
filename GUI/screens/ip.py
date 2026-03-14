from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Header, Footer, Input
from textual.validation import ValidationResult, Validator
from textual.screen import Screen
import ipaddress
from textual import on

class IPScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Input(placeholder = "IP Address",
                    validators=[

                    ]
                    )
        yield Horizontal(
            VerticalScroll(
                Static("IP", classes="header"),
                Button("Go to main Menu", id="ipScreenBtn"),
            )
        )
        yield Footer()

    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ipScreenBtn":
            self.app.pop_screen()

    class IPAddressValid(Validator):
        def validate(self, str)->ValidationResult:
            if self.isIpAddr(str):
                return self.success
            else:
                return self.failure("Is not a IP addr")

        def isIpAddr(ip: str) -> bool:
            try:
                ipaddress.ip_address(ip)
                return True
            except ValueError:
                return False
       