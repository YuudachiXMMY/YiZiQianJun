################################################################################
## Game_Map 数据
################################################################################

init -99 python:

    police_map_dic = {"obj_type":"police", "pos":[0, 0]}
    
    home_map_dic = {"obj_type":"home", "pos":[0, 2]}
    
    news_map_dic = {"obj_type":"news", "pos":[0, 5]}
    
    fountain_map_dic = {"obj_type":"fountain", "pos":[2, 2]}
    
    shop_map_dic = {"obj_type":"police", "pos":[3, 0]}
    
    interview_map_dic = {"obj_type":"interview", "pos":[3, 3]}
    
    rich_map_dic = {"obj_type":"rich", "pos":[3, 6]}


################################################################################
## Game_Map 数据结构
################################################################################

init -99 python:

    import random

    class GameMap_ObjLocation:

        def __init__(self, dic):
            self.obj_type = dic["obj_type"]
            self.position = dic["pos"]
            # if dic["obj_type"]=="news":
            self.times = dic["times"]
            self.hot = dic["hot"]
            self.requirement = dic["requirement"]
            self.explore_point = dic["explore_point"]


    class GameMap_Creator:

        def __init__(self, dic):
            
            ##
            police_map_dic = {"obj_type":"police", "times":99999, "hot":0,
                            "requirement":None, "pos":[0, 0] , "explore_point":-1}
            home_map_dic = {"obj_type":"home", "times":99999, "hot":0,
                            "requirement":None, "pos":[0, 2] , "explore_point":-1}
            news_map_dic = {"obj_type":"news_shop", "times":99999, "hot":0,
                            "requirement":None, "pos":[0, 5] , "explore_point":-1}
            # TODO fountain2
            # fountain_map_dic = {"obj_type":"fountain", "times":99999, "hot":0,
            #                 "requirement":None, "pos":[2, 2], "explore_point":-1}
            shop_map_dic = {"obj_type":"shop", "times":99999, "hot":0,
                            "requirement":None, "pos":[3, 0] , "explore_point":-1}
            interview_map_dic = {"obj_type":"interview", "times":99999, "hot":0,
                            "requirement":None, "pos":[3, 3], "explore_point":-1}
            rich_map_dic = {"obj_type":"rich", "times":99999, "hot":0,
                            "requirement":None, "pos":[3, 6], "explore_point":-1}
            ## 

            # self.matrix = [
            #     [ GameMap_ObjLocation(police_map_dic) , None , GameMap_ObjLocation(home_map_dic) , None , None , GameMap_ObjLocation(news_map_dic) , None],
            #     [ None , None , None , None , None , None , None],
            #     [ None , None , GameMap_ObjLocation(fountain_map_dic) , None , None , None , None],
            #     [ GameMap_ObjLocation(shop_map_dic) , None , None , GameMap_ObjLocation(interview_map_dic) , None , None , GameMap_ObjLocation(rich_map_dic)]
            # ]
            self.matrix = [
                [ GameMap_ObjLocation(police_map_dic) , None , GameMap_ObjLocation(home_map_dic) , None , None , GameMap_ObjLocation(news_map_dic) , None],
                [ None , None , None , None , None , None , None],
                [ None , None , None , None , None , None , None],
                [ GameMap_ObjLocation(shop_map_dic) , None , None , GameMap_ObjLocation(interview_map_dic) , None , None , GameMap_ObjLocation(rich_map_dic)]
            ]
            
            # 随机生成新闻
            for i in range(len(dic)):
                col = random.randint(0, 6)
                row = random.randint(0, 3)
                while self.matrix[row][col] != None:
                    col = random.randint(0, 6)
                    row = random.randint(0, 3)
                # # 二次检查
                # if matrix[row][col] != None:
                self.matrix[row][col] = GameMap_ObjLocation( {"obj_type":"news", "times":dic[i]["times"], "hot":dic[i]["hot"],
                                                            "requirement":dic[i]["requirement"], "pos":[row, col], "explore_point":dic[i]["explore_point"]})
            
            # 处理None
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    if self.matrix[row][col]==None:
                        self.matrix[row][col] = GameMap_ObjLocation( {"obj_type":"None", "times":99999, "hot":0,
                                                                    "requirement":None, "pos":[row, col], "explore_point":-1} )

        def toList(self):
            lst = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    lst.append(self.matrix[i][j])
            return lst