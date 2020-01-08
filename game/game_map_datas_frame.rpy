################################################################################
## Game_Map 数据结构
################################################################################

init -3 python:

    # 所有新闻时效-1, 总时效+1
    def changeGlobalTime(month):
        game_map_global_time += 1
        for i in month_round:
            month[str(i)]["times"] -= 1

    # 已发布新闻记录
    def publishNewsINMonth(month, key, opt):
        if not round_publishnews.has_key(month):
            round_publishnews[month] = {}
        round_publishnews[month][key] = opt

    # 已废弃新闻纪录
    def deleteNewsINMonth(month, key, opt):
        if not round_deletenews.has_key(month):
            round_deletenews[month] = {}
        round_deletenews[month][key] = opt

    # 合并两字典数据
    def addDIC1toDIC2(dic1, dic2):
        # check len
        if len(dic1)==len(dic2):
            for i in dic1:
                dic2[i] += dic1[i]
    
    # 杀掉已完成新闻
    def resetNews(dic, position):
        dic[position[0]*7+position[1]] = GameMap_ObjLocation({ "obj_type":"None", "pos":[position[0], position[1]], "title":None })

init -3 python:

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