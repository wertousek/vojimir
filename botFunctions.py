import discord


commandPrefix = None

def embed(title, url = None, description = None, fields = None, image = None, thumbnail = None, author =  None):
    e = discord.Embed.from_dict({
            "title": title,
            "color": 2480439,
            "description": description,
            "image": image,
            "thumbnail": thumbnail,
            "author": author,
            "fields": fields,
            "url": url,
            "footer": {
                "text": "Powered by Bertik23",
                "icon_url": "https://cdn.discordapp.com/avatars/452478521755828224/4cfdbde44582fe6ad05383171ac1b051.png"
                }
            }
        )
    return e

def command(message):
    if len(message) != 0:
        if message[0] == commandPrefix:
            if len(message[1:].split(" ", 1)) == 1:
                return message[1:], None
            else:
                return message[1:].split(" ", 1)[0], message[1:].split(" ",1)[1]
        else:
            return None, None
    else:
        return None, None