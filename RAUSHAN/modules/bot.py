import sys
import os
import json

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, get_sudo_users, reload_sudo_users, is_sudo, add_sudo_user, remove_sudo_user, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


def sudo_only(func):
    """Decorator to check if user is sudo"""
    async def wrapper(event):
        if is_sudo(event.sender_id):
            await func(event)
        else:
            await event.reply("**🚫 You are not authorized to use this command!**")
    return wrapper


def owner_only(func):
    """Decorator to check if user is owner"""
    async def wrapper(event):
        if event.sender_id == OWNER_ID:
            await func(event)
        else:
            await event.reply("**🚫 Only Owner can use this command!**")
    return wrapper


# Ping command - working example
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@sudo_only
async def ping(e):
    start = datetime.now()
    altron = await e.reply(f"•[ 🍹ᴀʟᴘʜᴀ тум 🍹 ]•")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await altron.edit(f"[🍹] 𝐀ʟᴘʜᴀ ᴘαᴘα ɪѕ нєʀє\n[🏓] αвє αв тєʀα куα нσgα\n[⚡] кιѕкι ᴄнυ∂αι кαʀиι нαι\n\n➜ `{mp} ms`")


# Restart command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@sudo_only
async def restart(e):
    await e.reply(f"ʀєвσσт ᴅσиє\n[🍷] 2 мιит ωαιт ᴘℓєαѕє\n[🫧] fιʀ ααʏєɢα тєʀɪ мᴀᴀ ᴄнσᴅиє ᴀʟᴘʜᴀ ʙᴀʙʏ ")
    try:
        await X1.disconnect()
    except Exception:
        pass
    try:
        await X2.disconnect()
    except Exception:
        pass
    try:
        await X3.disconnect()
    except Exception:
        pass
    try:
        await X4.disconnect()
    except Exception:
        pass
    try:
        await X5.disconnect()
    except Exception:
        pass
    try:
        await X6.disconnect()
    except Exception:
        pass
    try:
        await X7.disconnect()
    except Exception:
        pass
    try:
        await X8.disconnect()
    except Exception:
        pass
    try:
        await X9.disconnect()
    except Exception:
        pass
    try:
        await X10.disconnect()
    except Exception:
        pass

    execl(sys.executable, sys.executable, *sys.argv)


# Add sudo command - Owner only
@X1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@owner_only
async def addsudo(event):
    ok = await event.reply(f"»🍃 ᴀʟᴘʜᴀ ᴋᴀ єк σʀ иєω вєтα αᴅᴅ нσ gуα 🍃")
    target = ""
    try:
        reply_msg = await event.get_reply_message()
        target = reply_msg.sender_id
    except:
        await ok.edit("αвє ᴊʜᴀᴛ кє вααℓ υραʀ ѕє ʀєᴘℓу ᴅє ʀαнα нαι вααᴘ кσ")
        return

    if is_sudo(target):
        await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
    else:
        if add_sudo_user(target):
            reload_sudo_users()  # Reload the sudo list
            await ok.edit(f"» σує нσує мєʀα ᴄυтє вαᴄнα\n:⧽ `{target}`\n:⧽ `ωєℓᴄσмє тσ ᴀʟᴘʜᴀ ѕραм`")
        else:
            await ok.edit("**❌ Failed to add sudo user!**")


# Remove sudo command - Owner only
@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@owner_only
async def rmsudo(event):
    try:
        reply_msg = await event.get_reply_message()
        target = reply_msg.sender_id
    except:
        await event.reply("αвє ᴊʜᴀᴛ кє вααℓ υραʀ ѕє ʀєᴘℓу ᴅє ʀαнα нαι вααᴘ кσ")
        return

    if not is_sudo(target):
        await event.reply(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
    else:
        if remove_sudo_user(target):
            reload_sudo_users()  # Reload the sudo list
            await event.reply(f"**✅ Removed** `{target}` **from sudo users!**")
        else:
            await event.reply("**❌ Failed to remove sudo user!**")


# Sudo list command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@sudo_only
async def sudolist(event):
    current_sudo = get_sudo_users()
    sudo_list = "**📋 Current Sudo Users:**\n\n"
    for user_id in current_sudo:
        sudo_list += f"• `{user_id}`\n"
    
    sudo_list += f"\n**Total:** `{len(current_sudo)}` users"
    await event.reply(sudo_list)


# Check sudo command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%schecksudo(?: |$)(.*)" % hl))
async def checksudo(event):
    user_id = event.sender_id
    if is_sudo(user_id):
        await event.reply(f"**✅ Yes!** User `{user_id}` is a sudo user!")
    else:
        await event.reply(f"**❌ No!** User `{user_id}` is not a sudo user!")


# Test command - for testing sudo access
@X1.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%stest(?: |$)(.*)" % hl))
@sudo_only
async def test_cmd(event):
    await event.reply("**✅ Sudo access confirmed!** You can use this command!")
