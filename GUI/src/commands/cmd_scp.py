from .cmd_abc import Command
from src.executor import execute

# TODO: Incomplete, will fail if tested. Finish implementation after executor is updated to take password
class CommandSCP(Command):

    def __init__(self):

        # -r recursive copy enabled
        self.recursive_copy = False

        # -P specify port enabled
        self.port = None

        # -i authenticate with private key enabled
        self.authenticate_with_private_key = None

        # -C compress data enabled
        self.compress = False

        # -v verbose mode enabled
        self.verbose = False

        # -l limit bandwidth enabled
        self.limit_bandwidth = None

        # Required fields for all options:

        # Local file (directory if -r) to copy
        self.file = None

        # Target machine username
        self.target_username = None

        # Target machine host
        self.target_host = None

        # Target directory
        self.target_directory = None

        # Target machine user password
        self.target_password = None

    def parse(self, ui_dict):
        self.file = ui_dict.get('file')
        self.target_username = ui_dict.get('user')
        self.target_host = ui_dict.get('ip')
        self.target_directory = ui_dict.get('directory')
        self.target_password = ui_dict.get('passwpr')

        self.compress = "Compression" in ui_dict.get('options')
        self.verbose = "Verbose" in ui_dict.get('options')

        if ("Port" in ui_dict.get('options')):
            self.port = ui_dict.get('portId')
        if ("Bandwidth" in ui_dict.get('options')):
            self.limit_bandwidth = ui_dict.get('bandwidthId')
        if ("Private Key" in ui_dict.get('options')):
            self.authenticate_with_private_key = ui_dict.get('privateKeyId')
        

    def build_cmd(self):
        cmd = []

        if self.recursive_copy:
            cmd.append("-r")
        
        if self.port:
            cmd.append(f"-P {self.port}")

        if self.authenticate_with_private_key:
            cmd.append(f"-i {self.authenticate_with_private_key}")
        
        if self.compress:
            cmd.append("-C")
        
        if self.verbose:
            cmd.append("-v")

        if self.limit_bandwidth:
            cmd.append(f"-l {self.limit_bandwidth}")

        # Required fields for all options:

        if not all([self.file, self.target_username, self.target_host, self.target_directory]):
            return "Missing required fields!"

        cmd.append(self.file)
        
        destination = f"{self.target_username}@{self.target_host}:{self.target_directory}"
        cmd.append(destination)
        
        # TODO: pass as separate attribute for executor
        # if self.target_password:
        #     cmd.append(self.append(target_directory))
        # elif:
        #     return "Missing directory on target machine!"

        return cmd
    async def run_cmd(self):
        cmd = self.build_cmd()
        execute_return = await execute("scp", cmd, print, ["yes", self.target_password])
        if "yes/no/[fingerprint]" in execute_return:
            execute_return = await execute("scp", cmd, print, [self.target_password])
        return execute_return

# if __name__ == "__main__":
#    scp = CommandSCP()
#    CommandSCP.run_cmd(scp, "scp", scp.target_password)
   