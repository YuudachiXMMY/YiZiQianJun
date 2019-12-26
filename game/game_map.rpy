################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## Local Variables
################################################################################

init -3 python:

    import random

    class GameMap_ObjLocation:

        obj_type = ""
        times = 0
        hot = 0
        requirement = ""
        obj_action = ""
        position = [0, 0]

        def __init__(self, obj_type, times, hot,
                    requirement, obj_action, position):
            if obj_type == "police":
                self.obj_type = "building"
                # self.obj_action = Show("game_map_police", transition=Dissolve(0.5))
            else:
                self.obj_type = obj_type
                self.times = 5
                self.hot = hot
                self.requirement = requirement
                self.obj_action = obj_action
                self.position = position

    class GameMap_Creator:

        def __init__(self, dic):
            matrix = [
                [ "police" , None , "home" , None , None , "news" , None],
                [ None , None , None , None , None , None , None],
                [ None , None , "fountain" , None , None , None , None],
                [ "shop" , None , None , "interview" , None , None , "rich"]
            ]
            # 随机生成新闻
            for i in range(dic):
                col = random.randint(0, 6)
                row = random.randint(0, 3)
                while matrix[row][col] != None:
                    col = random.randint(0, 6)
                    row = random.randint(0, 3)
                # 二次检查
                if matrix[row][col] != None:
                    matrix[row][col] = GameMap_ObjLocation("news", dic[i]["times"], dic[i]["hot"],
                                                            dic[i]["requirement"], dic[i]["obj_action"], dic[i]["position"])
            
            self.matrix = matrix


        def toList(self):
            lst = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    lst.append(self.matrix[i][j])
            return lst


################################################################################
## 棋盘界面
################################################################################

# 主
screen game_map_main(dic):

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

        grid 7 4:
            for i in GameMap_Creator(dic).toList:
                if i.obj_type == None:
                    fixed:
                        pass
                else:
                    fixed:
                        pass

# 简介
screen game_map_detail():
    pass


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