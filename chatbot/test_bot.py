from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_db as tk
from dotenv import load_dotenv
import os
import gemini
import requests as req
from bs4 import BeautifulSoup as bs

load_dotenv()

tele_token = os.getenv("TELEGRAM_KEY")

TOKEN = tele_token



async def start(update, context):
    await update.message.reply_text("안녕하세요 저는 차단당한 박세찬입니다. 좀 도와주세요")

async def send_photo(update, context):
    photo_url = "https://search.pstatic.net/common?type=f&size=304x304&quality=95&direct=true&src=http%3A%2F%2Fshop1.phinf.naver.net%2F20200212_288%2F15814854698534uwpP_JPEG%2F43713fff.jpg"
    await update.message.reply_photo(photo=photo_url,caption="사진 이미지 불러왔어요~")

async def send_song(update, centext):
    song_url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    web = req.get(song_url,headers = headers)
    soup = bs(web.content, 'html.parser')
    title = soup.select('.wrap_song_info .rank01')[:20]
    name = soup.select('.checkEllipsis a')[:20]  # 20위까지 !!
    str = ''
    for i,(t,n) in enumerate(zip(title, name),1):
        str += f'{i}위 : {t.text.strip()} / {n.text}\n'
    mel0 = str
    mel = str +"\n"+"오늘자 멜론 차트입니다!"
    await update.message.reply_text(mel)
async def monitor_chat(update, context):
    user_text = update.message.text #감지된 메세지들
    chat_id = update.message.chat_id #메세지가 온 채팅방

    
    

    if "gpt" in user_text:
        res = gemini.aiai(user_text.replace("gpt",""))
        await context.bot.send_message(chat_id=chat_id,text=res) #parse_mode="MarkdownV2")
    elif "영화정보" in user_text: pass
        #await 영화정보 크롤링 함수 실행
    elif "사진줘" in user_text:
        await send_photo(update, context)
    elif "멜론차트" in user_text:
        await send_song(update, context)
    
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id=chat_id,text=res)
                break #한개의 키워드에만 작용

    
def main():
    app = Application.builder().token(TOKEN).build()
    #명령어 핸들러 추가
    app.add_handler(CommandHandler("start",start))
    #응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))
                    
    print("텔레그램 봇이 실행중입니다. 모니터링 중...")
    app.run_polling()

if __name__ == "__main__":
    main()
