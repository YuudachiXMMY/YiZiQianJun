
define oej = Character("欧尔佳",color="#fff", image="oej")

define month_round = 0
define persistent.month_0 = [1, 2, 3, 4, 5, 6]
define persistent.month_1 = [7, 8, 9, 10, 11, 12]

define next_label = None

image oej normal = Composite(
    (500,500),
    (0, 0), "images/oej/side/欧尔佳.png",
    (0, 0), "images/oej/side/欧尔佳普通.png")

image side oej normal = Composite((500,500),
    (0, 0),"images/oej/side/欧尔佳.png",
    (0, 0), "images/oej/side/欧尔佳普通.png")


# 游戏在此开始。

label start:

    $ explore_point = 50

    scene bg room

    show oej normal:
        xalign 0.5

    oej normal "您已创建一个新的 Ren'Py 游戏。"

    oej normal "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    jump Game_march_00_1982

label Game_march_00_1982:

    # 玩家初始位置
    $ palyer_currpos = [2,6]

    # 三月上 第一回合
    $ game_map_global_time = 4
    $ cur_month = Game_Map_march_0_1982
    $ month_round = persistent.month_0

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    $ next_label = "Game_march_01_1982"

    call screen game_map_main(game_map_list, cur_month)

    if _return==1:
        jump Game_march_01_1982

label Game_march_01_1982:

    "march 2"

    # 三月上 第二回合
    $ game_map_global_time = 0
    $ cur_month = Game_Map_march_0_1982
    $ month_round = persistent.month_1

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    $ next_label = "END_1982"

    call screen game_map_main(game_map_list, cur_month)

label END_1982:

    # 游戏结束
    return
