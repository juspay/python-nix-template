import socket
import platform
import getpass
from colorama import init, Fore, Style


def main():
    # Initialize colorama for cross-platform compatibility
    init()
    print_colored_info()


def get_system_info():
    """
    Retrieve system information including hostname, username, and OS name.
    Returns a tuple containing these values.
    """
    hostname = socket.gethostname()
    username = getpass.getuser()
    os_name = platform.system()
    return hostname, username, os_name

def print_colored_info():
    """
    Print system information in different colors:
    - Hostname in red
    - Username in green
    - OS name in blue
    """
    # Get system information
    hostname, username, os_name = get_system_info()

    # Print each piece of information in a distinct color
    print(f"Hostname: {Fore.RED}{hostname}{Style.RESET_ALL}")
    print(f"Username: {Fore.GREEN}{username}{Style.RESET_ALL}")
    print(f"OS Name: {Fore.BLUE}{os_name}{Style.RESET_ALL}")
