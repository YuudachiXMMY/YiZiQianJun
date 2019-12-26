# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define oej = Character("欧尔佳",color="#fff", image="oej")

image oej normal = Composite(
    (500,500),
    (0, 0), "images/oej/side/欧尔佳.png",
    (0, 0), "images/oej/side/欧尔佳普通.png")

image side oej normal = Composite((500,500),
    (0, 0),"images/oej/side/欧尔佳.png",
    (0, 0), "images/oej/side/欧尔佳普通.png")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    # show eileen happy
    show oej normal:
        xalign 0.5

    # 此处显示各行对话。

    oej normal "您已创建一个新的 Ren'Py 游戏。"

    "nothin"

    $ dic = {}

    call screen game_map_main(dic)

    oej normal "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
