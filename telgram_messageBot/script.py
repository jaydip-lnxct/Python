from telethon import TelegramClient
import json
import time
import random
# import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events



# Remember to use your own values from my.telegram.org!
api_id = 13737490
api_hash = '60a63affd355f704f2f58f13a4143a87'
token="5171228483:AAHE5ez1zGOHYeYNGlRaMxMtyen8lX65sHY"
client = TelegramClient('new_session', api_id, api_hash)


async def main():
    # Getting information about yourself
    # me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID  921392639
    # await client.send_message(921392639, 'Hello !, Friend')
    # ...to your contacts
    # This Is to start
    # calls=['+919624744024','+917878758576','+917698527324','+917069247356','+917283945538','+919510520619','+918347662838','+919913421622','+919833394778','+918128082210','+919624037507','+918368926410','+917623040141','+919979894906','+917574914972','+919586557347','+919586533201','+918690586753','+919687910171','+919106135327','+917698282406','+918780092592','+919574546841','+919904234623','+919714422452','+919328217277','+919537247185','+919429963976','+919574671738','+917990552111','+919879828862','+919714149838','+918128721460','+918153917094','+919687841420']
    # for call in calls:
    #     await client.send_message(call, 'Hello, friend! this is again & again test message from telethon')
    # # # ...or even to any username
    # receiver = InputPeerUser('5020697870', '6458651403789478353')
    # client.send_message(receiver, "https://t.me/+8teylk-OgaAzZTYx")
    try:
        f=open("csv.json","r")
        data=json.loads(f.read())
        count=0
        for user in data:
            if user['username']!='':
                second=random.randint(180,240)
                time.sleep(second)
                count+=1
                print(count)
                #print(i['username'])
                await client.send_message(user['username'], 'https://t.me/+8teylk-OgaAzZTYx')
    except Exception as e:
        print("error occured as",e);
    #     # client.(InviteToChannelRequest(channel_username,[user['username']]))

    # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        # if message.photo:
        #     path = await message.download_media()
        #     print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())