from .cmd_abc import Command
from executor import execute
import ipaddress

class CommandPing(Command):

    #!!! To be fixed once textual is linked (needs all parameters for object creation)
    def __init__(self):
        self.dest_ip = "142.251.142.206"
        self.count = 5
        self.ipv4 = True
        self.ipv6 = False
        self.audible = False
        self.broadcast = False
        self.flood = False
        self.interval = None

    def parse(self, ui_dict):
        self.dest_ip = ui_dict.get('destId')
        self.ipv4 = "IPv4" in ui_dict.get('options')
        self.ipv6 = "IPv6" in ui_dict.get('options')
        self.audible = "Audible" in ui_dict.get('options')
        self.broadcast = "Broadcast" in ui_dict.get('options')
        self.flood = "Flood" in ui_dict.get('options')
        if ("Count" in ui_dict.get('options')):
            self.count = ui_dict.get('countId')
        if ("Interval" in ui_dict.get('options')):
            self.interval = ui_dict.get('intervalId')


    def build_cmd(self):

        cmd=[]

        if self.dest_ip:
            cmd.append(self.dest_ip)
        
        if self.count:
            cmd.append(f"-c {self.count}")

        if self.ipv4:
            cmd.append("-4")
        
        if self.ipv6:
            cmd.append("-6")
        
        if self.audible:
            cmd.append("-a")

        if self.broadcast:
            cmd.append("-b")

        if self.flood:
            cmd.append("-f")
        
        if self.interval:
            cmd.append(f"-i {self.interval}")

        return cmd
    
    def run_cmd(self):
        cmd = self.build_cmd()
        execute("ping", cmd, print)
    

# To test
if __name__ == "__main__":
   ping = CommandPing() 
   CommandPing.run_cmd(ping)