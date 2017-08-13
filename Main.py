'''
Created on 2017/08/10

@author: Kotmw0701
'''
# -*- coding: utf-8 -*-

import discord
import re

client = discord.Client()
countdict = {}

@client.event
async def on_member_join(member):
    await client.send_message(member, getSeparatorMessage(
        "Discord Game Playersへご参加いただき有難うございます。当サーバー（DGPサーバー）では元々マインクラフトをしていた人を中心としてサーバーを立て、現在は色々なジャンルの話や、雑談をすることを想定して運営しています。",
        "それらチャンネルに入る前に、参加者全員に自己紹介を書いてもらうようお願いしています。",
        "",
        "Discord Game Players → #general で趣味などを含めた自己紹介文を書いてください。",
        "確認次第、認証を行います。",
        "",
        "Have fun!                                 DGP - Admin: kazu0617",
        "",
        "",
        "===========================================",
        "このメッセージは自動的に作って、配信してるよ",
        "返信をしても、お返事出来ないから注意してね",
        "==========================================="))

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    for server in client.servers:
        countdict[server.id] = 0

@client.event
async def on_message(message):
    if message.server is None:
        return
    nickname = message.server.me.nick
    if nickname is None:
        nickname = 'DGP_Auth'
    if re.match('.*'+nickname+'(ちゃん|ちゃーん|さん|さーん|くん|くーん).*', message.content):
        if '文字数判定お願い' in message.content:
            countdict[message.server.id] = 0
            users = u'文字数が規定を越していないのは \r\n ```'
            count = 0
            for user in message.server.members:
                if user.bot:
                    continue
                if user.id == 190468887593222144:
                    continue
                print("test2")
                print(is_AuthOther(message.server, user))
                if is_AuthOther(message.server, user):
                    print("test3")
                    users += user.name + ' '
                    count += 1
            users += '``` \r\n以上'+str(count)+' 名になります。'
            #await client.send_message(message.channel, users)
            return
        if message.server.id in countdict:
            i = countdict[message.server.id]
        if i < 3:
            await client.send_message(message.channel, 'はいはーい')
        elif i >= 3 and i < 5:
            await client.send_message(message.channel, getEmoji(message.server, "Soo3")+' 何回呼ぶの？')
        elif i >= 5:
            await client.send_message(message.channel, getEmoji(message.server, "Soo4")+' 用もないのに何回も呼ばないで')
        i += 1
        countdict[message.server.id] = i

def getSeparatorMessage(*msgs):
    separator = u'\r\n'
    text = u''
    for msg in msgs:
        text = text+msg+separator
    return text

def getEmoji(server, name):
    for emoji in server.emojis:
        if emoji.name == name:
            return '<:'+name+':'+emoji.id+'>'
    return None
    
def is_AuthOther(server, user):
    print("test")
    counts = 0
    for message in client.logs_from(server.get_channel(190495358843879428), limit=500):
        print("test")
        print(message)
        if message.author.id != user.id:
            continue
        msg = message.content.replace('\r\n', '').replace('\r', '').replace('\n', '') .replace(' ', '').replace('　', '')
        counts += len(msg)
        print(counts)
    return counts

client.run("MzQ1MTE0MTQzNDQ1MjIxMzg2.DG4TSA.Apf-NP5-YZLQTKBiJ_O2DDGypKg")