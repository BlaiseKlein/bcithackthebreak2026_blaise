from .cmd_abc import Command
from src.executor import execute
import ipaddress

class SshKeygenCommand(Command):

    def __init__(self):
        self.filename = None
        self.passphrase = None
        self.comment = False
        self.bits = False
        self.type = False

    def parse(self, ui_dict):
        self.filename = ui_dict.get("filenameId")
        self.passphrase = ui_dict.get("passphraseId")
        self.comment = ui_dict.get("commentId")
        self.bits = ui_dict.get("bitsId")
        self.type = ui_dict.get("typeId")

    def validate_params(self):
        if "/" in self.filename:
            raise TypeError("Filename must have no forward slashes")

        if self.bits is not None:
            try:
                count = int(self.bits)
            except TypeError:
                raise TypeError("Bits must be an integer input")
            if self.bits < 768 or self.bits > 2048:
                raise ValueError("Bits must be within the range of 786-2048")

    def build_cmd(self):
        cmd=[]

        if self.filename:
            cmd.append(f"-f")
            cmd.append(f"{self.filename}")

        if self.passphrase:
            cmd.append(f"-N")
            cmd.append(f"{self.passphrase}")
        else:
            cmd.append(f"-N")
            cmd.append("''")

        if self.comment:
            cmd.append(f"-C")
            cmd.append(f"{self.comment}")

        if self.bits:
            cmd.append(f"-b")
            cmd.append(f" {self.bits}")

        if self.type:
            cmd.append(f"-t")
            cmd.append(f" {self.type}")

        return cmd

    async def run_cmd(self):
        cmd = self.build_cmd()
        return cmd
        execute_return = await execute("ssh-keygen", cmd, print)
        return execute_return