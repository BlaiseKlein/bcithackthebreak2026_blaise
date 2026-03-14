from .cmd_abc import Command

# TODO: Incomplete, will fail if tested. Finish implementation after executor is updated to take password
class CommandSCP(Command):

    def __init__(self):
        self.r = False
        self.p = True
        self.i = False
        self.c = False
        self.v = False
        self.l = False

        # self.recursive_copy = False
        self.port = 8000
        self.authenticate_with_private_key = "~/temp/pwd.txt"
        # self.compress = False
        # self.verbose = False
        self.limit_bandwidth = 1000

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


        if self.r:
            cmd.append("-r")
        
        if self.p:
            cmd.append(f"-P {self.port}")

        if self.i:
            cmd.append(f"-i {self.authenticate_with_private_key}")
        
        if self.c:
            cmd.append("-C")
        
        if self.v:
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

    # def run_cmd(self):
    #     cmd = self.build_cmd()
    #     execute("scp", cmd, print)
    

if __name__ == "__main__":
   scp = CommandSCP() 
   CommandSCP.run_cmd(scp, "scp")