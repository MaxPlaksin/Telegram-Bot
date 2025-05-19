import pandas as pd
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# --- Конфигурация ---
TOKEN = "Введи токен"  # Замените на реальный токен!
EXCEL_FILE = "price_autopiter.xlsx"  # Ваш Excel-файл

# --- Загрузка данных ---
def load_data():
    try:
        return pd.read_excel(EXCEL_FILE)
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return pd.DataFrame()

# --- Поиск ---
def search_in_excel(query):
    df = load_data()
    if df.empty:
        return None
    result = df[df.apply(lambda row: str(query).lower() in str(row).lower(), axis=1)]
    return result if not result.empty else None

# --- Обработка /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Бот для поиска в прайсе Автопитер.\n"
        "Введите номер детали, название или артикул:"
    )

# --- Обработка сообщений ---
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    result = search_in_excel(query)

    if result is not None:
        # Ограничим вывод, если много строк
        reply = f"✅ Найдено {len(result)} совпадений:\n"
        reply += result.head(10).to_string(index=False)
    else:
        reply = "❌ Ничего не найдено. Попробуйте другой запрос."

    await update.message.reply_text(reply)

# --- Запуск бота ---
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Бот запущен! Для остановки нажмите Ctrl+C")
    app.run_polling()

if __name__ == "__main__":
    main()
