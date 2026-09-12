from pickle import INT
import subprocess
import re
import sys

#Configuration
#Hotspot variables
INTERFACE = 'wlp0s20f3'
SSID = 'must go'
PASSWORD = '00000000'

def get_active_channel():
    """Get the active channel of the Wi-Fi interface."""
    try:
        # subprocess.run executes  the 'iw' command to get the wifi details
        # capture_output=True to capture the output so that python can read it
        result = subprocess.run(
            ['iw','dev', INTERFACE, 'info'],
            capture_output=True, text=True, check=True
        )

        #Regular Expression(re) used to search the output for the word 'channel' followed by a channel number d+
        match = re.search(r'channel\s+(\d+)', result.stdout)

        if match:
            #match.group(1) returns the channel number found in the output
            return match.group(1)
        else:
            print('Error: Could not find the active channel. Are you connected to a Wi-Fi network?')
            sys.exit(1) # Stop the program with an error code

    except subprocess.CalledProcessError:
        print(f"Error: Could not read {INTERFACE}. Is the interface name correct?")
        sys.exit(1) # Stop the program with an error code

def start_hotspot(channel):
    """Execute the create_ap command with the discovered channel."""
    print(f"Starting hotspot {SSID} on channel {channel}...")

    # This list contains the command with spaces broken into items
    command = [
        'sudo', 'create_ap', '-c', channel,
        INTERFACE, INTERFACE, SSID, PASSWORD
    ]

    try:
        #we print the logs directly to the terminal for monitoring
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print('\nHotspot encountered an error and was stopped')
    except KeyboardInterrupt:
        #This handles when we use ctrl+c to stop the hotspot
        print('\nHotspot stopped by user')

if __name__ == '__main__':
    current_channel = get_active_channel()
    start_hotspot(current_channel)
