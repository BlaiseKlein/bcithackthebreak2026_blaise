from .cmd_abc import Command
from src.executor import execute

class CommandCurl(Command):

    def __init__(self):
        # -O save file with remote name flag enabled
        self.save_file_with_remote_name = False

        # -L follow redirects flag enabled
        self.follow_redirects = False

        # -I fetch http headers only enabled
        self.fetch_http_headers_only = False

        # -d send data with POST request enabled
        self.send_post_request = False
        self.send_post_request_data = None

        # -u server authentication enabled
        self.server_authentication = False
        self.user = None
        self.password = None

        # Required fields for all options:

        # target URL
        self.url = "google.com"

    
    def parse(self, ui_dict):
        self.url = ui_dict.get('urlId')
        self.save_file_with_remote_name = 'Save File' in ui_dict.get('options')
        self.follow_redirects = 'Follow Redirect' in ui_dict.get('options')
        self.fetch_http_headers_only = 'HTTP Header Only' in ui_dict.get('options')
        self.send_post_request = 'POST' in ui_dict.get('options')
        self.server_authentication = 'Server Auth' in ui_dict.get('options')
        if self.send_post_request:
            self.send_post_request_data = ui_dict.get('postId')
        if self.server_authentication:
            self.user = ui_dict.get('userId')
            self.password = ui_dict.get('passwordId')
        
    def build_cmd(self):
        cmd = []

        cmd.append("-s")

        if self.save_file_with_remote_name:
            cmd.append("-O")
        
        if self.follow_redirects:
            cmd.append("-L")

        if self.fetch_http_headers_only:
            cmd.append("-I")
        
        if self.send_post_request and self.send_post_request_data:
            cmd.append(f"-d {self.send_post_request_data}")
        
        if self.server_authentication and self.user and self.password:
            cmd.append(f"-u {self.user}:{self.password}")

        # Required fields for all options:

        if self.url:
            cmd.append(self.url)
        else:
            return "Missing URL!"

        return cmd

    async def run_cmd(self):
        cmd = self.build_cmd()
        return_execute = await execute("curl", cmd, print)
        return return_execute
    

if __name__ == "__main__":
   curl = CommandCurl() 
   curl.run_cmd(curl, "curl")