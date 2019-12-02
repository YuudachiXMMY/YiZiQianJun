################################################################################
## 初始化
################################################################################

init offset = -1

default persistent.Round1 = False

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## Say 屏幕 ######################################################################
##
## Say 屏幕用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此屏幕必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有侧边图像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没
    ## 有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为True，菜单内的叙述会使用旁白 (narrator) 角色。否则，叙述会显示为菜单内的
## 文字说明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    if main_menu:
        imagebutton:
            idle "back_ground"
            action ShowMenu("main_menu_actual")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 此代码可确保替换掉任何其他菜单屏幕。
    tag menu

    add "gui/main_screen/back_ground.png" zoom 0.71
    add "gui/main_screen/封面_02.png"
    add "gui/main_screen/封面_05.png"

    ## 此空框可使标题菜单变暗。
    frame:
        pass

    ## “use”语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation


screen main_menu_actual():

    tag menu

    if main_menu:

        add "gui/main_screen/back_ground.png" zoom 0.71 at trans_navi_TO_mainmenu_diy_back_ground
        add "gui/main_screen/封面_02.png" ypos 520 zoom 1.5
        add "gui/main_screen/封面_05.png" align(1.0,1.0) pos(1920,1080) zoom 1.5

        imagebutton:
            at trans_navi_TO_mainmenu_diy_button1
            top_padding -65
            ypos 550
            idle "start_idle"
            hover "start_hover"
            action Start()

        imagebutton:
            at trans_navi_TO_mainmenu_diy_button2
            top_padding -65
            ypos 650
            idle "load_idle"
            hover "load_hover"
            action ShowMenu("load")

        imagebutton:
            at trans_navi_TO_mainmenu_diy_button3
            top_padding -65
            ypos 750
            idle "option_idle"
            hover "option_hover"
            action ShowMenu("preferences")

        imagebutton:
            at trans_navi_TO_mainmenu_diy_button4
            top_padding -65
            ypos 850
            idle "gallery_idle"
            hover "gallery_hover"
            action ShowMenu("cg_gallery")


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。此屏幕需使用屏幕标题（title）调用，并显示
## 背景、标题和导航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此屏幕与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 这个屏幕没有什么特别之处，因此它也是如何制作自定义屏幕的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”屏幕到此处。子级“vbox”将包含在“game_menu”屏幕
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("基于 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## 此变量在 options.rpy 中重新定义，来添加文本到关于屏幕。
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责允许玩家保存游戏并将其重新读取。由于它们几乎完全一样，因此它们都
## 是以第三方屏幕“file_slots”来实现的。
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    tag menu

    frame:

        add "gui/main_screen/saving/存档底纹_大图.png"
        add "gui/buttons/滚动条.png" zoom 1.5 yalign 0.5 pos(1750, 540)

        imagebutton:
            pos(1728, 240)
            idle "previous_idle"
            hover "previous_hover"
            action FilePagePrevious()

        imagebutton:
            pos(1728, 390)
            idle "next_idle"
            hover "next_hover"
            action FilePageNext(max=4, auto=False, quick=False)

        imagebutton:
            pos(1728, 540)
            idle "return_idle"
            hover "return_hover"
            action Return()

        grid 3 2:

            style_prefix "slot"
            align(0.5, 0.45)
            xspacing 50
            yspacing 70

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, 7):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    add "gui/main_screen/saving/存档底纹_中间.png" align(0.5,0) zoom 1.61
                    add FileScreenshot(i) align(0.5,0) zoom 1.1
                    text FileTime(i, format=_("{#file_time}%Y年%B%d日  %H:%M"), empty=_("")):
                        color "#fff" xalign 0.5 ypos 240
                    text FileSaveName(i)
                    key "save_delete" action FileDelete(i)

        # The buttons at the top allow the user to pick a
        # page of files.
        # hbox:

            # yalign 1.0
            # xalign 0.5

            # textbutton _("<<") action FilePagePrevious()
            # imagebutton auto "gui/main_screen/saving/num/0_%s.png" action FilePage("auto")
            # textbutton _("A") action FilePage("auto")
            # imagebutton auto "gui/main_screen/saving/num/1_%s.png" action FilePage(1)
            # imagebutton auto "gui/main_screen/saving/num/2_%s.png" action FilePage(2)
            # imagebutton auto "gui/main_screen/saving/num/3_%s.png" action FilePage(3)
            # imagebutton auto "gui/main_screen/saving/num/4_%s.png" action FilePage(4)
            # imagebutton auto "gui/main_screen/saving/num/5_%s.png" action FilePage(5)
            # for i in range(1, 6):
            #     imagebutton auto "gui/main_screen/saving/num/" + str(i) + "_%s.png" action FilePage(i)
            # textbutton _(">>") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许玩家配置游戏以更好地适应自己。
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    
    frame:

        add "gui/main_screen/preferences/设置2.png"

        imagebutton:
            pos(1715, 210)
            idle "delete_idle"
            hover "delete_hover"
            action Show("delete_all_confirm_first", transition=Dissolve(0.5))

        imagebutton:
            pos(1715, 780)
            idle "return_idle"
            hover "return_hover"
            action Return()

        style_prefix "pb"

        bar value Preference("music volume") ypos 390

        bar value Preference("sound volume") ypos 510

        bar value Preference("text speed") ypos 630

        bar value Preference("auto-forward time") ypos 750


