
import argparse

DEBUG = False

# Verbosity Levels
VERBOSITY_LEVEL_QUIET = 1
VERBOSITY_LEVEL_NORMAL = 2
VERBOSITY_LEVEL_VERBOSE = 3
VERBOSITY_LEVEL_VERY_VERBOSE = 4
VERBOSITY_LEVEL_DEBUG = 5

# Message Types
MSG_TYPE_NORMAL  = 0x00000000
MSG_TYPE_DEBUG   = 0x00000001
MSG_TYPE_WARNING = 0x00000010
MSG_TYPE_ERROR   = 0X00000100

# Message Prompts
# TODO: Add timestamps
DEBUG_MESSAGE_PROMPT   = "[DEBUG]:   "
WARNING_MESSAGE_PROMPT = "[WARNING]: "
ERROR_MESSAGE_PROMPT   = "[ERROR]:   "

def Print(msg, type):
    MESSAGE_PROMPT = ""

    if type == MSG_TYPE_DEBUG:
        MESSAGE_PROMPT = DEBUG_MESSAGE_PROMPT
    elif type == MSG_TYPE_WARNING:
        MESSAGE_PROMPT = WARNING_MESSAGE_PROMPT
    elif type == MSG_TYPE_ERROR:
        MESSAGE_PROMPT = ERROR_MESSAGE_PROMPT

    print(MESSAGE_PROMPT + msg)

parser = argparse.ArgumentParser()

parser.add_argument(      "--version",             help = "Print the program version and exit")
parser.add_argument("-d", "--default",             help = "Print the default action and exit")
parser.add_argument("-v", "--verbose",             help = "Increase the output verbosity", action = "store_true")
parser.add_argument("-c", "--config",              help = "Configuration file to use")
parser.add_argument("-s", "--sides",   type = int, help = "Number of sided-die to use")
parser.add_argument("-n",              type = int, help = "Number of dice to roll. This option will work only if all the die being rolled have the same number of sides.")

args = parser.parse_args()

if DEBUG:
    Print("Debug mode enabled.", MSG_TYPE_DEBUG)
else:
    if args.verbose:
        Print("Verbose output: %s" % args.verbose, MSG_TYPE_NORMAL)

if args.verbose:
    Print("Verbosity has been turned on.", MSG_TYPE_DEBUG)
