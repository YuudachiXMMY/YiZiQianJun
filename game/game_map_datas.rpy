################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## Game_Map 数据
################################################################################

define game_map_randomevent_None = ["randomEvent_1", "randomEvent_2", "randomEvent_3"]

define game_map_building_shortdescription = {   "police":u"警察局是了解警务新闻的最好去处。犯罪新闻永远是给读者提供刺激的法宝，谁不想成为下一个名侦探呢！",
                                                "home":u"甜蜜的家，在这里可以做很多事情，尽情地享受生活吧！",
                                                "news_shop":u"报社所在处，在这里可以向同事们讨教工作上的难题，练习写作提高表达能力。",
                                                "fountain":"车水马龙的广场，总是聚集着不少人，时常会有人在此举行聚会。小偷因此很喜欢这里。",
                                                "shop":u"三教九流都会光顾的商业街，能打听到不少八卦，了解新闻的时尚潮流。",
                                                "interview":u"采访点，你可以获取线索，并有机会在这里采访到线索中的人物。",
                                                "rich":u"上流住宅区，富人和名流们聚集之处。说不定哪一天就能结识些大人物，挖出一条劲爆独家新闻！"}

default palyer_currpos = [2,6]
default player_newsgrade = 0

# init -99 python:

#     police_map_dic = {"obj_type":"police", "pos":[0, 0]}
    
#     home_map_dic = {"obj_type":"home", "pos":[0, 2]}
    
#     news_map_dic = {"obj_type":"news_shop", "pos":[0, 5]}
    
#     fountain_map_dic = {"obj_type":"fountain", "pos":[2, 2]}
    
#     shop_map_dic = {"obj_type":"shop", "pos":[3, 0]}
    
#     interview_map_dic = {"obj_type":"interview", "pos":[3, 3]}
    
#     rich_map_dic = {"obj_type":"rich", "pos":[3, 6]}


################################################################################
## Game_Map 数据结构
################################################################################

init -3 python:
    
    def resetNews(dic, position):
        dic[position[0]*7+position[1]] = GameMap_ObjLocation( {"obj_type":"None", "times":99999, "hot":0, "requirement":None, "pos":[position[0], position[1]], "explore_point":-1})

    def resetRandomevent_None(set, inde):
        pass

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
                # avoid buildings and player current position
                while self.matrix[row][col] != None or (row==palyer_currpos[0] and col==palyer_currpos[1]):
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