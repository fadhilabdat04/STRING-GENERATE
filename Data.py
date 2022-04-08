from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to \n{}
Bot For help You to Create Session.
[➼](https://te.legra.ph/file/0cb0a04edd1d3eea89108.jpg) So Why are you waiting For Generat STRING Session
───────────────────────

If you don't trust this bot, 
1) stop reading this message
2) delete this chat
───────────────────────
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

Pᴏᴡᴇʀᴇᴅ  Bʏ: [SUSHIL](https://t.me/iSUSHIL)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔰𝗦𝘁𝗮𝗿𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻🔰", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🔰𝗦𝘁𝗮𝗿𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻🔰", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔰𝗦𝘁𝗮𝗿𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻🔰", callback_data="generate")],
        [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/iSOULSPAM")],
        [
            InlineKeyboardButton(" 𝙃𝙤𝙬 𝙩𝙤 𝙐𝙨𝙚", callback_data="help"),
            InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩", callback_data="about")
        ],
        [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/TheiSOUL")],
    ]

    # Help Message
    HELP = """
**Available Commands** 🛠



/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by @TheNavya

Source Code : [Click Here](https://github.com/NAVYA-DEVELOPER/STRING-GENERATE)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @iSUSHIL
    """