screen delete_all_confirm_first():

    modal True
    zorder 100
    
    add "gui/main_screen/preferences/弹出框_03.png" align(0.5, 0.5) zoom 1.7

    imagebutton:
        align(0.4,0.6)
        idle "yes_idle"
        hover "yes_hover"
        action Show("delete_all_confirm_second", transition=Dissolve(0.5))

    imagebutton:
        align(0.6,0.6)
        idle "cancel_idle"
        hover "cancel_hover"
        action Hide("delete_all_confirm_first", transition=Dissolve(0.5))

screen delete_all_confirm_second():

    modal True
    zorder 101
    
    add "gui/main_screen/preferences/弹出框_04.png" align(0.5, 0.5) zoom 1.4

    imagebutton:
        align(0.4,0.6)
        idle "yes_idle"
        hover "yes_hover"
        action Show("delete_all"), Hide("delete_all_confirm_first", transition=Dissolve(0.5)), Hide("delete_all_confirm_second", transition=Dissolve(0.5)), Return()

    imagebutton:
        align(0.6,0.6)
        idle "cancel_idle"
        hover "cancel_hover"
        action Hide("delete_all_confirm_first", transition=Dissolve(0.5)), Hide("delete_all_confirm_second", transition=Dissolve(0.5))

screen delete_all():

    on "show" action SetVariable("persistent.Round1", False)

    timer 5.0 action Hide("delete_all")

# PC
style pb_slider:
    xpos 660
    xsize 1000 ysize 50
    left_bar "horizontal_left_bar"
    right_bar "horizontal_right_bar"
    thumb "thumb_idle"

# Phone
style pb_slider:
    variant "small"
    left_bar "horizontal_left_bar"
    right_bar "horizontal_right_bar"
    thumb "thumb_idle"


## 历史屏幕 ########################################################################
##
## 这是一个向玩家显示对话历史的屏幕。虽然此屏幕没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("对话历史记录为空。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不选择选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退控制区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问玩家是非问题时，会调用确认屏幕。
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## “skip_indicator”屏幕用于指示快进正在进行中。
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")



## Gallery ####################################################################
##

screen gallery_navigation:

    if renpy.get_screen("cg_indi") or renpy.get_screen("cg_achievement") or renpy.get_screen("cg_relationship") or renpy.get_screen("cg_relationship_help") or renpy.get_screen("cg_gallery") or renpy.get_screen("cg_materials"):
        
        zorder 100

        imagebutton:
            pos ( 110 , 180)
            idle "gui/gallery/button_frame.png"
            action ShowMenu("cg_indi")
        imagebutton:
            pos ( 110 , 330)
            idle "gui/gallery/button_frame.png"
            action ShowMenu("cg_achievement")
        imagebutton:
            pos ( 110 , 480)
            idle "gui/gallery/button_frame.png"
            action ShowMenu("cg_relationship")
        imagebutton:
            pos ( 110 , 630)
            idle "gui/gallery/button_frame.png"
            action ShowMenu("cg_gallery")
        imagebutton:
            pos ( 110 , 780)
            idle "gui/gallery/button_frame.png"
            action ShowMenu("cg_materials")

        imagebutton:
            yalign 0.5
            pos(1728 , 540)
            idle "return_idle"
            hover "return_hover"
            action ShowMenu("main_menu_actual")


screen cg_indi:

    tag menu

    #on "show" action ShowMenu("gallery_navigation")

    add "gui/gallery/indi/bg.png"
    add "cg_indi_prop" pos(365 , 50)
    add "cg_indi_title" pos(265 , 70)

    # grid 2 3:
    #     text _("")

    use gallery_navigation


