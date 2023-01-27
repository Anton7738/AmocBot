from discordScrape import retrieve_messages
import time

repeat = True

while(repeat): 
    seconds = time.time()
    if(seconds % 3600 == 0):
        retrieve_messages('1051059403287175198') 
