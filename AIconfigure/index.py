# coding=utf-8
import time

import do

global content  # 内容
global msg  # 要发送的消息


def sign():
    try:
        # 早安
        do.send_msg("嘉桐一号前来播报！")
        time.sleep(5)
        do.send_msg(do.morning(time.localtime().tm_hour, '5ca24f4c5c87879182b6c48d8352e0c2'))
        # 天气
        weather_msg = do.make_msg_weather_details(day=0)
        # 发送天气
        do.send_msg(weather_msg)

        print("天气播报完毕")
        time.sleep(5)

        # 情话
        """love_msg = do.love_msg('5ca24f4c5c87879182b6c48d8352e0c2')
        do.send_msg(love_msg)
        print("情话发送完成")
        time.sleep(5)"""
        # 电影台词
        film = do.film('5ca24f4c5c87879182b6c48d8352e0c2')
        film_msg = f"经典台词：\n {film['dialogue']} \n {film['english']} \n --{film['source']}"
        do.send_msg(film_msg)
        print("电影台词发送完成")
        time.sleep(5)
        # 诗句
        ancient_poetry = do.ancient_poetry('5ca24f4c5c87879182b6c48d8352e0c2')
        ancient_poetry_msg = f"今日古诗: \n《{ancient_poetry['source']}》 \n {ancient_poetry['cont']} \n --{ancient_poetry['author']}"
        do.send_msg(ancient_poetry_msg)
        print("每日诗句播报完毕")
        time.sleep(5)

        # 英语

        english = do.english_msg('5ca24f4c5c87879182b6c48d8352e0c2')
        englist_msg = f"每日一句英语:\n {english['zh']} \n {english['en']}"
        do.send_msg(englist_msg)
        print('每日英语播报完毕')
        time.sleep(5)

        # 彩虹屁
        chp = do.chp('5ca24f4c5c87879182b6c48d8352e0c2')
        chp_msg = f"夸夸今天的小嘉桐：\n {chp}"
        do.send_msg(chp_msg)
        print("彩虹屁发送完成")
        time.sleep(5)

        do.send_msg("嘉桐一号播报完啦，小嘉桐俺撤啦")
        print("信息全部投递完成~~")
        return True
    except Exception as e:
        print(f"出错了 错误信息是{e}")
        return False


def main():
    sign()


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
