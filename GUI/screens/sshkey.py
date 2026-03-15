from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, TextArea, Header, Footer, Input, Select, RadioButton
from textual.screen import Screen
from textual.validation import Number
from textual import on
from screens.ai import AIScreen
from src.commands.cmd_sshkey import SshKeygenCommand

class SSHKeyScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        options = [("rsa1", "rsa1"), ("rsa", "rsa"), ("dsa", "dsa")]
        with VerticalScroll(id="mainContainer"):
            with Horizontal(id="searchBar"):
                yield Input(placeholder="Search", id="aiSearch")
            with Horizontal(id="content"):
                yield VerticalScroll(
                    Input(placeholder="Filename",  id="filenameId"),
                    Input(placeholder="Passphrase", id="passphraseId"),
                    Input(placeholder="Comment", id="commentId"),
                    Input(placeholder="Bits (Between 768 and 2048)", validators=[Number()], id="bitsId"),
                    Select(options, prompt="Select key type", tooltip="Specifies the type of key to create. The possible values are ''rsa1'' for protocol version 1 and ''rsa'' or ''dsa'' for protocol version 2.", id="typeId"),
                    # RadioButton("Change Passphrase", id="changePassphraseId"),
                    # Input(placeholder="Old Passphrase", disabled=True, id="oldpassphraseId"),
                    VerticalScroll(
                        Button("Go to main Menu", id="menuBtn"),
                    )
                )
                yield VerticalScroll(
                    Button("Search", id="searchBtn"),
                    Button("Main Menu", id="menuBtn"),
                    Button("Submit", id="submitBtn"),
                )
                yield TextArea("", id="textArea")


        yield Footer()

    @on(Button.Pressed, "#menuBtn")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

    @on(Button.Pressed, "#submitBtn")
    async def onSubmit(self, event: Button.Pressed) -> None:

        inputValues = {
            input.id: input.value
            for input in self.query(Input)
            if input.value
        }

        selectedOptions = self.query_one("#typeId", Select).value

        if selectedOptions != False:
            inputValues["options"] = {"typeId": selectedOptions}


        ping = SshKeygenCommand()

        ping.parse(inputValues)

        outputText = ""

        try:
            ping.validate_params()
            outputText = await ping.run_cmd()
        except ValueError as e:
            outputText = e

        textArea = self.query_one("#textArea", TextArea)
        textArea.text = outputText

    @on(Button.Pressed, "#searchBtn")
    def onSearch(self, event: Button.Pressed) -> None:
        search_value = self.query_one("#aiSearch", Input).value
        self.app.push_screen(AIScreen(initial_text=search_value))

    # @on(RadioButton.Changed, "#changePassphraseId")
    # def on_radio_button_changed(self, event: RadioButton.Changed) -> None:
    #     button = self.query_one("#changePassphraseId", RadioButton)
    #     isSelected = button.value
    #     self.query_one("#oldpassphraseId").disabled = not isSelected