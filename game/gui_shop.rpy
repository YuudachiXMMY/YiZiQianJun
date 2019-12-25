################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## 商店界面
################################################################################

screen shop():

    zorder 101

    if renpy.get_screen("shop_news_month_1") or renpy.get_screen("shop_news_month_2") or renpy.get_screen("shop_mag") or renpy.get_screen("shop_letter") or renpy.get_screen("shop_shop_page_news1") or renpy.get_screen("shop_shop_page_news2") or renpy.get_screen("shop_shop_page_news3") or renpy.get_screen("shop_shop_page_paper"):

        grid 1 4:
            xpos -1550 yalign 0.5
            yspacing 20
            
            imagebutton:
                yalign 0.3
                auto "shop_news_navi_%s"
                action Show("shop_news_month_1", transition=Dissolve(0.5))
            imagebutton:
                yalign 0.4
                auto "shop_mag_navi_%s"
                action Show("shop_mag", transition=Dissolve(0.5))
            imagebutton:
                yalign 0.5
                auto "shop_letter_navi_%s"
                action Show("shop_letter", transition=Dissolve(0.5))
            imagebutton:
                yalign 0.6
                auto "shop_shop_navi_%s"
                action Show("shop_shop_page_paper", transition=Dissolve(0.5))


################################################################################
## 报纸
##

## 报纸 月份1
screen shop_news_month_1():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/报纸/已购买目录_月份底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/报纸/上级界面已购买目录_月份报纸1.jpg" zoom 1.5 xalign 0.45 yalign 0.5
    add "gui/buttons/滚动条.png" zoom 1.5 ypos 110 xpos(1685)

    grid 2 8:
        xpos 480 ypos 200
        yspacing 7 xspacing 330

        ## 三月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=march_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=march_1_1982, transition=Dissolve(0.5))

        ## 四月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=april_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=april_1_1982, transition=Dissolve(0.5))

        ## 五月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=may_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=may_1_1982, transition=Dissolve(0.5))

        ## 六月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=june_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=june_1_1982, transition=Dissolve(0.5))

        ## 七月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=july_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=july_1_1982, transition=Dissolve(0.5))

        ## 八月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=august_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=august_1_1982, transition=Dissolve(0.5))
        
        ## 九月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=september_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=september_1_1982, transition=Dissolve(0.5))

        ## 十月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=october_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=october_1_1982, transition=Dissolve(0.5))

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action Hide("shop_news_month_1"), Show("shop_news_month_2", transition=Dissolve(0.5))

        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_news_month_1", transition=Dissolve(0.5))

        if not renpy.get_screen("game_main"):
            use shop

## 报纸 月份2
screen shop_news_month_2():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/报纸/已购买目录_月份底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/报纸/已购买目录_月份报纸2.jpg" zoom 1.5 xalign 0.45 ypos 222
    add "gui/buttons/滚动条.png" zoom 1.5 ypos 110 xpos(1685)

    grid 2 4:
        xpos 480 ypos 200
        yspacing 7 xspacing 330
        
        ## 十一月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=november_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=november_1_1982, transition=Dissolve(0.5))
        
        ## 十二月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=december_0_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=december_1_1982, transition=Dissolve(0.5))
        
        ## 一月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=january_0_1983, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=january_1_1983, transition=Dissolve(0.5))

        ## 二月
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=february_0_1983, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_news_month_overview", month=february_1_1983, transition=Dissolve(0.5))

    fixed:
        xpos 1665

        imagebutton:
            ypos 745
            auto "previous_%s"
            action Hide("shop_news_month_2"), Show("shop_news_month_1", transition=Dissolve(0.5))
            
        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_news_month_2", transition=Dissolve(0.5))

        if not renpy.get_screen("game_main"):
            use shop

## 某月报纸
screen shop_news_month_overview(month):

    zorder 103
    modal True
    
    add "gui/game_screen/报纸/下级界面报纸查阅-_底图.png" zoom 1.5 xalign 0.7 yalign 0.4

    text _(""+month) align(0.5, 0.4)

    imagebutton:
        pos(1665, 200)
        auto "return_%s"
        action Hide("shop_news_month_overview", transition=Dissolve(0.5))

screen shop_news_detail():

    zorder 104

    add "gui/game_screen/报纸/显示窗.png" zoom 1.5 align(0.5, 0.5)

    ## 透明背景按钮 返回
    imagebutton:
        idle "gui/transparent_background.png"
        action Hide("shop_news_month_overview", transition=Dissolve(0.5))


################################################################################
## 杂志 ####################################################################
##

screen shop_mag():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/杂志/杂志查阅光板.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/杂志/已购买目录_月份杂志.jpg" zoom 1.5 xalign 0.45 ypos 222

    grid 2 6:
        xpos 480 ypos 200
        yspacing 7 xspacing 330

        ## 月份
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=march_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=april_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=may_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=june_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=july_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=august_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=september_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=october_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=november_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=december_1982, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=january_1983, transition=Dissolve(0.5))
        imagebutton:
            idle "gui/gallery/button_frame.png"
            action Show("shop_mag_detail", book=february_1983, transition=Dissolve(0.5))

    fixed:
        xpos 1665
            
        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_mag", transition=Dissolve(0.5))

        use shop

screen shop_mag_detail(book):

    zorder 103
    modal True

    add "gui/game_screen/杂志/对话框5-杂志查阅-切_03.png" zoom 1.5 xalign 0.7 yalign 0.4

    add "gui/game_screen/杂志/杂志内容/杂志查阅_一字千钧.jpg" zoom 1.5 xpos 350 yalign 0.5

    text _(""+book) align(0.5, 0.5)

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action None

        imagebutton:
            ypos 745
            auto "previous_%s"
            action None
        
        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_mag_detail", transition=Dissolve(0.5))


