#  (c)2020 TeleBot
#
# You may not use this plugin without proper authorship and consent from @TeleBotSupport
#
# Credits to everyone who made this plugin, idk who... I just merged them xD
#
""" Userbot module for having some fun with people. """

import asyncio
import random

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@jiNikuttan"

# ================= CONSTANT =================
RUNSREACTS = [
    "`പെമ്പിള്ളേരെ റോട്ടിക്കൂടെ നടക്കാൻ നീ സമ്മതിക്കില്ല , അല്ലേ.......ഡാ, നീയാണീ അലവലാതി ഷാജി അല്ലേ ?`",
    "`വർക്കിച്ചാ യെവൻ പുലിയാണ് കേട്ടാ പുലിയെന്ന് പറഞ്ഞാ വെറും പുലിയല്ല … ഒരു സിംഹം...😜😜 `",
    "`മാമ്മനും അനന്തരവനും കൂടി പണ്ട് ഈഴിര തോർത്തു വെച്ച് പരൽ മീനുകളെ പിടിച്ചു കളിച്ചിട്ടുണ്ടാകും ... പക്ഷെ ആ ഈഴിര വിരിച്ചാൽ സ്രാവിനെ കിട്ടുമെന്നു കരുതരുത് .. ഇത് കാർത്തികേയനാ ...😎😎😎 `",
    "`കഴിഞ്ഞ ഓണത്തിന് കൈപ്പുഴ കുഞ്ഞപ്പന്റെ കയ്യറുത്തപ്പോൾ കട്ടച്ചോരയാ മുഖത്തു തെറിച്ചത് അത്രക്കും വരില്ലല്ലോ ഒരു പീറ ആട്...🤭🤭🤭😜`",
    "`കളി ഹൈറേഞ്ചിലാണെങ്കിലും അങ്ങ് പാരീസിൽ ചെന്ന് ചോദിച്ചാലറിയാം ഈ സാത്താനെ...😎😎😡 `",
    "`എന്റെ ഹൈറേഞ്ചിൽ വന്നിട്ട് എന്റെ പിള്ളേരെ പേടിപ്പിക്കുന്നോടാ നാറികളേ...😡😡😜`",
    "`എവിടെയാടാ നീ അടിച്ചോണ്ട് പോയ എന്റെ നീലക്കുയിൽ 😡😡😜..`",
    "`കൃഷ്ണവിലാസം ഭഗീരഥൻ പിള്ള.. വലിയ വെടി നാല്.. ചെറിയ വെടി നാല്...😜😜🤭`",
    "`ഇര തേടി വരുന്ന പുലി കെണി തേടി വരില്ല..... പുലിയെ അതിന്റെ മടയിൽ ചെന്ന് വേട്ടയാടി കൊല്ലണം.... അതാണ് കാട്ടിലെ നിയമം...😎😎😇`",
    "`നീ പോ മോനെ ദിനേശാ...`",
    "`മരിപ്പിനുള്ള പരിപ്പുവടേം ചായേം ഞാൻ തരുന്നുണ്ട് ഇപ്പോഴല്ല പിന്നെ`",
    "`സാർ മഹാരാജാസ് കോളേജിൽ പഴേ k.s.u കാരനായിരുന്നല്ലേ അവിടുത്തെ s. F. I പിള്ളേർടെ ഇടി അവസാനത്തേതാണെന്ന് കരുതരുത്...`",
    "`നീയൊക്കെ അര ട്രൗസറും ഇട്ടോണ്ട് അജന്തയിൽ ആദിപാപം കണ്ടോണ്ട് നടക്കണ ടൈമിൽ നമ്മളീ സീൻ വിട്ടതാ നിന്റെയൊക്കെ ഇക്കാനോട് ചോദിച്ചാൽ അറിയാം പോയി ചോദിക്ക് 😎😎😈 `",
    "`വെല്ലുവിളികൾ ആവാം പക്ഷെ അത് നിന്നെക്കാൾ നാലഞ്ചോണം കൂടുതൽ ഉണ്ടവരോടാവരുത് `",
    "`ഇവിടെ കിടന്ന് എങ്ങാനും show ഇറക്കാൻ ആണ് പ്ലാൻ എങ്കിൽ പിടിച്ചു തെങ്ങിന്റെ മൂട്ടിലിട്ട് നല്ല വീക്ക് വീക്കും 😡😡😡`",
    "`ഈ പൂട്ടിന്റെ മുകളിൽ നീ നിന്റെ പൂട്ടിട്ട് പൂട്ടിയാൽ നിന്നെ ഞാൻ പൂട്ടും .. ഒടുക്കത്തെ പൂട്ട് 😡`",
    "`തമ്പുരാൻന്ന് വിളിച്ച അതെ നാവോണ്ട് തന്നെ ചെ** എന്ന് വിളിച്ചതിൽ മനസ്താപണ്ട്..എടോ അപ്പനെന്നു പേരുള്ള തേർഡ് റേറ്റ് ചെ** താനാരാടോ നാട്ടുരാജാവോ 😡😡`",
    "`ചന്തുവിനെ തോൽപ്പിക്കാൻ ആവില്ല മക്കളേ 😍😍🤗`",
    "`കൊച്ചി പഴയ കൊച്ചിയെല്ലെന്നറിയാ.... പക്ഷെ ബിലാൽ പഴയ ബിലാൽ തന്നെയാ 😈😈`",
    "`നെട്ടൂരാനോടാണോടാ നിന്റെ കളി 😜😜`",
    "`ഗോ എവേ സ്റ്റുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂ വിൽ നാട്ട് സീ എനി മിനിറ്റ് ഓഫ് ദി റ്റുഡേ.. എറങ്ങിപ്പോടാ 😜🤭🤣`",
    "`ആണ്ടവൻ ഇത് നിന്റെ കോയമ്പത്തൂരിലെ മായാണ്ടിക്കൊപ്പമല്ല കൊച്ചിയാ വിശ്വനാഥന്റെ കൊച്ചി 😎😎`",
    "`ഇതെന്റെ പുത്തൻ റെയ്ബാൻ ഗ്ലാസ്സാ ഇത് ചവിട്ടിപൊട്ടിച്ചാ നിന്റെ കാല് ഞാൻ വെട്ടും 😡😡😜`",
    "`നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ...😐 `",
    "`നാലാമത്തെ പെഗ്ഗിൽ ഐസ്ക്യൂബ്സ് വീഴുന്നതിനു മുൻപ് ഞാൻ അവിടെ എത്തും.....😉 `",
    "`പോരുന്നോ എന്റെ കൂടെ!😜 `",
    "`ഡാ ദാസാ... ഏതാ ഈ അലവലാതി.....😒 `",
    "`കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്ലി.....🥵 `",
    "`അല്ല ഇതാര് വാര്യംപിള്ളിയിലെ മീനാക്ഷി അല്ലയോ... എന്താ മോളെ സ്കൂട്ടറില്....🙈 `",
    "`മോന്തയ്ക്കിട്ട് കൊടുത്തിട്ട് ഒന്ന് എടുത്ത് കാണിച്ചുകൊടുക്ക് അപ്പോൾ കാണും ISI മാർക്ക് 😑 `",
    "`ഇട്ടിട്ട് പോകില്ലെന്ന് ഉറപ്പുള്ള പെണ്ണ്  🤰🤱👩👦 ”`",
    "`ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....⛪ `",
    "`ഇത് കണ്ണോ അതോ കാന്തമോ...👀 `",
]

