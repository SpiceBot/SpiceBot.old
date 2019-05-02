#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module


# imports for system and OS access, directories
import os
import sys

import json
import requests
from operator import itemgetter

# imports based on THIS file
# moduledir = os.path.dirname(__file__)
# shareddir = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(shareddir)
# from BotShared import *

comdict = {
            "author": "deathbybandaid",
            "contributors": [],
            "description": "",
            'privs': [],
            "example": "",
            "exampleresponse": "",
            }

# from pip._internal.utils.misc import get_installed_distributions

# from inspect import getmembers, isfunction


@sopel.module.commands('dbbtest', 'deathbybandaidtest')
def mainfunction(bot, trigger):

    bot.say("dbb test module")

    bot.deathbybandaid = dict()

    bot.deathbybandaid['test'] = 'fart'

    bot.say(str(bot.deathbybandaid))

    return

    bot.say("gathering information")
    irc_events_list = class_directory(sopel.tools._events.events)
    irc_events_values = []
    for irc_event in irc_events_list:
        irc_events_values.append(eval("sopel.tools._events.events." + irc_event))
    irc_events_values, irc_events_list = array_arrangesort(bot, irc_events_values, irc_events_list)

    bot.say("preparing writing script")
    filecontents = []
    filecontents.append("#!/usr/bin/env python")
    filecontents.append("# coding=utf-8")
    filecontents.append("from __future__ import unicode_literals, absolute_import, print_function, division")
    filecontents.append("")
    filecontents.append("# sopel imports")
    filecontents.append("from sopel import module")
    filecontents.append("from sopel.tools import stderr")
    for irc_event_name, irc_event_val in zip(irc_events_list, irc_events_values):
        filecontents.append("")
        filecontents.append("")
        filecontents.append("# " + irc_event_name + " = '" + irc_event_val + "'")
        filecontents.append("@module.event('" + irc_event_val + "')")
        filecontents.append("@module.rule('.*')")
        filecontents.append("def parse_event_" + irc_event_val + "(bot, trigger):")
        filecontents.append("   stderr(trigger.event + "    " + str(trigger.args))")

    bot.say("starting writing script")
    filename = '/home/spicebot/script.py'
    f = open(filename, "w+")
    for line in filecontents:
        f.write(line + "\n")
    f.close()
    bot.say("done writing script")

    return

    # text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget metus ipsum. Phasellus ut venenatis tortor. Sed eget egestas nisi. Curabitur fermentum in ligula sit amet dignissim. Praesent iaculis volutpat diam a interdum. Curabitur in quam vitae lectus finibus congue id vel urna. Nulla sollicitudin vulputate libero, vitae mattis leo gravida a. Morbi ut mollis sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi lobortis vel purus in maximus. Aliquam id lacus non augue rhoncus tempor. Vestibulum fringilla nisi sed tellus dignissim porta. Suspendisse congue ultricies varius. Etiam tincidunt, arcu semper vulputate suscipit, nisi diam mattis dolor, ac condimentum mi lectus et ex. Nullam cursus vel risus nec tincidunt. Aliquam viverra bibendum est, vitae tincidunt risus iaculis a. Mauris efficitur eros vitae nisl cursus, ut fringilla augue vulputate. Fusce tempor lacus non lectus placerat, at consectetur mauris congue. Morbi dui mauris, tristique"

    # text = "This is a test"

    byte_max = 512
    reserved_irc_bytes = 15
    byte_max -= reserved_irc_bytes
    byte_max -= len((bot.users.get(bot.nick).hostmask).encode('utf-8'))
    byte_max -= len((trigger.sender).encode('utf-8'))

    # text_list = get_sendable_message_list(text, byte_max)

    # for item in text_list:
    # bot.osd(text_list)

    return

    bot.say("here")

    bot.say(str((bot.channels[trigger.sender].privileges.keys())))

    bot.say(str(bot.memory["botdict"]["users"].keys()))

    return

    #botcom = bot_module_prerun(bot, trigger)
    #if not botcom.modulerun:
    #    return

    #if not botcom.multiruns:
    #    execute_main(bot, trigger, botcom)
    #else:
    #    # IF "&&" is in the full input, it is treated as multiple commands, and is split
    #    commands_array = spicemanip.main(botcom.triggerargsarray, "split_&&")
    #    if commands_array == []:
    #        commands_array = [[]]
    #    for command_split_partial in commands_array:
    #        botcom.triggerargsarray = spicemanip.main(command_split_partial, 'create')
    #        execute_main(bot, trigger, botcom)

    # botdict_save(bot)


def execute_main(bot, trigger, botcom):
    bot.say("DBB Testing")

    # functions_list = dir(__file__)
    # bot.say(str(functions_list))

    return

    main_dir = os.path.dirname(os.path.abspath(sopel.__file__))
    modules_dir = os.path.join(main_dir, 'modules')

    bot.say(str(modules_dir))

    return

    # osd(bot, botcom.channel_current, 'say', 'Generating list of installed pip modules.')

    # pipinstalled = sorted(["%s" % (i.key) for i in get_installed_distributions()])
    # pipinstalled = sys.modules.keys()
    # osd(bot, botcom.channel_current, 'say', str(pipinstalled))


def class_directory(inputclass):

    # make sure input is a class
    # if not isinstance(inputclass, class):
        # return []

    classdirlistfull, classdirlistclean = dir(inputclass), []
    for classdiritem in classdirlistfull:
        if not classdiritem.startswith("_"):
            classdirlistclean.append(classdiritem)
    return classdirlistclean


def array_arrangesort(bot, sortbyarray, arrayb):
    sortbyarray, arrayb = (list(x) for x in zip(*sorted(zip(sortbyarray, arrayb), key=itemgetter(0))))
    return sortbyarray, arrayb
