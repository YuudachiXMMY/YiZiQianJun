
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

    scene bg room

    show oej normal:
        xalign 0.5

    oej normal "您已创建一个新的 Ren'Py 游戏。"

    oej normal "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    $ explore_point = 50

    $ dic = [ 1, 2]
    
    $ game_map = GameMap_Creator(dic)
    $ game_map_list = game_map.toList()
    $ palyer_currpos = [2,6]

    $ cur_month = Game_Map_march_0_1982

    call screen game_map_main(game_map_list, cur_month)

    # 此处为游戏结尾。

    return
