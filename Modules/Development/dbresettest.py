#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module
from sopel.tools import stderr, Identifier
from sopel.db import SopelDB


def setup(bot):

    bot.memory['Sopel_DatabaseCache'] = dict()

    # Inject Database Functions
    stderr("[Sopel_DatabaseCache] Implanting Database functions into bot.")
    SopelDB.reset_nick_value = SopelDBCache.reset_nick_value


class SopelDBCache:

    def reset_nick_value(self, nick, key):
        """Resets the value for a given key to be associated with the nick."""
        nick = Identifier(nick)
        nick_id = self.get_nick_id(nick)
        self.execute('DELETE FROM nick_values WHERE nick_id = ? AND key = ?', [nick_id, key])

    def reset_channel_value(self, channel, key):
        """Resets the value for a given key to be associated with a channel."""
        channel = Identifier(channel).lower()
        self.execute('DELETE FROM channel_values WHERE channel = ? AND key = ?', [channel, key])


@sopel.module.commands('dbreset')
def mainfunction(bot, trigger):

    bot.db.set_nick_value('deathbybandaid', 'weaponsb', 3)

    testval = 1
    bot.say("value is " + str(bot.db.get_nick_value('deathbybandaid', 'weapons')))

    bot.say("setting value to " + str(testval))
    bot.db.set_nick_value('deathbybandaid', 'weapons', testval)

    bot.say("value is " + str(bot.db.get_nick_value('deathbybandaid', 'weapons')))

    bot.say("resetting value")
    bot.db.reset_nick_value('deathbybandaid', 'weapons')

    bot.say("value is " + str(bot.db.get_nick_value('deathbybandaid', 'weapons')))

    bot.say("valueb is " + str(bot.db.get_nick_value('deathbybandaid', 'weaponsb')))