RAPE_STRINGS = [
    "`വേലക്കാരി ആയിരുന്താലും നീ എൻ മോഹവല്ലി....🥰`",
    "`ഭവാനി ഒന്നു മനസ്സ് വെച്ചാൽ ഈ കലവറ നമുക്ക് മണിയറ ആക്കാം.....🥰🥰`",
    "`ഒരു മുത്തം തരാൻ പാടില്ല എന്നൊന്നും അന്റെ ഉപ്പാപ്പ പറഞ്ഞിട്ടുണ്ടാവില്ലല്ല....🥰😜`",
    "`ശോഭേ ഞാനൊരു വികാര ജീവിയാണ് 😜😜🥰😂 `",
    "`നിനക്കെന്നെ പ്രേമിച്ചൂടെ കൊച്ചേ 😜😜`",
    "`എങ്കിലേ എന്നോട് പറ ഐ ലവ് യൂന്ന് 🥰🥰🥰 `",
    "`പോരുന്നോ എന്റെ കൂടെ 🥰🥰 `",
    "`എനിക്ക് നിന്റെ പുറകിൽ നടക്കാനല്ല, ഒപ്പം നടക്കാനാണ് ഇഷ്ടം 🥰😍`",
    "`ഓളാ തട്ടമിട്ടു കഴിഞ്ഞാലെന്റെ സാറേ, പിന്നെ ചുറ്റുമുള്ളതൊന്നും കാണാൻ പറ്റൂല്ലാ 😍🥰`",
]
THANOS_STRINGS = [
    "`തെറി കേട്ടിട്ട് ഇവളുടെ വീട് കൊടുങ്ങല്ലൂർ ഭാഗത്താണെന്ന് തോന്നുന്നു...😜😜`",
    "`പുന്നാര മോളേ😜😜🤭 `",
    "`ചങ്ക് പറിച്ചു തരുന്ന ചങ്കത്തി കൂടെയുള്ളപ്പോൾ പിന്നെന്തിനാ ലവർ 🥰😜 `",
    "`ഇവൾ നമ്മളേക്കാൾ തറയാടാ...😂😂🤭`",
    "`അഹങ്കാരത്തിന് കയ്യും കാലും വെയ്ക്കാ... എന്നിട്ട് പെണ്ണെന്നു പേരും...🤣🤣😜`",
    "`ആനി മോനെ സ്നേഹിക്കുന്ന പോലെ , മാഗ്ഗിക്ക് എന്നെ സ്നേഹിക്കാമോ...🥰🥰😘`",
    "`അല്ല ഇതാരാ ! വാര്യംപള്ളിയിലെ മീനാക്ഷിയല്ലയോ ? എന്താ മോളേ സ്കൂട്ടർല്...😜😜🤣`",
]
ABUSEHARD_STRING = [
    "`നിന്റെ പേരെന്താന്നാ പറഞ്ഞെ -പൈലി ഡ്രാഗൺപൈലി ഡ്യൂഡ് സാറെന്ന്യല്ലേ പേരിട്ടത്.. എന്തൂള പേരാടാത് അയ്യേ...😛😛😜`",
    "`ദാമോദരൻ ഉണ്ണി മകൻ ദിൽമൻ ഇടക്കൊച്ചി, പീപ്പിൾ കാൾ മീ ഡ്യൂഡ് 😎😎🤨 `",
    "`മധ്യതിരുവിതാംകൂർ ഭരിച്ച രാജാവാ പേര് ശശി.. 😛😂🤣 `",
    "`തീരുമ്പോ തീരുമ്പോ പണി തരാൻ ഞാനെന്താ കുപ്പീന്ന് വന്ന ഭൂതോ... 😇😇🙄`",
    "`ഒന്ന് മിണ്ടാതിരിക്കുവോ.. എന്റെ കോൺസെൻട്രേഷൻ പോണ്.. ദേ ആയുധം വെച്ചുള്ള കളിയാ 😝😝😂`",
    "`സൂക്ഷിച്ചു നോക്കണ്ടടാ ഉണ്ണീ ഇത് ഞാനല്ല...😇🤣🤣`",
    "`ഈ യന്ത്രങ്ങളുടെ പ്രവർത്തനമൊന്നും താനെന്നെ പഠിപ്പിക്കേണ്ട ഞാനേ പോളിടെക്‌നിക് പഠിച്ചതാ 😎😎😝 `",
    "`ഡിങ്കോൾഫി അല്ലേ ഇത്രക്ക് ചീപ്പാണോ അര്ടിസ്റ്റ് ബേബി😉😉😜 `",
    "`ആദ്യമായി പ്രേമിച്ച പെണ്ണും ആദ്യമായി അടിച്ച ബ്രാൻഡും ഒരാളും ഒരു കാലത്തും മറക്കില്ല്യ😜😜😎`",
    "`ഡാ മോനേ അത് ലോക്കാ ഇങ്ങ് പോര്.. ഇങ്ങ് പോര്..😇😇🤭`",
    "`അടിച്ചതാരാടാ നിന്നെ ആണ്ടവനോ സേഡ്‌ജിയോ അടിച്ചതല്ല ചവിട്ടിയതാ ഷൂസിട്ട കാലുകൊണ്ട് 🤭🤭🤭`",
    "`വസൂ... ദേ തോറ്റു തുന്നം പാടി വന്നിരിക്കുന്നു നിന്റെ മോൻ...🤭🤭😜`",
    "`വോ ലമ്പേ.... വോ ബാത്തേ.... കോഴീ ന ജാനേ.... ങേ കോഴിയോ 🐓🐓🐓`",
    "`എന്താ? പെൺകുട്ടികൾക്കിങ്ങനെ സിമ്പിൾ ഡ്രെസ് ധരിക്കുന്ന പുരുഷന്മാരെ ഇഷ്ടമല്ലേ ? ഡോണ്ട് ദെ ലൈക് ?😎😜`",
    "`ലേലു അല്ലു ലേലു അല്ലു ലേലു അല്ലു അഴിച്ചു വിട് 🤣🤣`",
    "`ഇതെന്താ , എനിക്കുമാത്രം പ്രാന്തായതാണോ അതോ നാട്ടുകാർക്ക് മൊത്തത്തിൽ പ്രാന്തായോ ?😇😇🤣`",
    "`അങ്ങനെ പവനായി ശവമായി.. എന്തൊക്കെ ബഹളമായിരുന്നു.. മലപ്പുറം കത്തി, മെഷീൻഗണ്ണു, ബോംബ്, ഒലക്കേടെ മൂട്...🤭🤣🤣`",
]

