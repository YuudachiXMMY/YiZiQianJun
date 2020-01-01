################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## 棋盘界面
################################################################################

# 主
screen game_map_main(lst):

    zorder 101

    fixed:

        add "gui/game_screen/棋盘/地图棋盘3.jpg" zoom 1.5
        add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
        text _("[player_newsgrade] / 5"):
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

        # For Testing
        text _("[palyer_currpos]"):
            size 40 xalign 0.5 yalign 0.1 color "#fff" bold True

        # 干死移动控制
        imagebutton:
            xalign 0.87 yalign 0.85
            auto "map_gui_movebutton_%s"
            action Show("game_map_movecontrol", lst=lst, transition=Dissolve(0.5))

        grid 7 4:
            xpos 25 yalign 0.7
            xspacing 0 yspacing 40
            
            for i in game_map_list:
                imagebutton:
                    auto str(i.obj_type)+"_smallbutton_%s"
                    if i.obj_type=="news":
                        action Show("game_map_news", lst=lst, hot=i.hot, explore_point=i.explore_point, times=i.times, transition=Dissolve(0.5))
                    elif i.obj_type!="None":
                        action Show("game_map_building_detail", lst=lst, type=i.obj_type, transition=Dissolve(0.5))
                    else:
                        action NullAction()

# News简介
screen game_map_news(lst, hot, explore_point, times):

    tag game_map_main

    zorder 102

    use game_map_main(lst)

    if renpy.get_screen("game_map_main") and player_newsgrade!=5:

        fixed:

            add "gui/game_screen/棋盘/业绩-1_03.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
            text _("[player_newsgrade] / 5"):
                size 45 xpos 1450 ypos 95 bold True
            text _(str(explore_point)):
                size 45 xalign 0.5 xpos 1690 ypos 605 bold True
            text _(str(times)):
                size 40 xalign 0.5 xpos 1690 ypos 675 bold True
            text _(str("Explore")):
                size 40 xalign 0.5 xpos 1690 ypos 740 bold True

            # 热度显示
            grid hot 1:
                pos(1490, 490)
                xspacing 7
                
                for i in range(hot):
                    add "gui/game_screen/棋盘/专栏裁切_22.png" zoom 1.5

            # 干死移动控制
            imagebutton:
                xalign 0.87 yalign 0.85
                auto "map_gui_movebutton_%s"
                action Show("game_map_movecontrol", lst=lst, transition=Dissolve(0.5))

# Building简介
screen game_map_building_detail(lst, type):

    tag game_map_main

    zorder 102

    use game_map_main(lst)

    if renpy.get_screen("game_map_main") and player_newsgrade!=5:

        fixed:

            add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5

        window:
            background None
            
            text _(str(game_map_building_shortdescription[type])):
                xmaximum 50 size 40 bold True

        # 干死移动控制
        imagebutton:
            xalign 0.87 yalign 0.85
            auto "map_gui_movebutton_%s"
            action Show("game_map_movecontrol", lst=lst, transition=Dissolve(0.5))

# 移动控制
screen game_map_movecontrol(lst):

    zorder 105

    if renpy.get_screen("game_map_main") and player_newsgrade!=5:

        grid 7 4:
            xpos 25 yalign 0.7
            xspacing 0 yspacing 40
            
            for i in game_map_list:
                imagebutton:
                    auto str(i.obj_type)+"_smallbutton_%s"
                    if i.obj_type=="news":
                        action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - i.explore_point - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), SetVariable("player_newsgrade", player_newsgrade+1), Function(resetNews, dic=game_map_list, position=i.position), Hide("game_map_movecontrol")
                    else:
                        action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), Hide("game_map_movecontrol")


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