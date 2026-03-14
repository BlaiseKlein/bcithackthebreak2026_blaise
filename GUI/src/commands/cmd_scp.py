from .cmd_abc import Command

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
        self.file = "~/temp/temp.txt"

        # Target machine username
        self.target_username = "user"

        # Target machine host
        self.target_host = "192.168.0.1"

        # Target directory
        self.target_directory = "~/temp"

        # Target machine user password
        self.target_password = "123"

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

        if self.l:
            cmd.append(f"-l {self.limit_bandwidth}")

        # Required fields for all options:

        if self.file:
            cmd.append(self.append(file))
        elif:
            return "Missing file or directory!"

        if self.target_username:
            cmd.append(self.append(target_username))
        elif:
            return "Missing username on target machine!"

        if self.target_host:
            cmd.append(self.append(target_host))
        elif:
            return "Missing hostname/IP of target machine!"

        if self.target_directory:
            cmd.append(self.append(target_directory))
        elif:
            return "Missing directory on target machine!"

        # TODO: pass as separate attribute for executor
        # if self.target_password:
        #     cmd.append(self.append(target_directory))
        # elif:
        #     return "Missing directory on target machine!"

        return cmd

if __name__ == "__main__":
   scp = CommandSCP()
   CommandSCP.run_cmd(scp, "scp", scp.target_password)
   