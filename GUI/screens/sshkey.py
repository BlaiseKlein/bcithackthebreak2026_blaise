from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, SelectionList, Header, Footer, Input, Select, RadioButton
from textual.screen import Screen
from textual.validation import Number
from textual import on


class SSHKeyScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        options = [("rsa1", 1), ("rsa", 2), ("dsa", 3)]
        yield Horizontal(
            VerticalScroll(
                Input(placeholder="Filename",  id="filenameId"),
                Input(placeholder="Passphrase", id="passphraseId"),
                Input(placeholder="Comment", id="commentId"),
                Input(placeholder="Bits (Between 768 and 2048)", validators=[Number()], id="bitsId"),
                Select(options, prompt="Select key type", tooltip="Specifies the type of key to create. The possible values are ''rsa1'' for protocol version 1 and ''rsa'' or ''dsa'' for protocol version 2.", id="typeId"),
                RadioButton("Change Passphrase", id="changePassphraseId"),
                Input(placeholder="Old Passphrase", disabled=True, id="oldpassphraseId"),
                VerticalScroll(
                    Button("Go to main Menu", id="menuBtn"),
                )
            )
        )
        yield Footer()

    @on(Button.Pressed, "#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

    @on(RadioButton.Changed, "#changePassphraseId")
    def on_radio_button_changed(self, event: RadioButton.Changed) -> None:
        button = self.query_one("#changePassphraseId", RadioButton)
        isSelected = button.value
        self.query_one("#oldpassphraseId").disabled = not isSelected