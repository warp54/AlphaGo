from discord.ext import commands
 
bot = commands.Bot(command_prefix='!')
 
@bot.event
async def on_ready():
    print('logged in as \nname: {}\n  id: {}'.format(bot.user.name, bot.user.id))
    print('='*80)
 
@bot.command(pass_context=True)
async def hello(ctx):
    for i in range(1):
        await bot.say('Здравствуйте {}'.format(ctx.message.author.name))

async def func_comeon(ctx):
    voice = bot.voice_client_in(ctx.message.server)
    if ctx.message.author.voice.voice_channel:
        if voice:
            if voice.channel != ctx.message.author.voice.voice_channel:
                print('move to channel')
                await voice.move_to(ctx.message.author.voice.voice_channel)
        else:
            print('join to channel')
            voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
    else:
        await bot.say('where are you?')
        print('stay...')
    return voice
 
@bot.command(pass_context=True)
async def comeon(ctx):
    await func_comeon(ctx)
 
@bot.command(pass_context=True)
async def play(ctx):
    voice = await func_comeon(ctx)
    player = voice.create_ffmpeg_player('music.mp3')
    player.start()

access_token = os.environ["BOT_TOKEN"]       
bot.run(access_token)
