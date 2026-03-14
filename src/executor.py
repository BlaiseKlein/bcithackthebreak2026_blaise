import subprocess
from time import sleep
from subprocess import CalledProcessError, PIPE
import signal


# Executes a command with given paremeters and prints according to a callback function
# param - command: the command to execute
# param - parameters: a list of the parameters for the command, may be empty
# param - callback: a function that takes a single string as input, called with the resulting output
def execute(command, parameters, callback, postparameters = None):
    stringOut = "Nothing happened"

    try:
        completed = subprocess.Popen([command] + parameters, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        if postparameters:
            completed.stdin.write(postparameters.encode())
        try:
            completed.wait(timeout=3)
        except subprocess.TimeoutExpired:
            out, err = completed.communicate()
            if len(err) == 0:
                callback(out.decode("utf-8"))
                stringOut = out.decode("utf-8")
            else:
                callback(err.decode("utf-8"))
                stringOut = err.decode("utf-8")
            completed.send_signal(sig=signal.SIGINT)
            return stringOut

        out, err = completed.communicate()
        if len(err) == 0:
            callback(out.decode("utf-8"))
        else:
            callback(err.decode("utf-8"))
    except CalledProcessError as e:
        callback(e.stderr.decode("utf-8"))
        return e.stderr.decode("utf-8")

    return False

# To test, change the command and parameters and run this python file
if __name__ == "__main__":
    execute("cat", [], print, "hello")