PRO_STRINGS = [
    "`ഡാ മങ്കി മാങ്ങാതലയാ 😜`",
    "`വല്യ മലരനാണല്ലോടാ നീ`",
    "`പോയി ചാവടാ കള്ള പന്നീ`",
    "`പോയി തൊലയെടാ തവളാച്ചി മോറാ😜 `",
    "`മാറിപ്പോടാ മരം കൊത്തി മോറാ😜`",
    "`പുന്നാര മോനേ പോയി ചത്തൂടെ നിനക്ക് 😜`",
    "`നീ പോടാ കാട്ടുകോഴീ😜`",
    "`കോപ്പേ വല്യ ബഹളം വേണ്ട😜`",
    "`പുന്നാര മോനേ 😜`",
    "`പ്ഫാ ഇറങ്ങി പോടാ മാക്രി 😜`",
    "`നിന്റെ പെട്ടീം കെടക്കേം എടുത്ത് ഇപ്പോ ഇറങ്ങിക്കോണം ഇവിടുന്ന് `",
    "`ഇനി നീ വാ തുറന്നാൽ മണ്ണ് വാരി ഇടും 😜`",
    "`അടിച്ചു നിന്റെ മണ്ട പൊളിക്കും കേട്ടോടാ മരപ്പട്ടീ... 😡😜`",
    "`മത്തങ്ങാ തലയാ 😜`",
    "`മാങ്ങാണ്ടി മോറാ 😜`",
]

