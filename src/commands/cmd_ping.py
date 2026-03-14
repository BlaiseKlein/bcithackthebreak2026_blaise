from commands.cmd_abc import Command

class CommandPing(Command):

    #!!! To be fixed once textual is linked
    def __init__(self, dest_ip, count, ipv4, ipv6, audible, broadcast, packet_count, flood, interval):
        self.dest_ip = None
        self.count = None
        self.ipv4 = True
        self.ipv6 = False
        self.audible = False
        self.broadcast = False
        self.packet_count = None
        self.flood = False
        self.interval = None

    def build_cmd(self):
        cmd = ["ping"]

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

        if self.broacast:
            cmd.append("-b")
        
        if self.packet_count:
            cmd.append(f"-s {self.packet_count}")

        if self.flood:
            cmd.append("-f")
        
        if self.interval:
            cmd.append(f"-i {self.interval}")
        
    
