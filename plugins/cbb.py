from pyrogram import filters
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import UPI_QR_CODE_URL, OWNER_ID

# A dictionary to track users awaiting payment confirmation
#awaiting_payment_confirmation = {}


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id

    if data == "about":
        await query.message.edit_text(
            text=f"<b>Language : Python3</b>\n"
                 f"<b>Library : pyrogram</b>\n"
                 f"<b>Version : v7 </b>\n"
                 f"<b>Developer : @StupidBoi69</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📴 Close", callback_data="close")]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif data == "upi":
        # When the user clicks "Pay via UPI", send the UPI QR code and ask for payment confirmation
        await client.send_photo(
            chat_id=query.from_user.id,
            photo=UPI_QR_CODE_URL,
            caption="<blockquote><b>Please scan the QR code to make the payment. After the payment, send the payment receipt or a screenshot to owner</b></blockquote>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👑 Bot Owner", url=f"https://t.me/StupidBoi69")],
                    [InlineKeyboardButton("📴 Close", callback_data="close")]
                ]
            )
        )

    elif data == "premium":
        await query.message.edit_text(
            text=f"<b>⏺️ Hello {query.from_user.mention}, Please choose a plan:</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🥉 Bronze tier", callback_data="bronze"),
                     InlineKeyboardButton("🥈 Silver tier", callback_data="silver")],
                    [InlineKeyboardButton("🥇 Gold tier", callback_data="gold"),
                     InlineKeyboardButton("🏆 Platinum tier", callback_data="platinum")],
                    [InlineKeyboardButton("📴 Close", callback_data="close")]
                ]
            )
        )

    elif data == "bronze":
        await query.message.edit_text(
            text="<b>Bronze tier: ₹30 for 1 week</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Pay via UPI", callback_data="upi")],
                    [InlineKeyboardButton("⬅️ Back", callback_data="premium"),
                     InlineKeyboardButton("Next ➡️", callback_data="silver")],
                    [InlineKeyboardButton("📴 Cancel", callback_data="close")]
                ]
            )
        )

    elif data == "silver":
        await query.message.edit_text(
            text="<b>Silver tier: ₹99 for 1 month</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Pay via UPI", callback_data="upi")],
                    [InlineKeyboardButton("⬅️ Back", callback_data="bronze"),
                     InlineKeyboardButton("Next ➡️", callback_data="gold")],
                    [InlineKeyboardButton("📴 Cancel", callback_data="close")]
                ]
            )
        )

    elif data == "gold":
        await query.message.edit_text(
            text="<b>Gold tier: ₹249 for 3 months</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Pay via UPI", callback_data="upi")],
                    [InlineKeyboardButton("⬅️ Back", callback_data="silver"),
                     InlineKeyboardButton("Next ➡️", callback_data="platinum")],
                    [InlineKeyboardButton("📴 Cancel", callback_data="close")]
                ]
            )
        )

    elif data == "platinum":
        await query.message.edit_text(
            text="<b>Platinum tier: ₹500 for 6 months</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Pay via UPI", callback_data="upi")],
                    [InlineKeyboardButton("⬅️ Back", callback_data="gold"),
                     InlineKeyboardButton("📴 Cancel", callback_data="close")]
                ]
            )
        )



    """

    elif data == "upi":
        # When the user clicks "Pay via UPI", send the UPI QR code and ask for payment confirmation
        await client.send_photo(
            chat_id=query.from_user.id,
            photo=UPI_QR_CODE_URL,
            caption="Please scan the QR code to make the payment. After the payment, send the payment receipt or a screenshot here."
        )
        # Track the user in the payment confirmation dictionary
        awaiting_payment_confirmation[user_id] = True


@Bot.on_message(filters.photo | filters.text)
async def handle_message(client, message):
    user_id = message.from_user.id

    # Check if the user is in the payment confirmation list
    if user_id in awaiting_payment_confirmation:
        if message.photo:
            # Forward the payment confirmation photo to the bot owner
            await client.send_message(
                BOT_OWNER_ID,
                f"Payment confirmation from {message.from_user.mention} (ID: {user_id}):"
            )
            await message.forward(BOT_OWNER_ID)

            # Notify the user that their payment has been forwarded
            await message.reply("Thank you! Your payment confirmation has been submitted for review. You will be notified once it has been verified.")

        elif message.text:
            # Forward the payment confirmation message to the bot owner
            await client.send_message(
                BOT_OWNER_ID,
                f"Payment confirmation message from {message.from_user.mention} (ID: {user_id}): {message.text}"
            )

            # Notify the user that their payment has been forwarded
            await message.reply("Thank you! Your payment confirmation has been submitted for review. You will be notified once it has been verified.")

        # Remove the user from the payment confirmation list
        awaiting_payment_confirmation.pop(user_id, None)

    else:
        # If the user is not in the payment confirmation flow
        await message.reply("Please select a plan and proceed with the payment.")

"""
