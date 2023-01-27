import requests
import json
# Testing for later
import doctest
import unittest

# Maybe a global variable with the data?

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
    # ------------------------------------------------------------------------------------
    # WARNING: Once code is pushed to GitHub, Discord will sign out user and request login
    #          Password will need to be reset prior to login
    #          This is to prevent unauthorized access for outside users
    # ------------------------------------------------------------------------------------
    #          Workaround: comment out authorization parameter prior to pushing
    #                      use auth code ONLY for testing session
    #                      same auth code can be reused as long as password wasn't reset
    # ------------------------------------------------------------------------------------

    headers = {
                        # insert code here
        'authorization': ''
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)

    jsonn = json.loads(r.text)

    print(jsonn)

    amocMessagesBuffer = []
    
    for value in jsonn:
        if (value['author']['username']) == 'amoc':
            amocMessagesBuffer.append(value['content'])

    #print(amocMessagesBuffer)

    # open AmocMessages.txt for appending and reading, creating file if it doesn't exist
    fd = open("AmocMessages.txt", "a+")
    
    # Go through line by line in messagesBuffer
    for x in amocMessagesBuffer:
        # Check if the current buffer message is not in AmocMessages.txt
        if not amocMessagesBuffer[x] in fd.read():
            # If not in AmocMessages.txt, append to the .txt file
            fd.write(amocMessagesBuffer[x] + "\n")
    # close

    fd.close()

    """
    Before:
    <message 1>
    <message 2>

    After:
    [<message 1>, <message2>]
    """

    # some code added after using and emptying auth code

def main():
    retrieve_messages('1051059403287175198') 

if __name__ == "__main__":
    main()
