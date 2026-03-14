import subprocess
from subprocess import CalledProcessError

# Executes a command with given paremeters and prints according to a callback function
# param - command: the command to execute
# param - parameters: a list of the parameters for the command, may be empty
# param - callback: a function that takes a single string as input, called with the resulting output
def execute(command, parameters, callback):
    try:
        completed = subprocess.run([command] + parameters, capture_output=True, check=True)

        callback(completed.stdout.decode("utf-8"))
    except CalledProcessError as e:
        callback(e.stderr.decode("utf-8"))

    return False

# To test, change the command and parameters and run this python file
if __name__ == "__main__":
    execute("ls", ["-l", "-7"], print)