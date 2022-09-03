import random
from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment, MessageEvent

# 显示目录
show_menu = on_fullmatch(rule=to_me(), msg=("菜单", "显示菜单", "menu"), priority=1)


@show_menu.handle()
async def menu(event: MessageEvent):
    user_id = event.get_user_id()
    answer_list = [
        'OK!菜单来啦！你看我多宠你，随叫随到！\n',
        '来啦来啦！你要的目录来啦！\n',
        '',
    ]
    content = Message([
        MessageSegment.at(user_id), MessageSegment.face(124),
        MessageSegment.text(random.choice(answer_list)),
        MessageSegment.text("- -- ---  QQ川菜robot  --- -- -\n"),
        MessageSegment.face(147), MessageSegment.text(" *个人主页    "),
        MessageSegment.face(147), MessageSegment.text(" *钓鱼系统\n"),
        MessageSegment.face(147), MessageSegment.text(" 签到系统(签到)    "),
        MessageSegment.face(147), MessageSegment.text(" *上班系统\n"),
        MessageSegment.face(147), MessageSegment.text(" *宠物主页    "),
        MessageSegment.face(147), MessageSegment.text(" *排行系统\n"),
        MessageSegment.face(147), MessageSegment.text(" 人生重开(/人生重开)\n"),
        MessageSegment.text("PS1:@我并回复括号内内容查看。\nPS2:前有*代表正在开发\n"),
        MessageSegment.text("网址：https://github.com/20myself22/Chuancai-Robot"),
        MessageSegment.text("- -- ---  川菜0.0.0  --- -- -"),
    ]
    )

    await show_menu.finish(content)