screen cg_achievement:
    pass


screen cg_relationship:
    
    tag menu

    #on "show" action ShowMenu("gallery_navigation")

    add "gui/gallery/relation/bg.png"

    use gallery_navigation


screen cg_relationship_help(cha , name_lock , lock , val):

    if lock == false:
        add "gui/gallery/relation/cha_lock.png"
    else:
        add "gui/gallery/relation/" + cha + ".png"
        if name_lock:
            pass
        else:
            pass


screen cg_gallery:

    tag menu

    #on "show" action ShowMenu("gallery_navigation")
    
    add "gui/gallery/cg/bg.png"

    use gallery_navigation

    # grid 3 3:
    #     pass


screen cg_materials:
    pass


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此代码控制一次可以显示的最大 NVL 模式条目数。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


## 图片与动画 #####################################################################
##

## 动画
transform trans_navi_TO_mainmenu_diy_back_ground:
    alpha 0.7
    linear 1.5 alpha 1.0

transform trans_navi_TO_mainmenu_diy_comp:
    alpha 0.0
    linear 1.5 alpha 1.0

# transform trans_navi_TO_mainmenu_diy_:

transform trans_navi_TO_mainmenu_diy_button1:
    alpha 0.0 xpos -100
    linear 1.5 alpha 1.0 xpos -15

transform trans_navi_TO_mainmenu_diy_button2:
    alpha 0.0 xpos -100
    linear 1.5 alpha 1.0 xpos -10

transform trans_navi_TO_mainmenu_diy_button3:
    alpha 0.0 xpos -100
    linear 1.5 alpha 1.0 xpos -5

transform trans_navi_TO_mainmenu_diy_button4:
    alpha 0.0 xpos -100
    linear 1.5 alpha 1.0 xpos 0


## 背景
image back_ground:
    zoom 0.71 alpha 0.67
    "gui/main_screen/back_ground.png"
    linear 2.0 alpha 1.0
    linear 2.0 alpha 0.67
    repeat


## GUI
image start_idle:
    zoom 1.5
    "gui/main_screen/字_start.png"

image start_hover:
    zoom 1.5
    "gui/main_screen/字_start选中.png"

image load_idle:
    zoom 1.5
    "gui/main_screen/字_load.png"

image load_hover:
    zoom 1.5
    "gui/main_screen/字_load选中.png"

image option_idle:
    zoom 1.5
    "gui/main_screen/字_option.png"

image option_hover:
    zoom 1.5
    "gui/main_screen/字_option选中.png"

image gallery_idle:
    zoom 1.5
    "gui/main_screen/字_gallery.png"

image gallery_hover:
    zoom 1.5
    "gui/main_screen/字_gallery选中.png"

image yes_idle:
    zoom 1.5
    "gui/main_screen/saving/确定_未选.png"

image yes_hover:
    zoom 1.5
    "gui/main_screen/saving/确定_选中.png"

image cancel_idle:
    zoom 1.5
    "gui/main_screen/saving/取消_未选.png"

image cancel_hover:
    zoom 1.5
    "gui/main_screen/saving/取消_选中.png"

image return_idle:
    zoom 1.5
    "gui/buttons/按钮_返回_未选.png"

image return_hover:
    zoom 1.5
    "gui/buttons/按钮_返回_选中.png"

image delete_idle:
    zoom 1.5
    "gui/buttons/按钮_垃圾桶_未选.png"

image delete_hover:
    zoom 1.5
    "gui/buttons/按钮_垃圾桶_选中.png"

image thumb_idle:
    zoom 1.5
    "gui/slider/horizontal_idle_thumb.png"

image horizontal_left_bar:
    yzoom 1.5
    xzoom 2.5
    "gui/slider/horizontal_left_bar.png"

image horizontal_right_bar:
    yzoom 1.5
    xzoom 2.5
    "gui/slider/horizontal_right_bar.png"

image cg_indi_prop:
    zoom 1.5
    "gui/gallery/indi/prop.png"

image cg_indi_title:
    zoom 1.5
    "gui/gallery/indi/title.png"

image previous_idle:
    zoom 1.5
    "gui/buttons/按钮_后退_未选.png"

image previous_hover:
    zoom 1.5
    "gui/buttons/按钮_后退_选中.png"

image next_idle:
    zoom 1.5
    "gui/buttons/按钮_前进_未选.png"

image next_hover:
    zoom 1.5
    "gui/buttons/按钮_前进_选中.png"