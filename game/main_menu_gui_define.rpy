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