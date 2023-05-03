from aiogram import Bot, Dispatcher, executor, types
import config
import datetime
import queries

# Get TOKEN
bot = Bot(token=config.TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot)


# Start bot for trigger /start
@dispatcher.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply("Привет!\n\nОтправь дату, за которую нужно собрать статистику в формате ГГГГ-ММ-ДД")


# Send statisctics
@dispatcher.message_handler(content_types=['text'])
async def response_message(message: types.Message):
    try:
        # Generate date for query
        date = datetime.datetime.strptime(message.text, '%Y-%m-%d').date()

        # Execute queries
        # GET users info
        count_users = queries.get_count('users', date)
        all_users = queries.get_count('users')

        # GET clubs info
        count_clubs = queries.get_count('clubs', date)
        all_clubs = queries.get_count('clubs')

        # GET club subscribers info
        count_sub = queries.get_count('user_clubs', date)
        all_sub = queries.get_count('user_clubs')

        # GET posts info
        count_posts = queries.get_count('posts', date)
        all_posts = queries.get_count('posts')

        # GET photos info
        count_photos = queries.get_count('uploads', date)
        all_photos = queries.get_count('uploads')

        # GET likes info
        count_likes = queries.get_count('likes', date)
        all_likes = queries.get_count('likes')

        # GET comments info
        count_comments = queries.get_count('comments', date)
        all_comments = queries.get_count('comments')

        # Send stats
        await message.reply(f"\n"
                            f"        Статстика за {date}:\n"
                            f"        - новых пользователей {count_users}\n"
                            f"        - всего пользователей {all_users}\n"
                            f"\n"
                            f"        - новых клубов {count_clubs}\n"
                            f"        - всего клубов {all_clubs}\n"
                            f"\n"
                            f"        - новых подписчиков {count_sub}\n"
                            f"        - всего подписчиков {all_sub}\n"
                            f"\n"
                            f"        - новых постов {count_posts}\n"
                            f"        - всего постов {all_posts}\n"
                            f"\n"
                            f"        - новых фотографий загружено пользователями {count_photos}\n"
                            f"        - всего фотографий загружено пользователями {all_photos}\n"
                            f"\n"
                            f"        - новых лайков {count_likes}\n"
                            f"        - всего лайков {all_likes}\n"
                            f"\n"
                            f"        - новых комментариев {count_comments}\n"
                            f"        - всего комментариев {all_comments}\n"
                            f"\n")
    except ValueError:
        # if user request text not valid
        await message.reply("Проверь формат даты и попробуй еще раз :)")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)

