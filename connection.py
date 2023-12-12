import socket
import argparse

def check_internet_connection(host="www.google.com", port=80, timeout=3):
    """
    Check internet connection by connecting to a host.
    If the connection is successful, return True.
    If the connection fails, return False.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex)
        return False

if __name__ == "__main__":
    # Define the command-line arguments
    argPrs = argparse.ArgumentParser(description='Check internet connection.')

    argPrs.add_argument(
        'hostP1', 
        nargs='?', 
        default='www.google.com',
        help='The host to connect to. Default is www.google.com.'
    )

    argPrs.add_argument(
        'portP2', 
        nargs='?', 
        type=int, 
        default=80,
        help='The port to connect to. Default is 80.'
    )

    argPrs.add_argument(
        'timeoutP3', 
        nargs='?', 
        type=int, 
        default=3,
        help='The timeout for the connection. Default is 3 seconds.'
    )

    argPrs.add_argument(
        '-H', 
        '--host', 
        type=str,
        help='The host to connect to. Overrides the positional host argument.'
    )

    argPrs.add_argument(
        '-P', 
        '--port', 
        type=int,
        help='The port to connect to. Overrides the positional port argument.'
    )

    argPrs.add_argument(
        '-T', 
        '--timeout', 
        type=int,
        help='The timeout for the connection. Overrides the positional timeout argument.'
    )
    
    try:
        # Attempt to parse the command-line arguments using argPrs.parse_args()
        args = argPrs.parse_args()
        
        host = args.host if args.host else args.hostP1
        port = args.port if args.port else args.portP2
        timeout = args.timeout if args.timeout else args.timeoutP3
            
    except SystemExit:
        # In case of a SystemExit exception, handle it appropriately
        print("Error: arguments unavailable.")
        host = "www.google.com"
        port = 80
        timeout = 3
        
    # Proceed with the rest of your code using the extracted arguments
    if check_internet_connection(host, port, timeout):
        print("Internet connection is available.")
    else:
        print("No internet connection.")
        