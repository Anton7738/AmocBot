import requests
import json

def retrieve_messages(channelid):
    """
    Authorization code will need to be changed before local usage
    Step 1: Navigate to Discord's web client
    Step 2: Locate channel and open dev tools (ctrl + shift + i)
    Step 3: In dev tools, find "Network" tab
    Step 4: Refresh page
    Step 5: Type into the text box of channel
    Step 6: Under "Name" tab on lower left, scroll down and click on "typing"
    Step 7: Find "Headers" tab on right side of dev tools pane
    Step 8: Scroll down to "Request Headers" > "authorization"
    Step 9: Copy and paste code into parameter below
    """ 
    # WARNING: After usage, Discord may log you out as connection may be "unstable"

    headers = {
                        # insert code here
        'authorization': 'NzAzMTY4MTY2NzE2NTA2MjQy.GkXbVh.UsYAD3i5hA72qpiEwfdDaNFvrGDGSCyGZ8F4EU'
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)

    jsonn = json.loads(r.text)

    print(jsonn)

    for value in jsonn:
        if (value['author']['username']) == 'amoc':
            print(value['content'], '\n')

def main():
    retrieve_messages('1051059403287175198') 

if __name__ == "__main__":
    main()