################################################################################
## 信件
##

screen shop_letter():

    tag shop

    zorder 103
    modal True

    add "gui/game_screen/信件/回复信件_05.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/buttons/滚动条.png" zoom 1.5 ypos 110 xpos(1685)

    imagebutton:
        pos(500, 300)
        idle "gui/gallery/button_frame.png"
        action Show("shop_letter_detail", letter=march_0_1982, transition=Dissolve(0.5))

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action None

        imagebutton:
            ypos 745
            auto "previous_%s"
            action None
            
        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_letter", transition=Dissolve(0.5))

        use shop

screen shop_letter_detail(letter):
    
    tag shop_letter

    zorder 103
    modal True

    add "gui/game_screen/信件/回复信件_1.png" zoom 1.5 xalign 0.7 yalign 0.4

    fixed:
        ypos 880
        
        imagebutton:
            xpos 1400
            idle "gui/gallery/button_frame.png"
            action Show("shop_letter_detail_reply", letter=march_0_1982, transition=Dissolve(0.5))

        imagebutton:
            xpos 1200
            idle "gui/gallery/button_frame.png"
            action Hide("shop_letter_detail", transition=Dissolve(0.5))

screen shop_letter_detail_reply(letter):

    tag shop_letter

    zorder 104
    modal True

    add "gui/game_screen/信件/回复信件_03.png" zoom 1.5 xalign 0.7 yalign 0.4

    fixed:
        imagebutton:
            xpos 850 yalign 0.85
            auto "shop_letter_detail_reply_%s"
            action Hide("shop_letter_detail_reply", transition=Dissolve(0.5))


################################################################################
## 邮购
##

## 报纸
screen shop_shop_page_paper():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/邮购/邮购商店_底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/邮购/邮购商店_报纸.jpg" zoom 1.5 xalign 0.45 yalign 0.5

    use shop_shop_subscribe(page="paper", vol=0)

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action Show("shop_shop_page_news1", transition=Dissolve(0.5))

        # imagebutton:
        #     ypos 745
        #     auto "previous_%s"
        #     action Show("shop_shop_page_news3", transition=Dissolve(0.5))

        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_shop_page_paper", transition=Dissolve(0.5))

        use shop

## 杂志1
screen shop_shop_page_news1():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/邮购/邮购商店_底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/邮购/邮购商店_杂志1.jpg" zoom 1.5 xalign 0.45 yalign 0.5

    use shop_shop_subscribe(page="news", vol=1)

    fixed:

        pass

        # on "show" action Show("shop_shop_subscribe", page=shop_shop_page_news1)

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action Show("shop_shop_page_news2", transition=Dissolve(0.5))
        
        imagebutton:
            ypos 745
            auto "previous_%s"
            action Show("shop_shop_page_paper", transition=Dissolve(0.5))

        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_shop_page_news1", transition=Dissolve(0.5))

        use shop

## 杂志2
screen shop_shop_page_news2():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/邮购/邮购商店_底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/邮购/邮购商店_杂志2.jpg" zoom 1.5 xalign 0.45 yalign 0.5

    # TODO 1
    #差下面三位图片
    use shop_shop_subscribe(page="news", vol=2)

    fixed:
        xpos 1665

        imagebutton:
            ypos 610
            auto "next_%s"
            action Show("shop_shop_page_news3", transition=Dissolve(0.5))

        imagebutton:
            ypos 745
            auto "previous_%s"
            action Show("shop_shop_page_news1", transition=Dissolve(0.5))

        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_shop_page_news2", transition=Dissolve(0.5))

        use shop

## 杂志2
screen shop_shop_page_news3():

    tag shop

    zorder 102
    modal True

    add "gui/game_screen/邮购/邮购商店_底图.png" zoom 1.5 xalign 0.7 yalign 0.4
    add "gui/game_screen/邮购/邮购商店_杂志3.jpg" zoom 1.5 xalign 0.45 yalign 0.5

    # TODO 1
    #差下面三位图片
    use shop_shop_subscribe(page="news", vol=3)

    fixed:
        xpos 1665

        # imagebutton:
        #     ypos 610
        #     auto "next_%s"
        #     action Show("shop_shop_page_paper", transition=Dissolve(0.5))

        imagebutton:
            ypos 745
            auto "previous_%s"
            action Show("shop_shop_page_news2", transition=Dissolve(0.5))

        imagebutton:
            ypos 200
            auto "return_%s"
            action Hide("shop_shop_page_news3", transition=Dissolve(0.5))

        use shop

## 订购
screen shop_shop_subscribe(page, vol):

    zorder 103

    grid 3 2:
        xalign 0.575 yalign 0.68
        yspacing 290
        xspacing 310

        for i in range(0, 6):

            imagebutton:
                auto "shop_shop_subscribe_%s"
                action Show("shop_shop_subscribe_detail", content=page, num=i, vol=vol, transition=Dissolve(0.5))

## 订购 展开
screen shop_shop_subscribe_detail(content, num, vol):

    zorder 104
    modal True

    add "gui/game_screen/邮购/点击出现的商品介绍/商品-杂志介绍_底图.png" zoom 1.5 align(0.5, 0.5)
    # if vol==0:
    #     add "gui/game_screen/邮购/点击出现的商品介绍/shop_"+str(content)+"_"+str(num)+".jpg" zoom 1.5 align(0.5, 0.5)
    # else:
    add "gui/game_screen/邮购/点击出现的商品介绍/shop_"+str(content)+"_"+str(vol)+"_"+str(num)+".jpg" zoom 1.5 align(0.5, 0.5)
    
    imagebutton:
        idle "gui/transparent_background.png"
        action Hide("shop_shop_subscribe_detail", transition=Dissolve(0.5))