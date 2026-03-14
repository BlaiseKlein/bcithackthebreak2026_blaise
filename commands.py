def cmd_whoami():
    command = "whoami"
    # call Blaise's fork/exec function here

def cmd_id():
    command="id"
    # call Blaise's fork/exec function here

def cmd_groups():
    command="groups"
    # call Blaise's fork/exec function here

COMMANDS = {
    "whoami": cmd_whoami,
    "id": cmd_id,
    "groups": cmd_groups
}

def get_user_info():
    command_input = input("What user account detail do you want? (whoami/id/groups) ").strip()
    COMMANDS.get(command_input, lambda:print("Unknown command, try again"))()
