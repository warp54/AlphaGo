import asyncio
import discord
import datetime
import time
import random
import urllib.request
import urllib
import bs4
import sys
import json
from selenium import webdriver
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import os
import re

app = discord.Client()

token = "NjE1ODk4Mjk5MTY1MzExMDAz.XWU-ow.g16WsXR09JOoJ4eWgJXcgtrHfOI"
now = datetime.datetime.now()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("===========")
    await app.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))


@app.event
async def on_message(message: object):
    if message.author.bot:
        return None

    if message.content.startswith("!메이드"):
        all_image_choices = ["https://img.licilici.com/2019/08/24/5d6131c2b3654.jpg", 
                             "https://img.licilici.com/2019/08/24/5d6131c2e608c.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c2e834e.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c2e5178.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c2e765f.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c33ee45.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c3c3033.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c3c2ee4.jpg",
                             "https://img.licilici.com/2019/08/24/5d6131c3c375e.jpg"
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fkucuk1j32tc480u13.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fm1h61cj32tc480b2f.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fl2iw0dj32tc480b2f.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fl9228hj32tc480he0.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fljwhfrj32tc480nph.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fmcz270j32tc480b2f.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fltuypcj32tc480npj.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66fkkfog2j32tc4804qw.jpg",
                             "https://ww4.sinaimg.cn/bmiddle/006UMJL9gy1g66flevit2j32tc480hdy.jpg"]
        chosen_image = random.choice(all_image_choices)
        e = discord.Embed(title="", description="")
        e.set_image(url=chosen_image)
        await app.send_message (message.channel, embed = e)       

    if message.content.startswith("!이스터"):
        all_image_choices = ["https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_ZbWnu8OR_6e380801c1b845c53010ff7d1f55e7fdf63fcb8a.gif",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_nOqw6zdl_fd4f007398fb5ea8cfb459f84d00998d70519751.gif",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_rHXgm48F_d05f136ff2bafbb8d4110f830da37cabd8333960.gif",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_TenVFRLa_c761af52e025a5b0361858558b1da6d6b2ba9280.gif",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_iKonWdcZ_fa5f30c197066f9fea4ef387b95f75558c0f2668.gif",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_ySPJNRsa_97984120c78d3fea49705b72fc68494c35342633.jpg",
                             "https://hellven.net/data/file/realdada/27d5e3ff84fad478e2201f5aff21d4ddb3655c0c_hvTIP0aJ_12312b969548acd85a4d911a2aa6674adcdf1fdd.jpg"]
        chosen_image = random.choice(all_image_choices)
        e = discord.Embed(title="", description="")
        e.set_image(url=chosen_image)
        await app.send_message (message.channel, embed = e)      

    if message.content.startswith("!뇨호"):
        all_image_choices = ["https://external-preview.redd.it/FwJyC6bwyNZPhqX4fHQ_StFxhY6kzr-2zPnoLDdEdG4.jpg?auto=webp&s=e21246dba0eeab56b0487e0a6c449ae1f53e9ae4",
                             "https://preview.redd.it/f2fipdpik2j31.jpg?width=640&crop=smart&auto=webp&s=06775245e7cf9f573b61297127c82055e81c5b99",
                             "https://preview.redd.it/3cchxnsl62j31.jpg?width=640&crop=smart&auto=webp&s=5f5775fc089bd22f8ec16356f68e3e9fe000de48",
                             "https://i.redd.it/m9l2w8fae0j31.jpg",
                             "https://preview.redd.it/u059z7p4pui31.jpg?width=640&crop=smart&auto=webp&s=220b3609da0428fc47b519d537f62d410e8edf2f",
                             "https://preview.redd.it/057ojrc02vi31.jpg?width=640&crop=smart&auto=webp&s=44aca6929baac744b7c5c4ac0f2eba179395506f",
                             "https://external-preview.redd.it/zMKl0HjM68iut_ubW6pHN5wKlQdmkN7Jop5Dul-Oq3I.jpg?width=640&crop=smart&auto=webp&s=6166611592fbd48303f89fc644d60254d985ea55",
                             "https://external-preview.redd.it/PgJ1lvTDhQkiIUn66rf3bJYBKcSTGLaPAMLEYguFwaw.jpg?auto=webp&s=a4702ca5f0828cccaaa52306c747df2f13b303b7",
                             "https://preview.redd.it/c7p6fzpw2aj31.jpg?width=640&crop=smart&auto=webp&s=998c7d13de11ed0fa426e6756f03e38ab3dc6f66",
                             "https://external-preview.redd.it/ZjRXadj7BlDvDOigwCcuri1FB-fvC3disCbPPvobKxY.jpg?width=640&crop=smart&auto=webp&s=f7cb68a91db12cd444e91f266cfa3c3ca3124ff0",
                             "https://preview.redd.it/q2vl8d63x8j31.jpg?width=640&crop=smart&auto=webp&s=fd4275dbde000e4af6be8806c8d6171e93bfc752",
                             "https://preview.redd.it/mpbb0nrmg7j31.jpg?width=640&crop=smart&auto=webp&s=ccd8f6cd390d35b110141be90a87c30e1ff879b7",
                             "https://preview.redd.it/ed614128d6j31.jpg?width=640&crop=smart&auto=webp&s=e6dc96d423cf5da99fa7d69c4df4ade74ff79948",
                             "https://external-preview.redd.it/nKnI5xqaZUxD8-KDOz4XAHtgWRPRDTn2D4jTwovVZsU.jpg?width=640&crop=smart&auto=webp&s=0002dd268cbdfc1d383b536541bcb97c0eb3320d"]
        chosen_image = random.choice(all_image_choices)
        e = discord.Embed(title="", description="")
        e.set_image(url=chosen_image)
        await app.send_message (message.channel, embed = e)        

    if message.content.startswith("!모두모여"):
        await app.send_message(message.channel, "@everyone")

    if message.content == "!도움":
        embed = discord.Embed(title="안녕하세요!",
                              description="제 이름은 Random입니다!""\n""가능한 명령어는 !안녕, !시간, !날짜, !시계, !모두모여, !은돌이, !미야, !호야, !서새봄, !야짤, !니삭스, !메이드, !정재철, !이준석, !이재환, !이홍원, !서장준, !안현준, !이세진, !신영재, !고양이""\n""일부 명령어는 언제든 삭제될 수 있습니다.",
                              color=0x00ff00)
        embed.set_footer(
            text=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(
                now.minute) + ":" + str(now.second))
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith("!도움"):
        await app.send_message(message.channel, "답변입니다!")

    if message.content.startswith("!안녕"):
        await app.send_message(message.channel, "안녕")

    if message.content.startswith("아무도 없어?"):
        await app.send_message(message.channel, "괜찮아요 저는 여기 있어요!")

    if message.content == "!날짜":
        embed = discord.Embed(title="", description="", color=0x00ff00)
        embed.set_footer(text="%s년%s월%s일" % (now.year, now.month, now.day,))
        await app.send_message(message.channel, embed=embed)

    if message.content == "!시간":
        embed = discord.Embed(title="", description="", color=0x00ff00)
        embed.set_footer(
            text=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(
                now.minute) + ":" + str(now.second))
        await app.send_message(message.channel, embed=embed)

    if message.content == "!시계":
        embed = discord.Embed(title="", description="", color=0x00ff00)
        embed.set_footer(text=str(now))
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!은돌이'):
        embed = discord.Embed(title='은돌이는', description='후욱후욱', color=0x00ff00)
        embed.set_image(url="https://i.ytimg.com/vi/GxwmAEgdkC0/maxresdefault.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!호야'):
        embed = discord.Embed(title='호야는', description='빻빻', color=0x00ff00)
        embed.set_image(url="https://static-cdn.jtvnw.net/jtv_user_pictures/83e6c53e-b9ca-4c64-823f-3ff3a8e0a493-profile_image-300x300.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!미야'):
        embed = discord.Embed(title='미야는', description='출렁출렁', color=0x00ff00)
        embed.set_image(url="https://static-cdn.jtvnw.net/jtv_user_pictures/7297eb29-8b83-4608-a607-fd30aaa3707f-profile_image-300x300.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!자야'):
        embed = discord.Embed(title='자야...', description='기다려...', color=0x00ff00)
        embed.set_image(url="https://pbs.twimg.com/media/Dd0f-bkUwAAX4Hs.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!서새봄'):
        embed = discord.Embed(title='새봄이는', description='23살!', color=0x00ff00)
        embed.set_image(url="https://4.bp.blogspot.com/-TFXhJBAYiJM/XOTT9oBa5bI/AAAAAAAAfqU/S96211xdkFk-cm1htPtsiD6lOBzTw3pLACLcBGAs/s1600/1558438645.gif")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!야짤'):
        embed = discord.Embed(title='미치셨습니까', description='휴먼?', color=0x00ff00)
        embed.set_image(url="https://4.bp.blogspot.com/-Y8-bXwDP77c/XDtNryCCr2I/AAAAAAAAApM/cU1TFHVH3oQJI22ncvlhT4sY8mykHd6KQCLcBGAs/s1600/i13228430523.gif")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!니삭스'):
        embed = discord.Embed(title='니삭스가 취향인가요?', description='저두요', color=0x00ff00)
        embed.set_image(url="https://img.sonyunara.com/files/goods/45681/1544084667_0.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content == "!제작자":
        await app.send_message(message.channel, "제작자는 파이썬이라곤 배워본 적도 없는 컴맹입니다! 이걸 만든 것도 기적이죠!")

    if message.content == "!레식":
        await app.send_message(message.channel, "갓겜인데 모두들 다같이 해요!")

    if message.content == "!ssd":
        await app.send_message(message.channel, "SSD보다는 HDD죠!")

    if message.content == "!정재철":
        await app.send_message(message.channel, "으악! 더러워!")

    if message.content == "!안현준":
        await app.send_message(message.channel, "신!")

    if message.content == "!이준석":
        await app.send_message(message.channel, "한양대 에리카 재료화학공학과 최고의 아싸!")

    if message.content == "!이재환":
        await app.send_message(message.channel, "연매출 95억의 사나이!")

    if message.content == "!이홍원":
        await app.send_message(message.channel, "현재 김두령을 피해 도주중이라 부재중입니다!")

    if message.content == "!서장준":
        await app.send_message(message.channel, "랩실 노예라고 들었습니다만...")

    if message.content == "!이세진":
        await app.send_message(message.channel, "부재중시 설계실에 있습니다")

    if message.content == "!신영재":
        await app.send_message(message.channel, "하... 할많하않")

    if message.content == "hello":
        await app.send_message(message.channel, "HELLO WORLD!")

    if message.content.startswith("!복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 45)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 45)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 45)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!고양이'):
        embed = discord.Embed(
            title='고양이는',
            description='냐옹',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase + str(randomNum)
        embed.set_image(url=urlF)
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')

        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0, 3):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL), inline=False)

        await app.send_message(message.channel, embed=embed)

    if message.content.startswith("!날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip() 
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip() 
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text 
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False) 
        embed.add_field(name='현재상태', value=todayValue, inline=False) 
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False) 
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False) 



        await app.send_message(message.channel,embed=embed)

    if message.content.startswith('!이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "]

        randomNum = random.randrange(0, len(emoji))
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await app.send_message(message.channel, embed=discord.Embed(description=emoji[randomNum]))

    if message.content.startswith('!타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await app.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await app.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith("!들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = app.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await app.send_message(message.channel, '들어왔습니다')
            await app.join_voice_channel(channel)
        else:
            await app.send_message(message.channel, '봇이 이미 들어와있습니다.')

    if message.content.startswith("!케장콘"):
        all_image_choices = ["https://item.kakaocdn.net/do/44ef66e6647ca59051e85c2c27e7d3aaf43ad912ad8dd55b04db6a64cddaf76d",
                             "https://item.kakaocdn.net/do/78534b924475f19381b664557b711103f43ad912ad8dd55b04db6a64cddaf76d",
                             "https://item.kakaocdn.net/do/b76dda556c28888d8cfca99e1fba9596f43ad912ad8dd55b04db6a64cddaf76d",
                             "https://item.kakaocdn.net/do/1237df944742acb58c66e92f0b605088f43ad912ad8dd55b04db6a64cddaf76d"]
        chosen_image = random.choice(all_image_choices)
        e = discord.Embed(title="", description="")
        e.set_image(url=chosen_image)
        await app.send_message (message.channel, embed = e)

app.run(token)
