from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ⚠️ ЗАМЕНИТЕ URL НА ВАШ VERCEL URL!
TOKEN = os.environ.get('BOT_TOKEN', "8273729657:AAF0XR0g4fX7J3k9DVuW4Bfe5t5KafiwWQ8")
WEBAPP_URL = os.environ.get('WEBAPP_URL', "https://miner-frontend1.vercel.app")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("🚀 Играть в Минер", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"👋 Привет, {user.first_name}!\n\n"
        "🎮 Добро пожаловать в <b>Минер</b>!\n\n"
        "🎯 Правила игры:\n"
        "• Открывай клетки и избегай мин\n"
        "• С каждым ходом растет множитель\n"
        "• Забирай выигрыш в любой момент\n"
        "• Чем больше мин - тем выше множители!\n\n"
        "💰 Начальный баланс: <b>50 монет</b>\n\n"
        "🚀 Нажми кнопку ниже, чтобы начать игру!"
    )
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )
    
    logger.info(f"User {user.id} ({user.username}) started the bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "📖 <b>Помощь по игре Минер</b>\n\n"
        "🎮 <b>Как играть:</b>\n"
        "1. Выберите количество мин (3-24)\n"
        "2. Сделайте ставку (15-100 монет)\n"
        "3. Нажмите 'Старт'\n"
        "4. Открывайте безопасные клетки\n"
        "5. Забирайте выигрыш в любой момент\n\n"
        "⚠️ <b>Внимание:</b>\n"
        "• Если откроете мину - проиграете\n"
        "• Чем больше мин, тем выше множители\n"
        "• Множитель растет с каждым ходом\n\n"
        "💡 <b>Совет:</b> Начните с 3-6 мин для изучения игры\n\n"
        "🎮 /start - Начать игру"
    )
    
    await update.message.reply_text(help_text, parse_mode='HTML')

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    stats_text = (
        "📊 <b>Статистика</b>\n\n"
        "Для просмотра статистики откройте игру.\n"
        "Ваш баланс и история игр сохраняются автоматически.\n\n"
        "🎮 /start - Играть"
    )
    
    await update.message.reply_text(stats_text, parse_mode='HTML')

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("stats", stats_command))
        
        logger.info("🤖 Бот успешно запущен!")
        logger.info(f"📱 WebApp URL: {WEBAPP_URL}")
        
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Ошибка запуска бота: {e}")
        raise

if __name__ == '__main__':

    main()
