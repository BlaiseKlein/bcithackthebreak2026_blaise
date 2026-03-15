from .cmd_abc import Command

class CommandCurl(Command):

    def __init__(self):
        # -O save file with remote name flag enabled
        self.save_file_with_remote_name = False

        # -L follow redirects flag enabled
        self.follow_redirects = False

        # -I fetch http headers only enabled
        self.fetch_http_headers_only = False

        # -d send data with POST request enabled
        self.send_post_request = None
        self.send_post_request_data = None

        # -u server authentication enabled
        self.server_authentication = (None, None)
        user, password = self.server_authentication

        # Required fields for all options:

        # target URL
        self.url = "google.com"

    def build_cmd(self):
        cmd = []

        if self.save_file_with_remote_name:
            cmd.append("-O")
        
        if self.follow_redirects:
            cmd.append("-L")

        if self.fetch_http_headers_only:
            cmd.append("-I")
        
        if self.send_post_request and self.send_post_request_data:
            cmd.append(f"-d {self.send_post_request_data}")
        
        if self.server_authentication and user and password:
                cmd.append(f"-u {user}:{password}")

        # Required fields for all options:

        if self.url:
            cmd.append(self.append(url))
        else:
            return "Missing URL!"

        return cmd

    def run_cmd(self):
        cmd = self.build_cmd()
        execute("scp", cmd, print)
    

if __name__ == "__main__":
   curl = CommandCurl() 
   CommandSCP.run_cmd(curl, "curl")