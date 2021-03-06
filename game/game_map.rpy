################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## 棋盘界面
################################################################################

# 主
screen game_map_main(lst, month):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_main"), Jump(next_label), Return()]

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

        # 加班
        imagebutton:
            xalign 0.45 yalign 0.05
            auto "map_gui_overwork_%s"
            action SetVariable("explore_point", explore_point+15)

        # 下班
        imagebutton:
            xalign 0.6 yalign 0.05
            auto "map_gui_endwork_%s"
            action [Hide("game_map_main"), Jump(next_label), Return()]

        # 干死移动控制
        imagebutton:
            xalign 0.87 yalign 0.85
            auto "map_gui_movebutton_%s"
            action Show("game_map_movecontrol", lst=lst, month=month, transition=Dissolve(0.5))

        grid 7 4:
            # xpos 30
            xalign 0.05 yalign 0.67
            xspacing 47 yspacing 40
            
            for i in game_map_list:
                frame:
                    background None

                    if i.position[0]==palyer_currpos[0] and i.position[1]==palyer_currpos[1]:
                        add "gui/game_screen/棋盘/indi.png" zoom 1.5
                    else:
                        imagebutton:
                            if i.obj_type=="news" and month[str(i.title)]["times"]<=0:
                                auto "None_smallbutton_%s"
                            else:
                                auto str(i.obj_type)+"_smallbutton_%s"
                            if i.obj_type=="news":
                                if month[str(i.title)]["times"]<=0:
                                    action NullAction() 
                                else:
                                    action Show("game_map_news", lst=lst, month=month, title=i.title, transition=Dissolve(0.5))
                            elif i.obj_type!="None":
                                action Show("game_map_building_detail", lst=lst, month=month, type=i.obj_type, transition=Dissolve(0.5))
                            else:
                                action NullAction()


################################################################################
## 新闻界面 ####################################################################
##

# News简介
screen game_map_news(lst, month, title):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_news"), Jump(next_label), Return()]

    tag game_map_main

    use game_map_main(lst, month)

    zorder 102

    if month[title]["times"]>0 and renpy.get_screen("game_map_main"):

        fixed:

            add "gui/game_screen/棋盘/业绩-1_03.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
            text _("[player_newsgrade] / 5"):
                size 45 xpos 1450 ypos 95 bold True
            text _(str(month[title]["explore_point"])):
                size 45 xalign 0.5 xpos 1690 ypos 605 bold True
            text _(str(month[title]["times"])):
                size 40 xalign 0.5 xpos 1690 ypos 675 bold True
            text _(str("未给")):
                size 40 xalign 0.5 xpos 1690 ypos 740 bold True

            window:
                background None
                xfill True
                xalign 0.93 xsize 400
                yalign 0.35 ysize 500

                text _(month[title]["short_description"]):
                    size 40 bold True

            # 热度显示
            grid month[title]["hot"] 1:
                pos(1490, 490)
                xspacing 7
                
                for i in range(month[title]["hot"]):
                    add "gui/game_screen/棋盘/专栏裁切_22.png" zoom 1.5

            # 干死移动控制
            imagebutton:
                xalign 0.87 yalign 0.85
                auto "map_gui_movebutton_%s"
                action Show("game_map_movecontrol", lst=lst, month=month, transition=Dissolve(0.5))

# 新闻详细动作框架
screen game_map_news_action(lst, month, title, page):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_news_action"), Jump(next_label), Return()]

    tag game_map_main

    use game_map_main(lst, month)

    zorder 103
    modal True

    if page<len(month[title]["detail"]) and month[title]["times"]>0 and renpy.get_screen("game_map_main"):

        add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5

        window:
            background None
            xfill True
            xalign 0.93 xsize 450
            yalign 0.5 ysize 700
            
            text _(month[title]["detail"][page]):
                size 40 bold True

            imagebutton:
                xalign 1.0 yalign 1.0
                auto "map_gui_publnews_%s"
                if page==len(month[title]["detail"])-1:
                    action Show("game_map_news_action_decision", lst=lst, month=month, title=title, transition=Dissolve(0.5))
                elif page<len(month[title]["detail"]):
                    action Show("game_map_news_action", lst=lst, month=month, title=title, page=page+1, transition=Dissolve(0.5))
            imagebutton:
                xalign 0.0 yalign 1.0
                auto "map_gui_deletenews_%s"
                if page>0:
                    action Show("game_map_news_action", lst=lst, month=month, title=title, page=page-1, transition=Dissolve(0.5))

