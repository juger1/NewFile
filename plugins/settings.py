import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from bot import Bot
from config import ADMINS, USE_PAYMENT
from database.database import add_admin, del_admin, full_adminbase, present_admin
from helpers_func import *

# Settings command handler
@Bot.on_message(filters.command('settings') & filters.private & filters.user(ADMINS))
async def settings_command(client: Bot, message: Message):
    buttons = [
        [
            InlineKeyboardButton("Add Admin", callback_data="add_admin"),
            InlineKeyboardButton("Remove Admin", callback_data="remove_admin"),
        ],
        [
            InlineKeyboardButton("Show Admins", callback_data="show_admin"),
            InlineKeyboardButton("Add Premium User", callback_data="add_premium"),
        ],
        [
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply("Choose an option:", reply_markup=reply_markup)

# Callback query handler for settings
@Bot.on_callback_query()
async def callback_query_handler(client: Bot, callback_query):
    action = callback_query.data
    message = callback_query.message

    if action == "add_admin":
        await add_admin_process(client, message)
    elif action == "remove_admin":
        await remove_admin_process(client, message)
    elif action == "show_admin":
        await show_admins_process(client, message)
    elif action == "add_premium":
        await add_premium_process(client, message)
    elif action == "cancel":
        await message.reply("Process cancelled. 🛑")
        return  # Exit the callback function

    # Acknowledge the callback query
    await callback_query.answer()

async def add_admin_process(client: Bot, message: Message):
    while True:
        try:
            # Ask for user ID
            admin_id = await client.ask(
                text="Enter user ID to add as admin\nHit /cancel to cancel", 
                chat_id=message.from_user.id, 
                timeout=60
            )
        except Exception:
            return
        
        if admin_id.text.lower() == "/cancel":
            await admin_id.reply("Cancelled 😉!")
            return
        
        if not admin_id.text.isdigit():
            await admin_id.reply("❌ Error 😖\n\nPlease enter a valid numeric user ID.", quote=True)
            continue
        
        try:
            await client.get_users(user_ids=admin_id.text)
            break
        except Exception:
            await admin_id.reply("❌ Error 😖\n\nThe user ID is incorrect.", quote=True)
            continue

    if not await present_admin(int(admin_id.text)):
        try:
            await add_admin(int(admin_id.text))
            await message.reply(f"<b>Admin {admin_id.text} added successfully</b>")
            try:
                await client.send_message(
                    chat_id=admin_id.text,
                    text="You are now an admin! Ask the owner to add you to the required channels. 😁"
                )
            except Exception:
                await message.reply("Failed to notify the user. Ensure they have started the bot. 🥲")
        except Exception:
            await message.reply("Failed to add admin. 😔\nSome error occurred.")
    else:
        await message.reply("Admin already exists. 💀")

async def remove_admin_process(client: Bot, message: Message):
    while True:
        try:
            # Ask for user ID
            admin_id = await client.ask(
                text="Enter user ID to remove as admin\nHit /cancel to cancel", 
                chat_id=message.from_user.id, 
                timeout=60
            )
        except Exception:
            return
        
        if admin_id.text.lower() == "/cancel":
            await admin_id.reply("Cancelled 😉!")
            return
        
        if not admin_id.text.isdigit():
            await admin_id.reply("❌ Error 😖\n\nPlease enter a valid numeric user ID.", quote=True)
            continue
        
        try:
            await client.get_users(user_ids=admin_id.text)
            break
        except Exception:
            await admin_id.reply("❌ Error 😖\n\nThe user ID is incorrect.", quote=True)
            continue

    if await present_admin(int(admin_id.text)):
        try:
            await del_admin(int(admin_id.text))
            await message.reply(f"<b>Admin {admin_id.text} removed successfully 😀</b>")
        except Exception:
            await message.reply("Failed to remove admin. 😔\nSome error occurred.")
    else:
        await message.reply("Admin doesn't exist. 💀")

async def show_admins_process(client: Bot, message: Message):
    admin_list = await full_adminbase()
    if not admin_list:
        await message.reply("No admins found.")
    else:
        await message.reply(f"<b>Full admin list 📃\n\n{admin_list}</b>", parse_mode='html')

async def add_premium_process(client: Bot, message: Message):
    if USE_PAYMENT:
        while True:
            try:
                user_id = await client.ask(
                    text="Enter user ID for premium membership\nHit /cancel to cancel", 
                    chat_id=message.from_user.id, 
                    timeout=60
                )
            except Exception:
                return  
            if user_id.text.lower() == "/cancel":
                await user_id.reply("Cancelled 😉!")
                return
            
            if not user_id.text.isdigit():
                await user_id.reply("❌ Error\n\nThe user ID is incorrect. Please enter a valid numeric user ID.", quote=True)
                continue
            
            try:
                await client.get_users(user_ids=int(user_id.text))
                break
            except Exception:
                await user_id.reply("❌ Error\n\nThe user ID is incorrect.", quote=True)
                continue

        user_id = int(user_id.text)
        while True:
            try:
                timeforprem = await client.ask(
                    text="""<blockquote><b>👛 Enter the amount of time you want to provide the premium user</b></blockquote>
<b>(Note: Choose correctly, it's not reversible.)

Enter 1 for One-time verification
Enter 2 for One week
Enter 3 for One month
Enter 4 for Three months
Enter 5 for Six months</b>""", 
                    chat_id=message.from_user.id, 
                    timeout=60
                )
            except Exception:
                return

            if timeforprem.text.lower() == "/cancel":
                await timeforprem.reply("Cancelled 😉!")
                return

            if not timeforprem.text.isdigit() or int(timeforprem.text) not in [1, 2, 3, 4, 5]:
                await message.reply("You have given wrong input. 😖")
                continue
            else:
                break
        
        timeforprem = int(timeforprem.text)
        timestring = {
            1: "One time verified",
            2: "One week",
            3: "One month",
            4: "Three months",
            5: "Six months"
        }[timeforprem]
        
        try:
            await increasepremtime(user_id, timeforprem)  # Function to increase premium time
            await message.reply("Premium added! 🤫")
            await client.send_message(
                chat_id=user_id,
                text=f"<b>👑 Update for you\n\nYou are added as a premium member for ({timestring}) 😃\n\nFeedback: @StupidBoi69</b>",
            )
        except Exception as e:
            print(e)
            await message.reply("Some error occurred.\nCheck logs.. 😖\nIf you got a premium added message, then it's ok.")
       
