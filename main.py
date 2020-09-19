import asyncio
import os
from urllib.request import urlopen

import discord
import datetime
from bs4 import BeautifulSoup
import random

client = discord.Client()


calcResult = 0

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("==========")

    async def bt(games):
        await client.wait_until_ready()

        while not client.is_closed():
            for g in games:
                await client.change_presence(status=discord.Status.online, activity=discord.Game(g))
                await asyncio.sleep(5)
    await bt(['마고야 도움말','2020-09-03출생','아직 미완성'])


@client.event
async def on_message(message):
    if message.content.startswith("마고야 안녕"):
        await message.channel.send("응 안녕")
    if message.content == "마고야 도움말":
        embed = discord.Embed(title="도움말", description='''마고의 명령어 입니다''', color=0x8285FA)
        embed.add_field(name="대화", value="뭐해/갠디/마마고(마고야 x)", inline=False)
        embed.add_field(name="놀이", value="사다리타기 (사람/결과)", inline=False)
        embed.add_field(name="잡다한 기능 1", value="1부터10/시간/핑/골라(목록)", inline=False)
        embed.add_field(name="잡다한 기능 2", value="음식추천/계산 (더하기,빼기,곱하기,나누기) 숫자 숫자", inline=False)
        embed.add_field(name="특수기능", value="식제 메시지 감지/새로온 유저 감지", inline=False)
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=False)
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=False)
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=False)
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=False)
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=False)

        await message.channel.send(embed=embed)
    if message.content.startswith("마고야 뭐해"):
        await message.channel.send("니생각")
    if message.content.startswith("마고야 갠디"):
        await message.author.send("갠디 보냈다.")
    if message.author.bot:
        return None
    if message.content.startswith("마마고"):
        await message.channel.send("응? 왜불러")
    if message.content.startswith("마고야 시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await message.channel.send(str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분 입니다.")
    if message.content.startswith("마고야 핑"):
        embed=discord.Embed(title=':ping_pong:퐁!',description=str(client.latency)+'ms',color=0x8285FA)
        await message.channel.send(embed=embed)
    if message.content.startswith("마고야 정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x8285FA)
        embed.add_field(name="이름",value=message.author.name,inline=False)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년"+str(date.month) + "월"+str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("마고야 사다리타기 "):
        team = message.content[10:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0,len(person)):
            await message.channel.send(person[i] + "은(는)" + teamname[i] + "입니다")
    if message.content.startswith("마고야 골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(2,len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)
    if message.content.startswith("마고야 음식추천"):
        food = "삼겹살 곱창 스테이크 초밥 회 후라이드치킨 육회 대게찜 떡순튀 소갈비" \
               " 간장게장 랍스터버터구이 김치찌게 감자탕 양념치킨 라면 부대찌개 보쌈" \
               " 닭발 샤브샤브 닭갈비 햄버거 차돌박이 된장찌개 닭강정 김볶 피자 수육 " \
               "국밥 양념게장 찜닭 간장치킨 조개구기 닭도리탕 족발 탕수육 해물찜 양갈비" \
               " 물냉면 산낙지 크림파스타 닭꼬치 짜장면 불족발 양꼬치 설렁탕 갈비탕 " \
               "대하소금구이 훈제치킨 짬뽕 버팔로윙 떡국 타코야키 물회 돈까스 라멘 우동" \
               " 쭈꾸미볶음 바지락칼국수 훠궈 순두부찌개 제육볶음 잔치국수 깐쇼새우" \
               " 육개장 돼지껍데기 토마토스파게티 카레돈까스덮밥 오리주물럭 누룽지백숙" \
               " 비빔밥 수제비 로제파스타 소고기무국 삼계탕 해신탕 쌀국수 오일파스타 " \
               "낙지볶음 김밥 비빔냉면 함밥스테이크 매운탕 소떡소떡 알밥 토스트 선지해장국" \
               " 꼬막무침 대구내장탕 불고기 참치마요덮밥 카레 꿔바로우 메밀국수 샌드위치" \
               " 보리굴비 깐풍기 두부김치 청국장 치즈퐁듀 찐만두 쫄면 비빔국수 오므라이스" \
               " 문어숙회 묵사발 군만두 어묵 오코노미야끼 마파두부덮밥 물만두 중식볶음밥 " \
               "고등어조림 모듬전 타코 골뱅이무침 해물누룽지탕 추어탕 닭똥집 버섯전골 " \
               "콩국수 분짜 오징어볶음 과메기 잡채밥 소세지 콩나물밥"
        foodchoice = food.split(" ")
        foodnumber = random.randint(2,len(foodchoice))
        foodresult = foodchoice[foodnumber]
        await message.channel.send(foodresult + " 처머겅")

    if message.content.startswith("마고야 실검"):
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class": "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i +1)) + "위 | " + e.text + "\n"
            await message.channel.send(result)

    if message.content.startswith("마고야 1부터10"):
        for x in range(10):
            await message.channel.send(x + 1)
    if message.content.startswith("마고야 계산"):
        global calcResult
        if message.content[7:].startswith("더하기"):
            calcResult = int(message.content[11:12]) + int(message.content[13:14])
            await message.channel.send("Result : " + str(calcResult))
        if message.content[7:].startswith("빼기"):
            calcResult = int(message.content[10:11]) - int(message.content[12:13])
            await message.channel.send("Result : " + str(calcResult))
        if message.content[7:].startswith("곱하기"):
            calcResult = int(message.content[11:12]) * int(message.content[13:14])
            await message.channel.send("Result : " + str(calcResult))
        if message.content[7:].startswith("나누기"):
            try:
                calcResult = int(message.content[11:12]) / int(message.content[13:14])
                await message.channel.send("Result : " + str(calcResult))
            except ZeroDivisionError:
                await message.channel.send("You can't divide with 0.")

@client.event
async def on_message_delete(message):
    await message.channel.send("메세지 삭제 감지(" + str(message.author) + "): " + message.content)
    return


async def on_member_join(member):
    await member.guild.get_channel(743810244982866093).send(member.mention + "님이 새롭게 접속했습니다. 환영해주세요!")
    return
















access_token = os.environ["BOT_TOKEN"]
client.run(access_token)




















