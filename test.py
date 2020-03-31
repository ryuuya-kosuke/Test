import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がbotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます、" + message.author.name + "さん！"
            await message.channel.send(m)

client.run("Njk0MzgyNDAwMTg0MjU0NTE0.XoOVdg.RZ3fl8OG5l54tV31guvNXfmY9BU")