# 新闻抉择Main
screen game_map_news_action_decision(lst, month, title):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_news_action_decision"), Jump(next_label), Return()]

    tag game_map_main

    use game_map_main(lst, month)

    zorder 104
    modal True

    if month[title]["times"]>0 and renpy.get_screen("game_map_main"):

        fixed:

            # add "gui/game_screen/棋盘/业绩-1_02.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
            add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
            text _("[player_newsgrade] / 5"):
                size 45 xpos 1450 ypos 95 bold True

            # 选项1
            window:
                background None
                xfill True
                xalign 0.93 xsize 450
                yalign 0.3 ysize 300
                text _(month[title]["opt1"]):
                    size 40 bold True
                imagebutton:
                    xalign 0.5 ypos -20
                    auto "map_gui_publishnews_%s"
                    if renpy.get_screen("game_map_news_action_decision_publish"):
                        action Function(changeGlobalTime, month=month),  SetVariable("player_newsgrade", player_newsgrade+1), SetVariable("game_map_global_time", game_map_global_time+1), Function(publishNewsINMonth, month=str(month), key=title, opt="opt1_result"), Show("game_map_main", lst=lst, month=month, transition=Dissolve(0.5))
                    elif renpy.get_screen("game_map_news_action_decision_delete"):
                        action Function(changeGlobalTime, month=month),  SetVariable("player_newsgrade", player_newsgrade+1), SetVariable("game_map_global_time", game_map_global_time+1), Function(deleteNewsINMonth, month=str(month), key=title, opt="opt1_result"), Show("game_map_main", lst=lst, month=month, transition=Dissolve(0.5))
                    else:
                        action NullAction()

            # 选项2
            window:
                background None
                xfill True
                xalign 0.93 xsize 450
                yalign 0.65 ysize 300
                text _(month[title]["opt2"]):
                    size 40 bold True
                imagebutton:
                    xalign 0.5 ypos -20
                    auto "map_gui_publishnews_%s"
                    if renpy.get_screen("game_map_news_action_decision_publish"):
                        action Function(changeGlobalTime, month=month),  SetVariable("player_newsgrade", player_newsgrade+1), SetVariable("game_map_global_time", game_map_global_time+1), Function(publishNewsINMonth, month=str(month), key=title, opt="opt2_result"), Show("game_map_main", lst=lst, month=month, transition=Dissolve(0.5))
                    elif renpy.get_screen("game_map_news_action_decision_delete"):
                        action Function(changeGlobalTime, month=month),  SetVariable("player_newsgrade", player_newsgrade+1), SetVariable("game_map_global_time", game_map_global_time+1), Function(deleteNewsINMonth, month=str(month), key=title, opt="opt2_result"), Show("game_map_main", lst=lst, month=month, transition=Dissolve(0.5))
                    else:
                        action NullAction()
            
            window:
                background None
                xfill True
                xalign 0.93 xsize 450
                yalign 0.5 ysize 700
                # 发布新闻
                imagebutton:
                    xalign 1.0 yalign 1.0
                    auto "map_gui_publnews_%s"
                    action Show("game_map_news_action_decision_publish", lst=lst, month=month, title=title)

                # 废弃新闻
                imagebutton:
                    xalign 0.0 yalign 1.0
                    auto "map_gui_deletenews_%s"
                    action Show("game_map_news_action_decision_delete", lst=lst, month=month, title=title)