SLAP_TEMPLATES = [
    "{user1} {victim} ന്റെ തലക്ക് ഒലക്ക കൊണ്ട് അഞ്ചാറു അടി കൊടുത്തു 😪😪 .",
    "{user1} ചാണകം വാരി {victim} ന്റെ മോന്തക്ക് എറിഞ്ഞു 🤢🤮 .",
    "️{user1} ഓടി വന്ന് {victim} ന്റെ തലയിൽ ചീമുട്ടയെറിഞ്ഞു 🤭🤭😜.",
    "{user1} ️{victim} നെ കാലേ വാരി നിലത്തടിച്ചു 🤓☹️",
    "️{user1} വലിയ പാറക്കല്ലെടുത്തു {victim} ന്റെ തലക്കെറിഞ്ഞു 😱😱🤭 .",
    "{user1} {victim} നെ വിളിച്ചോണ്ട് പോയി പൊട്ടകിണറ്റിൽ തള്ളിയിട്ടു 🤗🤗😝 .",
    "️{user1} കാക്കയെ വിളിച്ചു വരുത്തി {victim} ന്റെ തലയിൽ അപ്പിയിടീച്ചു 😝🤣 .",
    "{user1} ഓടി വന്ന് ചൂരൽ കൊണ്ട് {victim} ന്റെ ചന്തിക്കിട്ട് അഞ്ചാറു അടി കൊടുത്ത് 😂😜 .",
    "{user1} {victim} നെ കൊതുകിനെ കൊല്ലുന്ന പോലെ അടിച്ചു കൊന്നു 🤭😜.",
    "️{user1} കോഴിക്കാഷ്ടം എടുത്ത് {victim} ന്റെ മുഖത്തു തേച്ചു 🤭🤣.",
    "{user1} {victim} നെ എടുത്തോണ്ട് പോയി ചാണകക്കുഴിയിലിട്ടു 🤣🤣😛.",
    "️{user1} പട്ടിയെ അഴിച്ചു വിട്ട് {victim} ന്റെ ചന്തിയിൽ കടിപ്പിച്ചു 😂😂😛.",
    "{user1} കട്ടുറുറുമ്പിനെകൊണ്ട് {victim} ന്റെ കുണ്ടിക്ക് കടിപ്പിച്ചു 🤭🤭😜",
    "{user1} {victim} നെ കോഴിയാണെന്ന് കരുതി കൂട്ടിലടച്ചു 🤭🤭😜",
]

