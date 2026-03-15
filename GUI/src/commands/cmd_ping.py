from .cmd_abc import Command
from src.executor import execute
import ipaddress

class CommandPing(Command):

    def __init__(self):
        self.dest_ip = None
        self.count = None
        self.ipv4 = False
        self.ipv6 = False
        self.audible = False
        self.broadcast = False
        self.flood = False
        self.interval = None

    def parse(self, ui_dict):
        self.dest_ip = ui_dict.get('destId')
        self.ipv4 = "IPV4" in ui_dict.get('options')
        self.ipv6 = "IPV6" in ui_dict.get('options')
        self.audible = "Audible" in ui_dict.get('options')
        self.broadcast = "Broadcast" in ui_dict.get('options')
        self.flood = "Flood" in ui_dict.get('options')
        if ("Count" in ui_dict.get('options')):
            self.count = ui_dict.get('countId')
        if ("Interval" in ui_dict.get('options')):
            self.interval = ui_dict.get('intervalId')

    def validate_params(self):
        # check ip exists
        if not self.dest_ip:
            raise ValueError(f"Must have destination IP address")

        # validate ip
        try:
            ip = ipaddress.ip_address(self.dest_ip)
        except ValueError:
            raise ValueError(f"{self.dest_ip} is not a valid IP address")

        # validate both IPV4 and IPV6
        if self.ipv4 and self.ipv6:
            raise ValueError(f"Can't set both IPv4 and IPv6")

        # validate ip string version matches flag if set
        version = ip.version
        if self.ipv4 and version == 6:
            raise ValueError(f"IPv4 flag set, but {self.dest_ip} is not an IPv4 address")
        elif self.ipv6 and version == 4:
            raise ValueError(f"IPv6 flag set, but {self.dest_ip} is not an IPv6 address")

        # count validation
        if self.count is not None:

            try:
                count = int(self.count)
            except TypeError:
                raise TypeError("Count must be an integer")

            if count < 0:
                raise ValueError(f"Count must be a positive number")

            if count > 1000:
                raise ValueError(f"Count is too large, must be <= 1000")

        # interval validation
        if self.interval is not None:
            try:
                interval = float(self.interval)
            except TypeError:
                raise TypeError("Interval must be a float or integer")

            if interval < 0.2:
                raise ValueError("Interval must be greater than 0.2s")

            if interval > 60:
                raise ValueError("Interval must be less than 60s")

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
    
    async def run_cmd(self):
        cmd = self.build_cmd()
        if self.count:
            execute_return = await execute("ping", cmd, print, self.count) 
        else:
            execute_return = await execute("ping", cmd, print)
        return execute_return
    

# To test
if __name__ == "__main__":
    ping = CommandPing()
    ui_dict = {'destId':'142.251.142.206', 'countId': '20', 'intervalId': '5',
              'options':["IPV4", 'Broadcast', 'Flood','Count','Interval','Audible']}
    ping.parse(ui_dict)
    print(vars(ping))
    try:
        ping.validate_params()
    except ValueError as e:
        print(e)


   #CommandPing.run_cmd(ping)