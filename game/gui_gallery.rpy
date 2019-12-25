################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Gallery
################################################################################

screen gallery_navigation():

    tag menu

    if renpy.get_screen(["cg_indi", "cg_achievement", "cg_relationship",
                        "cg_relationship_extends", "cg_gallery", "cg_materials"]):
        
        zorder 100

        add "gui/buttons/滚动条.png" zoom 1.5 yalign 0.5 pos(1750, 540)

        fixed:
            xpos 110
            
            imagebutton:
                ypos 180
                idle "gui/gallery/按钮_个人档案_未选.png"
                hover "gui/gallery/按钮_个人档案_选中.png"
                action ShowMenu("cg_indi")
            imagebutton:
                ypos 330
                idle "gui/gallery/按钮_记者手册_未选.png"
                hover "gui/gallery/按钮_记者手册_选中.png"
                action ShowMenu("cg_achievement")
            imagebutton:
                ypos 480
                idle "gui/gallery/按钮_人际关系_未选.png"
                hover "gui/gallery/按钮_人际关系_选中.png"
                action ShowMenu("cg_relationship")
            imagebutton:
                ypos 630
                idle "gui/gallery/按钮_相册回忆_未选.png"
                hover "gui/gallery/按钮_相册回忆_选中.png"
                action ShowMenu("cg_gallery")
            imagebutton:
                ypos 780
                idle "gui/gallery/按钮_写作素材_未选.png"
                hover "gui/gallery/按钮_写作素材_选中.png"
                action ShowMenu("cg_materials")

        imagebutton:
            pos(1730, 240)
            auto "return_%s"
            action Return()
            # action ShowMenu("main_menu_actual")


################################################################################
## 个人档案
##

screen cg_indi():

    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_indi_prop" pos(365, 50)
    add "cg_indi_title" pos(265, 70)

    # grid 2 3:
    #     text _("")

    use gallery_navigation


################################################################################
## 记者手册
##

screen cg_achievement():

    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_achievement_title" pos(265, 70)

    use gallery_navigation


################################################################################
## 人际关系
##

screen cg_relationship():
    
    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_relationship_title" pos(265, 70)

    textbutton _("点此减少克莱因好感度") xalign 0.25 yalign 0.65 action SetDict(cha_list_love, "克莱因", cha_list_love["克莱因"]-1)
    textbutton _("点此增加克莱因好感度") xalign 0.5 yalign 0.65 action SetDict(cha_list_love, "克莱因", cha_list_love["克莱因"]+1)

    fixed:
        pos(400, 210)

        use cg_relationship_detail(u"阿莱特")
        use cg_relationship_detail(u"西尔斯")
        use cg_relationship_detail(u"林奈")
        use cg_relationship_detail(u"泽维尔")
        use cg_relationship_detail(u"克莱因")
        use cg_relationship_detail(u"里德")
    
    use gallery_navigation

    imagebutton:
        xpos 1730 ypos 720
        auto "next_%s"
        action Show("cg_relationship_extends", transition=Dissolve(0.5))

screen cg_relationship_extends():
    
    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_relationship_title" pos(265, 70)

    fixed:
        pos(400, 210)
        
        use cg_relationship_detail(u"列文斯顿")
        use cg_relationship_detail(u"德怀特")
        use cg_relationship_detail(u"null1")
        use cg_relationship_detail(u"null2")
        use cg_relationship_detail(u"null3")
        use cg_relationship_detail(u"null4")
    
    use gallery_navigation

    imagebutton:
        xpos 1730 ypos 745
        auto "previous_%s"
        action Show("cg_relationship", transition=Dissolve(0.5))


################################################################################
## 人际关系 框架
##

screen cg_relationship_detail(cha):

    add "gui/gallery/relation/cha_lock.png" zoom 1.4 xpos relation_datail[""+str(cha)+"_xpos"]
        
    add "gui/gallery/relation/角色_"+cha+".png" zoom 1.4 xpos relation_datail[""+str(cha)+"_xpos"]

    text _(str(cha_list_love[cha])) color "#fff" size 50 ypos 580 xpos relation_datail[""+str(cha)+"_xpos"]+85

    # add "gui/gallery/relation/cha_lock.png" zoom 1.4

    # if cha!=u"null" and cha_list_love[cha]!=0:
        
    #     add "gui/gallery/relation/角色_"+cha+".png" zoom 1.4

    #     text _(str(cha_list_love[cha])) color "#fff" size 50 ypos 580


################################################################################
## 相册回忆
##

screen cg_gallery():

    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_gallery_title" pos(265, 70)

    use gallery_navigation

    # grid 3 3:
    #     pass


################################################################################
## 写作素材
##

screen cg_materials():

    tag menu

    add "gui/gallery/background.png" zoom 1.5

    add "cg_materials_title" pos(265, 70)

    use gallery_navigation