HATE_STRINGS = [
    "🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓കോഴി 🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓കോഴി 🐓🐓🐓🐓🐓🐓കോഴി 🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓കോഴി 🐓🐓🐓🐓🐓🐓",
    "എടാ കള്ള കോയീ.... 🐓🐓🐓🐓🐓🐓",
    "കൊക്കര കോ കോ.... 🐓🐓🐓🐓🐓🐓",
    "ബ  ബ്ബ ബ്ബാ കോയി ബാ  ബാ... 🐓🐓",
    "ഡേയ്  കള്ള കാട്ടുകോഴീ... 🐓🐓🐓🐓",
    "നിക്കെടാ കോഴീ അവിടെ... 🐓🐓🐓🐓",
    "ശ്ശോ പോ കോഴീ... 🐓🐓🐓🐓",
    "കുണുക്കിട്ട കോഴീ കുളക്കോഴീ.... 🎶🐓🐓🐓",
    "ബാ ബാ ബ്ബാ  കോഴീ വന്ന് കൂട്ടിൽ കേറ്... 🐓🐓🐓",
]

# ===========================================

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Sur_vivor"


@telebot.on(admin_cmd(pattern="mslap ?(.*)"))
@telebot.on(sudo_cmd(pattern="mslap ?(.*)", allow_sudo=True))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await eor(event, caption)

    except BaseException:
        await eor(event, "`Can't slap this nibba !!`")


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await eor(event, "`I don't slap strangers !!`")
            return None

    return replied_user


async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)

    caption = temp.format(user1=DEFAULTUSER, victim=slapped)

    return caption


@telebot.on(admin_cmd(outgoing=True, pattern="mrape"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="mrape"))
async def raping(raped):
    index = random.randint(0, len(RAPE_STRINGS) - 1)
    reply_text = RAPE_STRINGS[index]
    await raped.edit(reply_text)


@telebot.on(admin_cmd(outgoing=True, pattern="mshe"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="mshe"))
async def thanos(thanos):
    index = random.randint(0, len(THANOS_STRINGS) - 1)
    reply_text = THANOS_STRINGS[index]
    await thanos.edit(reply_text)


@telebot.on(admin_cmd(outgoing=True, pattern="mabuse"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="mabuse"))
async def fuckedd(abusehard):
    index = random.randint(0, len(ABUSEHARD_STRING) - 1)
    reply_text = ABUSEHARD_STRING[index]
    await abusehard.edit(reply_text)


@telebot.on(admin_cmd(outgoing=True, pattern="mruns"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="mruns"))
async def fuckedd(abusehard):
    index = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[index]
    await abusehard.edit(reply_text)


@telebot.on(admin_cmd(outgoing=True, pattern="minsult$"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="minsult$"))
async def proo(pros):
    index = random.randint(0, len(PRO_STRINGS) - 1)
    reply_text = PRO_STRINGS[index]
    await pros.edit(reply_text)


