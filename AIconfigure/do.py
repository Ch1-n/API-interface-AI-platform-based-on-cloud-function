# coding=utf-8

import requests
import json
import time


# 改进
# 天气提示语
# 天气图标
# 获取天气图标

# 用个数表示天气 注意 0 时
def make_weather_icon(weather_name):
    weather_msg = ''
    if '晴' in weather_name:
        weather_id = 74
        weather_msg = f'@face={weather_id}@'
    elif '多' or '阴' in weather_name:  # 多云 或者 阴天
        weather_id = 91
        weather_msg = f'@face={weather_id}@'
    elif '小' or '雨' or '阵' in weather_name:  # 小于 或者 雨
        weather_id = 90
        weather_msg = f'@face={weather_id}@'
    elif '大' or '暴' or '暴雨' in weather_name:  # 小雨 或者 雨
        weather_id = 90
        weather_msg = f'@face={weather_id}@ @face={weather_id}@ @face={weather_id}@'
    elif '雷电' or '雷' or '电' in weather_name:  # 雷电
        weather_id = 54
        weather_msg = f'@face={weather_id}@ @face={weather_id}@'
    return weather_msg


# 温度 判断
def tem_icon(tem_num):
    tem_num = int(tem_num)
    tem_msg = ''
    if tem_num <= 10:  # 冷
        tem_id = 1
        tem_msg = f'今天有点冷，小嘉桐注意保暖哦~~~~  @face={tem_id}@'
    elif 20 <= tem_num <= 25:
        tem_id = 21  # 晴天 温度适中
        tem_msg = f'小嘉桐这温度好凉爽啊~~ @face={tem_id}@'
    elif 25 < tem_num < 30:
        tem_id = 35  # 有点热哦
        tem_msg = f'小嘉桐今天有点热哦~~ @face={tem_id}@'
    elif tem_num > 30:
        tem_id = 34  # 有点热哦
        tem_msg = f'小嘉桐今天会很热哦~~ @face={tem_id}@'
    return tem_msg


# 天气提示
def set_weather_msg(weather_name_d, weather_name_n):
    weather_msg = ''
    if ('晴' or '晴天') in weather_name_d and ('多云' or '云' or '阴天') in weather_name_n:  # 晴转多云
        weather_msg = '[提示语]'
    elif ('晴' or '晴天') in weather_name_d and ('晴' or '晴天') in weather_name_n:  # 晴转多云
        weather_msg = '[提示语]'
    elif '小雨' in weather_name_d and ('晴' or '晴天') in weather_name_n:  # 晴转多云
        weather_msg = '[提示语]'
    elif '小雨' in weather_name_d and '小雨' in weather_name_n:  # 晴转多云
        weather_msg = '[提示语]'
    elif '小雨' in weather_name_d and '多云' in weather_name_n:  # 晴转多云
        weather_msg = '[提示语]'

    elif ('晴' or '晴天') in weather_name_d and '小雨' in weather_name_n:  # 晴转小雨
        weather_msg = '[提示语]'

    elif ('晴' or '晴天') in weather_name_d and '大雨' in weather_name_n:  # 晴转大雨
        weather_msg = '[提示语]'

    elif ('云' or '多云') in weather_name_d and ('晴天' or '晴') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    elif ('云' or '多云') in weather_name_d and ('云' or '多云') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    # 雷雨转晴
    elif ('雷' or '闪电' or '雷阵雨' or '雷阵') in weather_name_d and ('晴天' or '晴') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    elif ('雷' or '闪电' or '雷阵雨' or '雷阵') in weather_name_d and ('雷' or '闪电' or '雷阵雨' or '雷阵') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    # 阵雨转晴
    elif ('阵雨' or '阵') in weather_name_d and ('晴天' or '晴') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    elif ('阵雨' or '阵') in weather_name_d and ('阵雨' or '阵') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    # 大雨转晴
    elif ('大' or '大雨') in weather_name_d and ('晴天' or '晴') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'
    elif ('大' or '大雨') in weather_name_d and ('大' or '大雨') in weather_name_n:  # 多云转晴
        weather_msg = '[提示语]'

    return weather_msg


