
define oej = Character("欧尔佳",color="#fff", image="oej")

define month_round = 0
define persistent.month_0 = [1, 2, 3, 4, 5, 6]
define persistent.month_1 = [7, 8, 9, 10, 11, 12]

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

    jump Game_march_00_1982

label Game_march_00_1982:

    show oej normal:
        xalign 0.5

    oej normal "准备进入三月上 前半"

    # 玩家初始位置
    $ palyer_currpos = [2,6]

    $ next_label = "Game_march_01_1982"
    $ player_newsgrade = 0

    # 三月上 第一回合
    $ game_map_global_time = 0
    $ cur_month = Game_Map_march_0_1982
    $ month_round = persistent.month_0

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    call screen game_map_main(game_map_list, cur_month)

label Game_march_01_1982:

    "准备进入三月上 后半"

    $ next_label = "Game_march_10_1982"

    # 三月上 第二回合
    $ game_map_global_time = 0
    $ cur_month = Game_Map_march_0_1982
    $ month_round = persistent.month_1

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    call screen game_map_main(game_map_list, cur_month)

label Game_march_10_1982:

    $ explore_point = 50

    show oej normal:
        xalign 0.5

    oej normal "准备进入三月下 前半"

    # 玩家初始位置
    $ palyer_currpos = [2,6]

    $ next_label = "Game_march_11_1982"
    $ player_newsgrade = 0

    # 三月下 第一回合
    $ game_map_global_time = 0
    $ cur_month = Game_Map_march_1_1982
    $ month_round = persistent.month_0

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    call screen game_map_main(game_map_list, cur_month)

label Game_march_11_1982:

    "准备进入三月下 后半"

    $ next_label = "END_1982"

    # 三月下 第二回合
    $ game_map_global_time = 0
    $ cur_month = Game_Map_march_1_1982
    $ month_round = persistent.month_1

    $ game_map = GameMap_Creator(month_round)
    $ game_map_list = game_map.toList()

    call screen game_map_main(game_map_list, cur_month)

label END_1982:

    # 游戏结束
    return