# 发布新闻pass
screen game_map_news_action_decision_publish(lst, month, title):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_news_action_decision_publish"), Jump(next_label), Return()]

    tag game_map_news_action_decision

    zorder 105

    if month[title]["times"]>0 and renpy.get_screen("game_map_news_action_decision"):

        pass

# 废弃新闻pass
screen game_map_news_action_decision_delete(lst, month, title):

    # 结束回合RR
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_news_action_decision_delete"), Jump(next_label), Return()]

    tag game_map_news_action_decision

    zorder 105

    if month[title]["times"]>0 and renpy.get_screen("game_map_news_action_decision"):
        
        pass


################################################################################
## 建筑界面 ####################################################################
##

# Building简介
screen game_map_building_detail(lst, month, type):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_building_detail"), Jump(next_label), Return()]

    tag game_map_main

    zorder 102

    use game_map_main(lst, month)

    if renpy.get_screen("game_map_main"):

        fixed:

            add "gui/game_screen/棋盘/底纹_业绩.png" zoom 1.5 xanchor 1.0 xalign 1.0 yalign 0.5
            text _("[player_newsgrade] / 5"):
                size 45 xpos 1450 ypos 95 bold True

            window:
                background None
                xfill True
                xalign 0.93 xsize 450
                yalign 0.5 ysize 700
                
                text _(game_map_building_shortdescription[type]):
                    size 40 bold True

        # 干死移动控制
        imagebutton:
            xalign 0.87 yalign 0.85
            auto "map_gui_movebutton_%s"
            action Show("game_map_movecontrol", lst=lst, month=month, transition=Dissolve(0.5))


################################################################################
## 移动控制 ####################################################################
##

screen game_map_movecontrol(lst, month):

    # 结束回合
    if game_map_global_time>=5 or player_newsgrade==5:
        on "show" action [Hide("game_map_movecontrol"), Jump(next_label), Return()]

    zorder 110

    if renpy.get_screen("game_map_main"):

        grid 7 4:
            xalign 0.05 yalign 0.67
            xspacing 47 yspacing 40
            
            for i in game_map_list:
                frame:
                    background None

                    if i.position[0]==palyer_currpos[0] and i.position[1]==palyer_currpos[1]:
                        add "gui/game_screen/棋盘/indi.png" zoom 1.5
                    else:
                        imagebutton:
                            if i.obj_type=="news" and month[str(i.title)]["times"]<=0:
                                auto "None_smallbutton_%s"
                            else:
                                auto str(i.obj_type)+"_smallbutton_%s"
                            if i.obj_type=="news":
                                if month[str(i.title)]["times"]<=0:
                                    action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), SetVariable("game_map_global_time", game_map_global_time+1), Function(changeGlobalTime, month=month), Hide("game_map_movecontrol", transition=Dissolve(0.5))
                                else:
                                    action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - month[i.title]["explore_point"] - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), Function(resetNews, dic=game_map_list, position=i.position), Show("game_map_news_action", lst=lst, month=month, title=i.title, page=0, transition=Dissolve(0.5)), Hide("game_map_movecontrol", transition=Dissolve(0.5))
                            # 空白处随机事件
                            elif i.obj_type=="None" and len(game_map_randomevent_None)>0 and random.randint(0, 99) <= 10:
                                    action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), SetVariable("game_map_global_time", game_map_global_time+1), Function(changeGlobalTime, month=month), Jump(game_map_randomevent_None[random.randint(0, len(game_map_randomevent_None)-1)]), Hide("game_map_movecontrol", transition=Dissolve(0.5))
                            else:
                                action SetVariable("palyer_currpos", i.position), SetVariable("explore_point", explore_point - abs(palyer_currpos[0]-i.position[0]) - abs(palyer_currpos[1]-i.position[1])), SetVariable("game_map_global_time", game_map_global_time+1), Function(changeGlobalTime, month=month), Hide("game_map_movecontrol", transition=Dissolve(0.5))


################################################################################
## 新手引导
################################################################################

screen beginner_leading_textbox(dia):

    pass