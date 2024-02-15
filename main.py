import re
import requests
from aiogram import Dispatcher, Bot
from aiogram import types

from config import TOKEN
import asyncio
import logging
from aiogram.filters import Command

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("salom!")


@dp.message(Command("video"))
async def video(message: types.Message):
    await message.answer_document(
        "https://redirector.googlevideo.com/videoplayback?expire=1707939096&ei=uMDMZZSFCuaPlu8P58yS-AY&ip=198.98.59.215&id=o-AJy-8qj_X3xwR-9-TMlu2p1o6wywdf3GfAXpdegRQ7Em&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=fj&mm=31%2C26&mn=sn-5uaeznsl%2Csn-p5qlsn6l&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=107500&siu=1&spc=UWF9fyncw18IKr-6VLbTsnQFWLosDCwZTF5Y-QFmQcgFQtMfk3Dr0cnYqBsC&vprv=1&svpuc=1&mime=video%2Fmp4&ns=XZ3Sy1IHiRggaE77AxnMqeYQ&cnr=14&ratebypass=yes&dur=172.570&lmt=1665570863117839&mt=1707916876&fvip=3&fexp=24007246&c=WEB&sefc=1&txp=4538434&n=bKakX_BgAlZq2g&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Csiu%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRAIgL28UDHL5HmarXe0G4l8_51GNPTVgSV4TlMRj8Rahkx0CIAyyxHQNUJN6DaZ7gGsFPGi8yJ7yWw4vWkB6Dij5au_1&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=APTiJQcwRgIhALM07inbHJyO7X3HokzDf4LaIjiVjECNSo0-077a-zEUAiEA9NcpIZUgSLW7gmmSJWKV22fqVn2TnryCr78syZqYLrA%3D&range=0-")


@dp.message()
async def send_url(message: types.Message):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": message.text}

    headers = {
        "X-RapidAPI-Key": "5fdb52baf6mshf5d86ef5e45ac55p17ca97jsn40b14a84c093",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()

    video = response.json().get('videos', [])

    video_url = video["items"][1].get("url", None)
    await message.answer_video(video_url)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())






