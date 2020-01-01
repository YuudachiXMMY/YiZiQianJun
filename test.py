# police_map_dic = {"obj_type":"police", "obj_action":None, "pos":[0, 0]}
    
# home_map_dic = {"obj_type":"home", "obj_action":None, "pos":[0, 2]}

# news_map_dic = {"obj_type":"news", "obj_action":None, "pos":[0, 5]}

# fountain_map_dic = {"obj_type":"fountain", "obj_action":None, "pos":[2, 2]}

# shop_map_dic = {"obj_type":"police", "obj_action":None, "pos":[3, 0]}

# interview_map_dic = {"obj_type":"interview", "obj_action":None, "pos":[3, 3]}

# rich_map_dic = {"obj_type":"rich", "obj_action":None, "pos":[3, 6]}

import random

class GameMap_ObjLocation:

    def __init__(self, dic):
        self.obj_type = dic["obj_type"]
        if dic["obj_type"]!="news":
            self.times = 999999
            self.hot = 0
            self.requirement = None
        else:
            self.times = dic["times"]
            self.hot = dic["hot"]
            self.requirement = dic["requirement"]
        self.obj_action = dic["obj_action"]
        self.position = dic["pos"]

class GameMap_Creator:

    matrix = [  [None, None], \
        [None, None] ]

    def __init__(self, dic):

        police_map_dic = {"obj_type":"police", "obj_action":None, "pos":[0, 0]}
            
        home_map_dic = {"obj_type":"home", "obj_action":None, "pos":[0, 2]}

        news_map_dic = {"obj_type":"news", "obj_action":None, "pos":[0, 5]}

        fountain_map_dic = {"obj_type":"fountain", "obj_action":None, "pos":[2, 2]}

        shop_map_dic = {"obj_type":"police", "obj_action":None, "pos":[3, 0]}

        interview_map_dic = {"obj_type":"interview", "obj_action":None, "pos":[3, 3]}

        rich_map_dic = {"obj_type":"rich", "obj_action":None, "pos":[3, 6]}
        
        matrix = [
            [ GameMap_ObjLocation(police_map_dic) , None , GameMap_ObjLocation(home_map_dic) , None , None , GameMap_ObjLocation(news_map_dic) , None], \
                [ None , None , None , None , None , None , None], \
                    [ None , None , GameMap_ObjLocation(fountain_map_dic) , None , None , None , None], \
                        [ GameMap_ObjLocation(shop_map_dic) , None , None , GameMap_ObjLocation(interview_map_dic) , None , None , GameMap_ObjLocation(rich_map_dic)]
        ]
        # 随机生成新闻
        for i in range(len(dic)):
            col = random.randint(0, 6)
            row = random.randint(0, 3)
            while matrix[row][col] != None:
                col = random.randint(0, 6)
                row = random.randint(0, 3)
            # 二次检查
            if matrix[row][col] != None:
                matrix[row][col] = GameMap_ObjLocation( {"obj_type":"news", "times":dic[i]["times"], "hot":dic[i]["hot"], \
                    "requirement":dic[i]["requirement"], "obj_action":dic[i]["obj_action"], "pos":[row, col]} )
        
        # 处理None
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if matrix[row][col]==None:
                    matrix[row][col] = GameMap_ObjLocation( {"obj_type":"None", "obj_action":None, "pos":[row, col]} )
        
        self.matrix = matrix

dic_local = [   {"times":5, "hot":10, "requirement":None, \
    "obj_action":None}, \
        {"times":4, "hot":10, "requirement":None, \
            "obj_action":None}]

game_map = GameMap_Creator(dic_local)

for i in range(len(dic_local)):
    for j in range(len(dic_local[0])):
        print dic_local[i][j].obj_type