@telebot.on(admin_cmd(pattern=r"foryou$", outgoing=True))
@telebot.on(sudo_cmd(pattern=r"foryou$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await eor(event, "For you❤️...")
    await asyncio.sleep(2)
    x = random.randrange(1, 33)
    if x == 1:

        await eor(event, 
            "💑ആത്മാർത്ഥ കൂടുതൽ എവിടെ കാട്ടിയോ അവിടെ നിന്നായിരിക്കും ഏറ്റവും കൂടുതൽ അവഗണന💔🚶🚶"
        )

    if x == 2:

        await eor(event, 
            "നെഞ്ചിൽ ഒരു നീറ്റൽ അവശേഷിപ്പിക്കാതെ ഒരു പ്രണയവും ഇറങ്ങി പോകുന്നില്ല... അങ്ങനെ അല്ലെങ്കിൽ അത് പ്രണയവും അല്ല💘💘!"
        )

    if x == 3:

        await eor(event, 
            "ചില ഇഷ്ട്ടങ്ങൾ ഉണ്ട്, ഇഷ്ട്ടപെടരുതെന്നു അറിഞ്ഞിട്ടും ഇഷ്ട്ട പെട്ടു പോയതാണ😇😇💞്..."
        )

    if x == 4:

        await eor(event, 
            "സ്വന്തമെന്നു കരുതി അഹങ്കരിക്കുന്ന നിയഴലും സൂര്യന്റെ ഔദാര്യമാണ്.😅😅"
        )

    if x == 5:

        await eor(event, 
            "നിന്നോട് വഴക്കിടാൻ എനിക്ക് ഇഷ്ട്ടമായിരുന്നു, അപ്പോഴെല്ലാം നിന്നോടുള്ള സ്നേഹം കൂടി വന്നു... എന്നിട്ടും നീ എന്തെ എന്നെ മനസിലാകാതെ പോയെ😪😪😪....????"
        )

    if x == 6:

        await eor(event, 
            "പൊന്നിട്ട് മൂടും എന്ന് പറയുന്നില്ല.... എന്നാൽ മണ്ണിട്ട് മൂടും വരെ കൂടെ ഉണ്ടാവും..😍😍."
        )

    if x == 7:

        await eor(event, 
            "കൊണ്ട് പോകുവാൻ ഒന്നുമില്ല ഈ ലോകത്ത്... കൊടുത്ത് പോവാൻ സ്നേഹവും സൗഹൃദവും മാത്രം😉😉🙃."
        )

    if x == 8:

        await eor(event, 
            "നിന്നിൽ ഞാൻ ഇനിയും പെയ്യും.. നിന്നെ നനച്ചു.. നിന്റെ ആത്മാവിനെ നെഞ്ചോടു ചേർക്കും.. ഒടുവിൽ ഞമ്മൾ ഒരു മഴയായി തീരും, ഒരുമിച്ച് പെയ്യും.❣️❣️💓💕"
        )

    if x == 9:

        await eor(event, 
            "കാലം എന്നെ നിനക്ക് മുന്നിൽ എത്തിച്ചു എങ്കിൽ, എന്റെ മരണം വരെ ഞാൻ നിന്റെ കൂടെ ഉണ്ടാവും നീയായി എന്നെ വെറുത്തില്ലെങ്കിൽ മാത്രം💘💘"
        )

    if x == 10:

        await eor(event, 
            "എന്റെ പ്രണയം അസ്തമിക്കുകയില്ല..🌅. എന്റെ ഓർമകളുടെ ചെരുവിലെ സ്വപ്നങ്ങളും നിറങ്ങളും ഞാനും മായും വരെ..✨️✨️."
        )

    if x == 11:

        await eor(event, 
            "എന്റെ ജീവിതം തുടങ്ങിയത് നിന്നോടൊപ്പം അല്ല പക്ഷെ എനിക്ക് ഉറപ്പുണ്ട് എന്റെ ജീവിതത്തിനു ഒരു അവസാനം ഉണ്ടെങ്കിൽ അത് നിന്നോട് ഒപ്പം ആയിരിക്കും, ആ അവസാന നിമിഷം വരെ ഞാൻ ഉണ്ടാവും നിന്റെ കൂടെ.💑💑.."
        )

    if x == 12:

        await eor(event, 
            "നീണ്ട കാത്തിരിപ്പിന് ഞാൻ തയാറാണ് കാലമേ.. മറ്റൊരു ഹൃദയം പകരം തന്ന് തൃപ്തി പെടുത്തരുത്.. നീണ്ട മുടിയിഴകൾ വെള്ളനൂൽ ആയി മാറിയേക്കാം.. നനുത്ത വിരലുകൾ വരണ്ടു ചുളുങ്ങിയേക്കാം.. മിഴികൾ അന്ധത കൂട്ട് പിടിച്ചേക്കാം.. അപ്പോഴും എന്റെ ഹൃദയം ആ ഓർമകളിൽ ചുവന്നു താനെയിരിക്കും.. അത് കൊണ്ട് നീ എനിക്കായി എന്തെകിലും തരാൻ ബാക്കി വച്ചിട്ടുണ്ടെങ്കിൽ അവളെ തന്നെ തരിക.. എന്റെ പ്രണയത്തെ..👫👫💝"
        )

    if x == 13:

        await eor(event, 
            "സ്നേഹിക്കണം, ചതിക്കുന്നവരെയല്ല അവഗണിക്കുന്നവരെയും അല്ല, ചങ്ക് പറിച്ചു തരുന്നവരെ ഞമ്മുടെ കണ്ണ് നിറഞ്ഞാൽ ഉള്ളു പിടയുന്നവരെ.💘💘."
        )

    if x == 14:

        await eor(event, 
            "കാണാൻ കൊതിക്കുന്ന മുഖവും.. കേൾക്കാൻ കൊതിക്കുന്ന ശബ്ദവും ഒരുപാട് അകലെ ആയിരിക്കുമ്പോൾ, സ്നേഹം ഒരു നൊമ്പരം മാത്രമാണ്.💔💔💔."
        )

    if x == 15:

        await eor(event, 
            "തിരക്ക് ഇല്ലങ്കിലും ചിലർ തിരക്കിൽ ആയിരിക്കും, എങ്ങനെ എങ്കിലും ഞമ്മുടെ മുന്നിൽ നിന്നും ഒഴിഞ്ഞു മാറി നിൽക്കാൻ.😣😣😣😖."
        )

    if x == 16:

        await eor(event, 
            "ജീവിതത്തിന്റെ ഇരുൾ അടഞ്ഞ വഴികളിലൂടെ ഒറ്റയ്ക്കു നടക്കുമ്പോൾ ചേർത്ത് പിടിക്കാൻ കിട്ടുന്ന കൈകളുടെ കരുത്ത് നോക്കാറില്ല ആരും.🤝🤝👫👬👭."
        )

    if x == 17:

        await eor(event, 
            "ഒരു പെൺകുട്ടി ആത്മാർഥമായി നിങ്ങളെ പ്രണയിക്കുന്നുണ്ടെങ്കിൽ.. അവൾ നിങ്ങളോട് ഒരുപാട് കാര്യങ്ങൾക് ദേഷ്യപ്പെടും💑❣️.."
        )

    if x == 18:

        await eor(event, 
            "നടക്കില്ല നടക്കില്ല എന്ന് വിചാരിച്ചാൽ ലോകത്ത് ഒരു കാര്യാവും നടക്കില്ല.. എന്നാൽ നടക്കും നടക്കും എന്ന് വിചാരിച്ചിട്ടിറങ്ങിയാൽ നടക്കാതെ കാര്യവും ഇല്ലാ 😅😇.."
        )

    if x == 19:

        await eor(event, 
            "മനസ് വിതുമ്പുന്ന സമയത്തും ചിരിക്കാൻ കഴിയുന്നത് ഭാഗ്യമാണ്, ഒരു വരദാനമാണ്.☺️☺️.. ഒന്നും ഇല്ലാത്തവർക്ക് ദൈവത്തിന്റെ സമ്മാനമാണ് അങ്ങനെ ചിരിക്കാൻ ഉള്ള കഴിവ്.☺️☺️😇."
        )

    if x == 20:

        await eor(event, 
            "കൈ തട്ടി ഫോണിലോട്ടു നോക്കിയപ്പോൾ ഒരു മൊഞ്ചുള്ള മുഖം, അപ്പൊ മനസിലായി കൈ തട്ടി ഫ്രണ്ട് ക്യാമറ ഓൺ ആയതാണെന്നു..🙈🙈🙈"
        )

    if x == 21:

        await eor(event, 
            "ജീവിതത്തിൽ ആരെയും വിലകുറച്ചു കാണരുത്. ഓർക്കുക, നിലച്ചു പോയ ഘടികാരവും ദിവസത്തിൽ രണ്ടു പ്രാവിശ്യം യഥാർത്ഥ സമയം കാണിച്ച് തരുന്നു.⌚️⌚️. "
        )

    if x == 22:

        await eor(event, 
            "ആരെയും പരിഹസിക്കരുത് സ്വന്തം സുഹൃത്തായാൽപോലും.. ന്യൂനതകൾ ഇല്ലാത്ത മനുഷ്യർ ഇല്ല.. എല്ലാം തികഞ്ഞവരായി മനുഷ്യനെ സൃഷ്ടിച്ചിട്ടുമില്ല..💞☺️"
        )

    if x == 23:

        await eor(event, 
            "നിന്നെ പരിചയപെട്ടപ്പോഴോ.. നിന്നോട് സംസാരിച്ചു തുടങ്ങിയപ്പോഴോ ഞാൻ അറിഞ്ഞില്ല.. നീയെന്റെ ഹൃദയത്തിലോട്ട് ഒരു ടിക്കറ്റ് എടുക്കുമെന്ന് ഈ ടിക്കറ്റ് വച്ച് അടുത്ത സ്റ്റോപ്പിൽ ആണോ.. അതോ അവസാന സ്റ്റോപ്പിൽ ഇറങ്ങുക, അത് വ്യക്തമല്ല.. എന്നാലും ഞാൻ നിന്നെ ഒരുപാട് സ്നേഹിക്കുന്നു..😇💓💖"
        )

    if x == 24:

        await eor(event, 
            "എന്റെ സ്വപ്നങ്ങളിൽ നിറയുന്നത് നിന്റെ മുഖം മാത്രം.. നീ എനിക്ക് എന്ത്ര പ്രിയ പെട്ടതാണെന്ന് പറയാൻ എനിക്ക് വാക്കുകൾ ഇല്ല.. എന്ത്ര കാലം വേണമെങ്കിലും കാത്തിരിക്കാം ഞാൻ.. നീ എന്റേത്‌ മാത്രമാവുന്ന നിമിഷത്തിനായി💘💘.."
        )

    if x == 25:

        await eor(event, 
            "ഓരോ യാത്രയിലും അറിയാതെ നിന്നെ തിരയുന്നു ഞാൻ.. കൈവിട്ടു പോയ നിന്റെ കൈകളെ.. നിന്റെ ഓർമകളെ.💔☹️☹️😢."
        )

    if x == 26:

        await eor(event, "നിന്റെ ഇഷ്ട്ടങ്ങൾ തേടി എന്റെ ഇഷ്ടങ്ങൾ എല്ലാം നീയായി.❤️❤️..")

    if x == 27:

        await eor(event, 
            "ആകാശത്തിലെ നക്ഷത്രങ്ങളെയും, കടൽ തീരത്തെ മണൽ തരികളെയും എന്ന് ഞാൻ എണ്ണി തീർക്കുന്നോ അന്ന് ഞാൻ നിന്നെ മറക്കും.💘💘❤️❤️.."
        )

    if x == 28:

        await eor(event, 
            "മറക്കാൻ വയ്യ എന്ന് പറഞ്ഞ പലർക്കും ഇപ്പോൾ ഞമ്മളെ ഓർക്കാൻ വയ്യ എന്നാ അവസ്ഥയിലായി😊😊😊..."
        )

    if x == 29:

        await eor(event, 
            "ചിലർക്ക് ഞമ്മളാണ് ഏറ്റവും പ്രിയപ്പെട്ടത് എന്ന് കരുതുന്നുവെങ്കിലും...... അവർക്ക് പ്രിയം ഞമ്മളെ കാൾ മറ്റുള്ളവരോടാണ്, എന്നാ തിരിച്ചറിവ്.... വല്ലാത്ത നൊമ്പരം തന്നെയാണ്................ എന്നും.......... എപ്പോഴും 😊😊😭😭......."
        )

    if x == 30:

        await eor(event, 
            "ഒരു പ്രണയം ഉണ്ടായിരുന്നു അത് ഞാൻ പഠിക്കാതെ എഴുതിയ പരീക്ഷ പോലെ തോറ്റു പോയി. കുറച്ച് ഓർമ്മകൾ ഉണ്ടായിരുന്നു അത് ഞാൻ ദൂരെ കടലിൽ ഒഴുകി കളഞ്ഞിട്ടും വീണ്ടും മഴയായി അത് എന്റെ മേൽ പെയ്യുന്നു. പിന്നെ ഉള്ളത് അല്പം വേദനയാണ്, അത് അണയാതെ, കളയാതെ ഒരു കനലായി നോവായി മനസ്സിൽ ഇപ്പോഴും കൊണ്ട് നടക്കുന്നു.🚶‍♂️🚶‍♂️."
        )

    if x == 31:

        await eor(event, 
            "ദിവസവും ഒരുപാട് പെൺകുട്ടികളെ കാണാറുണ്ട്, അവരോട് ആരോടും ഇത് വരെ ഒരു ഇഷ്ട്ടം തോന്നിട്ടില്ല. കാരണം, എന്റെ പെണ്ണിന് എന്നിലൊരു വിശ്വാസമുണ്ട്. അത് തകർക്കാൻ എനിക്ക് ഈ ജന്മം കഴിയില്ല❤️❤️💘.."
        )

    if x == 32:

        await eor(event, 
            "സ്നേഹം... അത് കൈകുമ്പിളിൽ കോരി എടുക്കാനോ തട്ടി എടുക്കാനോ കഴിയില്ല, അത് ഹൃദയത്തിൽ നിന്നും ഹൃദയത്തിലേക്കു പകർന്നു നൽകുവാനേ കഴിയു.❤️❤️😇."
        )

    if x == 33:

        await eor(event, 
            "എന്റെ ഹൃദയത്തിൽ ചുവന്ന റോസാപുഷ്പ്പങ്ങൾ വളരുന്നുണ്ട്. പക്ഷെ, അവ ഒരിക്കലും കൊഴിയാറില്ല. കാരണം, ഞാൻ നിന്റെ പുഞ്ചിരി കാണുമ്പോഴും നിന്നെ കുറിച്ച് ചിന്തിക്കുമ്പോഴുമെല്ലാം അവ വിടരുന്നു☺️☺️.."
        )


@telebot.on(admin_cmd(outgoing=True, pattern="kozhi"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="kozhi"))
async def hating(hated):
    index = random.randint(0, len(HATE_STRINGS) - 1)
    reply_text = HATE_STRINGS[index]
    await hated.edit(reply_text)
