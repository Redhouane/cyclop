"""
red-bot contains components related twitter account management.

This bot consists of the following components:
:config: Manage connection to twitter api using Tweepy
:like_retweet: A program which like and retweet tweets select using a list of keywords given within arg.txt file
"""

import logging

# Version of the surya package
__version__ = "1.0.0"

# Directories for reading/writing logs
LOGS_FILE = '../../logs/red-bot.log'

# Logging config
logging.basicConfig(level=logging.INFO,
                    filename=LOGS_FILE,
                    filemode='a',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
