import requests
import json

def retrieve_messages(channelid):
    headers = {
        'authorization': 'NzAzMTY4MTY2NzE2NTA2MjQy.GlMZfT.71Zeo_m1R0BIpWxrAt1dGZeU6ilkYFJ3WylRsw'
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)

    jsonn = json.loads(r.text)

    for value in jsonn:
        if (value['author']['username']) == 'amoc':
            print(value['content'], '\n')

def main():
    retrieve_messages('1051059403287175198') 

if __name__ == "__main__":
    main()