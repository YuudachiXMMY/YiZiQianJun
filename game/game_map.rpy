################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## Local Variables
################################################################################

init -3 python:
    class GameMap_ObjLocation:

        point = 0
        times = 0
        requirement = ""
        obj_action = ""
        position = [0, 0]

        def __init__(self, point, times, requirement, obj_action, position):
            self.point = point
            self.times = times
            self.requirement = requirement
            self.obj_action = obj_action
            self.position = position

    class GameMap_Creator:

        def __init__(self, lst):
            matrix = [
                [ "police" , null , "home" , null , null , "news" , null]
                [ null , null , null , null , null , null , null]
                [ null , null , "fountain" , null , null , null , null]
                [ "shop" , null , null , "interview" , null , null , "rich"]
            ]

            for i in range(lst):


################################################################################
## 棋盘界面
################################################################################

screen game_main(lst):

    fixed:

        add "gui/game_screen/棋盘/地图棋盘3.jpg" zoom 1.5
        add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
        text _("0 / 5"):
            size 45 xpos 1450 ypos 95 bold True
        
        # 左上角探索
        imagebutton:
            pos(0, 0)
            auto "explore_%s"
            action Show("shop_news_month_1", transition=Dissolve(0.5))

        text _("[explore_point]"):
            size 45 xpos 475 ypos 95 bold True
        text _("$"):
            size 40 yalign 0.5 xpos 200 ypos 55 bold True
        text _("[explore_money]"):
            size 40 xalign 1.0 yalign 0.5 xpos 330 ypos 55 color "#fff" bold True

        # 玩家位置
        add "gui/game_screen/棋盘/indi.png" zoom 1.5

        # grid 7 4:
        #     for point in game_map_list_rand:
        #         if point != Null:
        #             fixed:
        #                 pass
        #         else:
        #             fixed:
        #                 pass


################################################################################
## 新手引导
################################################################################

screen beginner_leading_textbox(dia):

    pass

    # window:
    #     xsize 500 xfill True
    #     ysize 280
    #     xalign 0.5 yalign 0.5
    #     ## TODO
    #     background "textbox"

    #     text dia