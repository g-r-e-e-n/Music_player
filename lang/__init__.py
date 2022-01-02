"""
Green_Player, Telegram Voice Chat Bot
Copyright (c) 2022
"""

import json


def load(lang):
    return json.load(open(f"./lang/{lang}.json", "r"))
