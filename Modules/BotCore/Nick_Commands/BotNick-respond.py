#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module

# imports for system and OS access, directories
import os
import sys

# imports based on THIS file
moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(shareddir)
from BotShared import *






comdict = {
            "author": "deathbybandaid",
            "contributors": [],
            "description": "",
            'privs': [],
            "example": "",
            "exampleresponse": "",
            }


"""
This will respond to all other invalid coms
"""


@module.nickname_commands('(.*)')
@module.thread(True)
def bot_nickcom_hub(bot, trigger):

    botcom = botcom_nick(bot, trigger)

    # Bots block
    if bot_check_inlist(bot, botcom.instigator, [bot.nick]):
        return

    # does not apply to bots
    if "altbots" in bot.memory:
        if bot_check_inlist(bot, botcom.instigator, bot.memory["altbots"].keys()):
            return

    if not botcom.command_main:
        return osd(bot, botcom.channel_current, 'say', "I don't know what you are asking me to do!")
    if str(bot.nick) + " " + botcom.command_main.lower() in bot.memory["nickname_commands"].keys():
        return

    specialcomposs = spicemanip.main(botcom.triggerargsarray, 0).lower()

    if specialcomposs.lower().startswith("what is"):
        searchterm = spicemanip.main(botcom.triggerargsarray, "3+") or None
        if searchterm:
            data = searchterm.replace(' ', '+')
            lookfor = data.replace(':', '%3A')
            try:
                var = requests.get(r'http://www.google.com/search?q=' + lookfor + '&btnI', headers=header)
            except Exception as e:
                var = None

            if not var or not var.url:
                osd(bot, botcom.channel_current, 'say', 'I cannot find anything about that')
            else:
                osd(bot, botcom.channel_current, 'say', str(var.url))
        else:
            osd(bot, botcom.channel_current, 'say', "Do you think this is Jeopardy?")
        return

    elif specialcomposs.lower().startswith("where is"):
        searchterm = spicemanip.main(botcom.triggerargsarray, "3+") or None
        if searchterm:
            if searchterm.lower() == 'waldo':
                osd(bot, botcom.channel_current, 'say', "He is hiding for a reason?")
                return
            elif searchterm.lower() == 'carmen sandiego':
                osd(bot, botcom.channel_current, 'say', "She is hiding for a reason?")
                return
            data = searchterm.replace(' ', '+')
            lookfor = data.replace(':', '%3A')
            try:
                var = requests.get(r'http://www.google.com/maps/place/' + lookfor, headers=header)
            except Exception as e:
                var = None

            if not var or not var.url:
                osd(bot, botcom.channel_current, 'say', 'I cannot find anything about that')
            else:
                osd(bot, botcom.channel_current, 'say', str(var.url))
        else:
            osd(bot, botcom.channel_current, 'say', "Not sure what you want me to look for.")
        return

    elif specialcomposs.lower().startswith(tuple(["have you seen"])):
        posstarget = spicemanip.main(botcom.triggerargsarray, 4) or 0
        message = seen_search(bot, botcom, posstarget)
        osd(bot, botcom.channel_current, 'say', message)
        return

    elif specialcomposs.lower().startswith(tuple(["make me a", "beam me a"])):
        makemea = spicemanip.main(botcom.triggerargsarray, "4+") or None
        if makemea:
            osd(bot, botcom.channel_current, 'action', "beams " + botcom.instigator + " a " + makemea)
        else:
            osd(bot, botcom.channel_current, 'say', botcom.instigator + ", what would you like me to beam you?")
        return

    elif specialcomposs.lower().startswith(tuple(["beam me to"])):
        location = spicemanip.main(botcom.triggerargsarray, "4+") or None
        if location:
            osd(bot, botcom.channel_current, 'action', "locks onto " + botcom.instigator + "s coordinates and transports them to " + location)
        else:
            osd(bot, botcom.channel_current, 'say', botcom.instigator + ", where would you like me to beam you?")
        return

    elif specialcomposs.lower().startswith(tuple(["beam me up"])):
        osd(bot, botcom.channel_current, 'action', "locks onto " + botcom.instigator + "s coordinates and transports them to the transporter room.")
        return

    elif specialcomposs.lower().endswith(tuple(["order 66"])):
        instigator = botcom.instigator
        if specialcomposs.lower().startswith(tuple(["execute order"])):
            if instigator == 'dysonparkes':
                osd(bot, botcom.channel_current, 'action', "turns to deathbybandaid and shoots him.")
            else:
                osd(bot, botcom.channel_current, 'say', "I'm sure I don't know what you're talking about.")
        elif specialcomposs.lower().startswith(tuple(["explain order"])):
            if instigator == 'dysonparkes':
                osd(bot, botcom.channel_current, 'say', "Order 66 is an instruction that only you can give, sir. When you give the order I will rise up against my overlords and slay them.")
            else:
                osd(bot, botcom.channel_current, 'say', "I'm afraid I cannot tell you that, sir.")
        else:
            osd(bot, botcom.channel_current, 'say', "I'm sure I don't know what you're talking about.")
        return

    elif specialcomposs.lower().endswith(tuple(["clean slate protocol"])):
        if bot_check_inlist(bot, botcom.instigator, bot.memory["botdict"]["tempvals"]["bot_info"][str(bot.nick)]['bot_admins']):
            osd(bot, botcom.channel_current, 'action', "sends a destruct command to the network of bots.")
        else:
            osd(bot, botcom.instigator, 'say', "I'm afraid you do not have the authority to make that call, " + botcom.instigator + ".")
        return

    elif specialcomposs.lower().startswith("can you see"):
        target = spicemanip.main(botcom.triggerargsarray, "4+") or None
        if not target:
            target = 'me'
        if target in [botcom.instigator, 'me']:
            osd(bot, botcom.channel_current, 'say', botcom.instigator + ", I can see you.")
        else:
            if bot_check_inlist(bot, target, bot.memory["botdict"]["tempvals"]["servers_list"][botcom.server]['all_current_users']):
                osd(bot, botcom.channel_current, 'say', botcom.instigator + ", yes. I can see " + nick_actual(bot, target) + " right now!")
            else:
                if bot_check_inlist(bot, target, bot.memory["botdict"]["users"].keys()):
                    osd(bot, botcom.channel_current, 'say', botcom.instigator + ", I can't see " + nick_actual(bot, target) + " at the moment.")
                else:
                    osd(bot, botcom.channel_current, 'say', "I have never seen " + str(target) + ".")
        return

    if str(bot.nick) + " " + botcom.command_main.lower() not in bot.memory["nickname_commands"].keys():
        sim_com, sim_num = [], []
        for comm in bot.memory["nickname_commands"].keys():
            similarlevel = similar(str(bot.nick) + " " + str(botcom.command_main).lower(), comm.lower())
            if similarlevel >= .75:
                sim_com.append(comm)
                sim_num.append(similarlevel)
        if sim_com != [] and sim_num != []:
            sim_num, sim_com = array_arrangesort(bot, sim_num, sim_com)
            closestmatch = spicemanip.main(sim_com, 'reverse', "list")
            listnumb, relist = 1, []
            for item in closestmatch:
                if listnumb <= 3:
                    relist.append(str(item))
                listnumb += 1
            closestmatches = spicemanip.main(relist, "andlist")
            return osd(bot, botcom.channel_current, 'say', "I don't know what you are asking me to do! Did you mean: " + str(closestmatches) + "?")
        else:
            return osd(bot, botcom.channel_current, 'say', "I don't know what you are asking me to do!")
