from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from bot.storage import add_puff, get_stats

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("➕ Сделать тягу", callback_data="add_puff"),
        InlineKeyboardButton("📊 Статистика", callback_data="show_stats")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Йо! Это твой трекер 🚬", reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = str(query.from_user.id)

    if query.data == "add_puff":
        add_puff(user_id)
        await query.edit_message_text("✅ Тяга добавлена!")
    elif query.data == "show_stats":
        stats = get_stats(user_id)
        await query.edit_message_text(f"📊 Твои тяги:\nСегодня: {stats['today']}\nВсего: {stats['total']}")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
