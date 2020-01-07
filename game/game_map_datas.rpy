################################################################################
## 初始化
################################################################################

init offset = -2

################################################################################
## Game_Map 数据
################################################################################

define game_map_round_Newsdata = {}

define game_map_randomevent_None = ["randomEvent_1", "randomEvent_2", "randomEvent_3"]

define game_map_building_shortdescription = {   "police":"警察局是了解警务新闻的最好去处。犯罪新闻永远是给读者提供刺激的法宝，谁不想成为下一个名侦探呢！",
                                                "home":"甜蜜的家，在这里可以做很多事情，尽情地享受生活吧！",
                                                "news_shop":"报社所在处，在这里可以向同事们讨教工作上的难题，练习写作提高表达能力。",
                                                "fountain":"车水马龙的广场，总是聚集着不少人，时常会有人在此举行聚会。小偷因此很喜欢这里。",
                                                "shop":"三教九流都会光顾的商业街，能打听到不少八卦，了解新闻的时尚潮流。",
                                                "interview":"采访点，你可以获取线索，并有机会在这里采访到线索中的人物。",
                                                "rich":"上流住宅区，富人和名流们聚集之处。说不定哪一天就能结识些大人物，挖出一条劲爆独家新闻！"}

default palyer_currpos = [2,6]
default player_newsgrade = 0

################################################################################
## Game_Map 数据结构
################################################################################

init -3 python:

    # 合并数据
    def addDIC1toDIC2(dic1, dic2):
        for i in dic1:
            dic2[i] += dic1[i]
    
    # 杀掉已完成新闻
    def resetNews(dic, position):
        dic[position[0]*7+position[1]] = GameMap_ObjLocation({ "obj_type":"None", "pos":[position[0], position[1]], "title":None })

init -99 python:

    import random

    class GameMap_ObjLocation:

        def __init__(self, dic):
            self.obj_type = dic["obj_type"]
            self.position = dic["pos"]
            self.title = str(dic["title"])

    class GameMap_Creator:

        def __init__(self, dic):
            
            ##
            police_map_dic = {"obj_type":"police", "pos":[0, 0], "title":"police"}
            home_map_dic = {"obj_type":"home", "pos":[0, 2], "title":"home"}
            news_map_dic = {"obj_type":"news_shop", "pos":[0, 5], "title":"news_shop"}
            # TODO fountain2
            # fountain_map_dic = {"obj_type":"fountain", "pos":[2, 2], "title":"fountain"}
            shop_map_dic = {"obj_type":"shop", "pos":[3, 0], "title":"shop"}
            interview_map_dic = {"obj_type":"interview", "pos":[3, 3], "title":"interview"}
            rich_map_dic = {"obj_type":"rich", "pos":[3, 6], "title":"rich"}
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
            for i in dic:
                col = random.randint(0, 6)
                row = random.randint(0, 3)
                # 避免建筑或玩家自身位置
                while self.matrix[row][col] != None or (row==palyer_currpos[0] and col==palyer_currpos[1]):
                    col = random.randint(0, 6)
                    row = random.randint(0, 3)
                self.matrix[row][col] = GameMap_ObjLocation({ "obj_type":"news", "pos":[row, col], "title":i })
            
            # 处理None
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    if self.matrix[row][col]==None:
                        self.matrix[row][col] = GameMap_ObjLocation({ "obj_type":"None", "pos":[row, col], "title":None })

        # Matrix to List
        def toList(self):
            lst = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    lst.append(self.matrix[i][j])
            return lst