import telepot
import feedparser
import time
from settings import bot, refresh_time, start_msg, stop_msg, client_file

feed_url_1 = "https://feeds.feedburner.com/ndtvsports-latest"


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    chat_id = msg['chat']['id']
    command_input = msg['text']
    # get news from RSS
    if command_input == '/News':
        bot.sendMessage(chat_id, start_msg)
        registerClientID(chat_id)
        feed = feedparser.parse(feed_url_1)

        msg = feed.entries[0].title + '\n' + feed.entries[0].link
        bot.sendMessage(chat_id, msg)	   
	# stop the bot
    if command_input == '/stop':
        bot.sendMessage(chat_id, stop_msg)
        removeClientID(chat_id)


def update():
    while True:
        # Get last news
        try:
            feed = feedparser.parse(feed_url_1)
            last = feed.entries[0]

            # Wait for updates
            time.sleep(refresh_time)

            # Get last news and check if its new
            print("Checking news at " + time.strftime("%H:%M:%S"))
            feed = feedparser.parse(feed_url_1)
            new = feed.entries[0]

            if((new.published > last.published) and (new.link != last.link)):
                print("Something new found at " + time.strftime("%H:%M:%S"))

                msg = new.title + '\n' + new.link
                sendToAll(msg)			
				
            feed = feedparser.parse(feed_url_2)
            last = feed.entries[0]

            # Wait for updates
            time.sleep(refresh_time)

            # Get last news and check if its new
            print("Checking news at " + time.strftime("%H:%M:%S"))
            feed = feedparser.parse(feed_url_2)
            new = feed.entries[0]

            if((new.published > last.published) and (new.link != last.link)):
                print("Something new found at " + time.strftime("%H:%M:%S"))

                msg = new.title + '\n' + new.link
                sendToAll(msg)
				
				
            feed = feedparser.parse(feed_url_3)
            last = feed.entries[0]

            # Wait for updates
            time.sleep(refresh_time)

            # Get last news and check if its new
            print("Checking news at " + time.strftime("%H:%M:%S"))
            feed = feedparser.parse(feed_url_3)
            new = feed.entries[0]

            if((new.published > last.published) and (new.link != last.link)):
                print("Something new found at " + time.strftime("%H:%M:%S"))

                msg = new.title + '\n' + new.link
                sendToAll(msg)
				
				
        except:
            print("Something went wrong during update.\nConnection down?")


def sendToAll(msg):
    try:
        f = open(client_file, "r")
    except:
        return

    for client in f:
        bot.sendMessage(client, msg)


def registerClientID(chat_id):
    try:
        f = open(client_file, "r+")
    except:
        f = open(client_file, "w")
        f.write(str(chat_id) + '\n')
        return

    insert = 1

    for client in f:
        if client.replace('\n', '') == str(chat_id):
            insert = 0

    if insert:
        f.write(str(chat_id) + '\n')

    f.close()


def removeClientID(chat_id):
    try:
        f = open(client_file, "r+")
    except:
        return

    tmp = ''

    for client in f:
        if client.replace('\n', '') != str(chat_id):
            tmp = tmp + str(client)

    f.close()

    f = open(client_file, "w")
    for client in tmp:
        f.write(client)

    f.close()


# Main
print("Starting AnimeBot...")
bot.message_loop(handle)
update()
