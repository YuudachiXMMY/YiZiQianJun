
init offset = -1

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

image textbox:
    zoom 1.5 xzoom 1.08
    xalign 0.5 yalign 1.0
    "gui/textbox.png"

image textbox_phone:
    xzoom 1.6 yzoom 2.1
    xalign 0.5 yalign 1.0
    "gui/textbox.png"


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

image next_idle:
    zoom 1.5
    "gui/buttons/按钮_后退_未选.png"

image next_hover:
    zoom 1.5
    "gui/buttons/按钮_后退_选中.png"

image previous_idle:
    zoom 1.5
    "gui/buttons/按钮_前进_未选.png"

image previous_hover:
    zoom 1.5
    "gui/buttons/按钮_前进_选中.png"

image printer_idle:
    zoom 1.5
    "gui/game_screen/打字机_未选.png"

image printer_hover:
    zoom 1.5
    "gui/game_screen/打字机_选中.png"


## CG####
image cg_indi_prop:
    zoom 1.5
    "gui/gallery/indi/prop.png"

image cg_indi_title:
    zoom 1.5
    "gui/gallery/indi/title.png"

image cg_achievement_title:
    zoom 1.5
    "gui/gallery/achievement/title.png"

image cg_relationship_title:
    zoom 1.5
    "gui/gallery/relation/title.png"

image cg_gallery_title:
    zoom 1.5
    "gui/gallery/cg/title.png"

image cg_materials_title:
    zoom 1.5
    "gui/gallery/material/title.png"

image cg_indi_nav_idle:
    "gui/gallery/按钮_个人档案_未选.png"

image cg_indi_nav_hover:
    "gui/gallery/按钮_个人档案_选中.png"

image cg_achievement_nav_idle:
    zoom 1.5
    "gui/gallery/按钮_记者手册_未选.png"

image cg_achievement_nav_hover:
    zoom 1.5
    "gui/gallery/按钮_记者手册_选中.png"

image cg_relationship_nav_idle:
    zoom 1.5
    "gui/gallery/按钮_人际关系_未选.png"

image cg_relationship_nav_hover:
    zoom 1.5
    "gui/gallery/按钮_人际关系_选中.png"

image cg_gallery_nav_idle:
    zoom 1.5
    "gui/gallery/按钮_相册回忆_未选.png"

image cg_gallery_nav_hover:
    zoom 1.5
    "gui/gallery/按钮_相册回忆_选中.png"

image cg_materials_nav_idle:
    zoom 1.5
    "gui/gallery/按钮_写作素材_未选.png"

image cg_materials_nav_hover:
    zoom 1.5
    "gui/gallery/按钮_写作素材_选中.png"


## 柯安时报####
image kean_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_柯安时报.png"

image kean_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_柯安时报1.png"

image kean_save_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_存档.png"

image kean_save_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_存档1.png"

image kean_load_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_读取.png"

image kean_load_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_读取1.png"

image kean_auto_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_自动.png"

image kean_auto_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_自动1.png"

image kean_auto_selected:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_自动1.png"

image kean_preference_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_设置.png"

image kean_preference_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_设置1.png"

image kean_return_idle:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_返回.png"

image kean_return_hover:
    zoom 1.5
    "gui/game_screen/柯安时报/按钮_返回1.png"


## 探索点数
image explore_idle:
    zoom 1.5
    "gui/game_screen/探索点/探索点数未选.png"

image explore_hover:
    zoom 1.5
    "gui/game_screen/探索点/探索点数选中.png"


## 商店界面

image shop_letter_detail_reply_idle:
    zoom 1.5
    "gui/game_screen/信件/报纸裁切_回复1.png"

image shop_letter_detail_reply_hover:
    zoom 1.5
    "gui/game_screen/信件/报纸裁切_回复2.png"

image shop_shop_subscribe_idle:
    zoom 1.5
    "gui/game_screen/邮购/邮购商店_订阅未选中.png"

image shop_shop_subscribe_hover:
    zoom 1.5
    "gui/game_screen/邮购/邮购商店_订阅选中.png"