# 天气
def weather(address, key, day):  # day ：0 =今天 1 明天 2后天 （最大为2）
    url = f"https://free-api.heweather.com/s6/weather/forecast"
    content = {
        'day': '',  # 日期
        'city': '',  # 城市
        'province': '',  # 省份
        'cond_txt_d': '',  # 初始  初始 转 结束
        'cond_txt_d_icon': '',  # 初始 图标
        'cond_txt_n': '',  # 结束
        'cond_txt_n_icon': '',  # 结束 图标
        'cond_msg': '',  # 天气提示语
        'tmp_max': '',  # 最高温度
        'tmp_max_id': 0,  # 最高温度图标id
        'tmp_min': '',  # 最低温度
        'tmp_min_id': 0,  # 最低温度图标id
        'tmp_msg': ''  # 温度提示语
    }
    try:
        if day > 2:
            return '超出天数'
        dic = {
            'location': f'{address}',
            'key': f'{key}',
            'lang': 'zh'
        }
        req = requests.get(url=url, params=dic)

        req_json = req.json()
        content['city'] = req_json['HeWeather6'][0]['basic']['location']  # 城市
        content['province'] = req_json['HeWeather6'][0]['basic']['admin_area']  # 省份

        content['day'] = req_json['HeWeather6'][0]['daily_forecast'][day]['date']  # 日期
        content['cond_txt_d'] = req_json['HeWeather6'][0]['daily_forecast'][day]['cond_txt_d']  # 天气
        content['cond_txt_n'] = req_json['HeWeather6'][0]['daily_forecast'][day]['cond_txt_n']  # 天气

        content['tmp_max'] = req_json['HeWeather6'][0]['daily_forecast'][day]['tmp_max']  # 最高温度
        content['tmp_min'] = req_json['HeWeather6'][0]['daily_forecast'][day]['tmp_min']  # 最低温度

        # 设置图标
        # 设置天气图标
        content['cond_txt_d_icon'] = make_weather_icon(content['cond_txt_d'])
        content['cond_txt_n_icon'] = make_weather_icon(content['cond_txt_n'])
        # 温度图标
        content['tmp_max_id'] = tem_icon(content['tmp_max'])
        content['tmp_min_id'] = tem_icon(content['tmp_min'])

        # 设置提示语
        # 天气提示语
        content['cond_msg'] = set_weather_msg(content['cond_txt_d'], content['cond_txt_n'])
        # 温度提示
        content['tmp_msg'] = tem_icon(content['tmp_max'])
        return content

    except Exception as e:
        print(f"出错了  错误信息是{e}")


# 整合天气提示语
def make_msg_weather_details(day):
    weather_result = weather('西安', 'e490a26df5ca4d8286ddd688cf9f10b0', day=day)

    weather_msg = f"天气: 省份 {weather_result['province']} 城市  {weather_result['city']}   日期 {weather_result['day']} @face=144@  天气 {weather_result['cond_txt_d']} {weather_result['cond_txt_d_icon']}  转 {weather_result['cond_txt_n']} {weather_result['cond_txt_n_icon']}  {weather_result['cond_msg']}  最高温度 {weather_result['tmp_max']} °C   {weather_result['tmp_msg']} 最低温度 {weather_result['tmp_min']} °C "
    return weather_msg


# 早安 晚安
def morning(loca_time, key):
    content = ''
    url = "http://api.tianapi.com/txapi/zaoan/index?key="

    try:
        if 5 < loca_time < 12:  # 早上
            req = requests.get(url=(url + key))
            req_json = req.json()
            content = req_json['newslist'][0]['content']
        else:
            print("现在还不是早上")
            print(f"现在不是早上现在是{time.localtime().tm_hour}时 传入时间是{loca_time}时")
        return content
    except Exception as e:
        print(f"出错了 错误信息是{e}")
        pass


# 电影台词
def film(key):
    content = {
        "dialogue": '',
        "english": '',
        "source": ''
    }
    url = f"http://api.tianapi.com/txapi/dialogue/index?key={key}"
    try:
        req = requests.get(url=url)
        req_json = req.json()
        content["dialogue"] = req_json['newslist'][0]['dialogue']
        content["english"] = req_json['newslist'][0]['english']
        content["source"] = req_json['newslist'][0]['source']
        return content
    except Exception as e:
        print(f"出错了 错误信息是{e}")


# 英语一句话
def english_msg(key):
    content = {
        "zh": '',
        "en": ''
    }
    url = f"http://api.tianapi.com/txapi/everyday/index?key={key}"
    try:
        req = requests.get(url=url)
        req_json = req.json()
        # print(req_json)
        content["zh"] = req_json['newslist'][0]['content']
        content["en"] = req_json['newslist'][0]['note']

        # 输出
        # for key, value in content.items():
        #     print(key, value)
        return content
    except Exception as e:
        print(f"出错了 错误信息是{e}")


# 古代情诗
def ancient_poetry(key):
    content = {
        'cont': '',
        'source': '',
        'author': ''
    }
    url = f"http://api.tianapi.com/txapi/verse/index?key={key}"
    try:
        req = requests.get(url=url)
        req_json = req.json()
        # print(req_json)
        content['cont'] = req_json['newslist'][0]['content']
        content['source'] = req_json['newslist'][0]['source']
        content['author'] = req_json['newslist'][0]['author']
        # 输出
        # for key, value in content.items():
        #     print(key, value)
        return content
    except Exception as e:
        print(f"出错了 错误信息是{e}")


# 彩虹屁
def chp(key):
    content = ''
    url = f"http://api.tianapi.com/txapi/caihongpi/index?key={key}"
    try:
        req = requests.get(url=url)
        req_json = req.json()
        # print(req_json)
        content = req_json['newslist'][0]['content']
        return content
    except Exception as e:
        print(f"出错了 错误信息是{e}")


# 发送消息
def send_msg(msg):
    try:
        # Wechat
        sckey = 'SCT66734TyhADtYe8gaaFFylSNealcIAW'
        url = f'https://sc.ftqq.com/%s.send?text=(^з^)&desp={msg}' % sckey
        # QQ
        #url = f'https://qmsg.zendee.cn/send/e33d5209d569984d0f0476643c1e2e7b?msg={msg}'

        requests.get(url=url)
    except Exception as e:
        print(f"出错了 错误信息是{e}")
