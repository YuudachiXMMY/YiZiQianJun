init offset = -4

################################################################################
## Game_Map 三月上棋盘
################################################################################

define Game_Map_MONTH_0or1_1982_templete = {"1": { "short_description":"",
                                                    "hot":0,
                                                    "explore_point":0,
                                                    "times":0,
                                                    "requirement":None,
                                                    "detail":"",
                                                    "opt1":"",
                                                    "opt1_result":{"艺术":0, "压力":0},
                                                    "opt2":"",
                                                    "opt2_result":{"":0}
                                                },
                                            "2": { "short_description":"",
                                                    "hot":0,
                                                    "explore_point":0,
                                                    "times":0,
                                                    "requirement":None,
                                                    "detail":"",
                                                    "opt1":"",
                                                    "opt1_result":{"艺术":0, "压力":0},
                                                    "opt2":"",
                                                    "opt2_result":{"":0}
                                                }
                                            }

define Game_Map_march_0_1982 = {"1": { "short_description":"美术馆计划展出裸体塑像“女教皇”。",
                                        "hot":2,
                                        "explore_point":10,
                                        "times":5,
                                        "requirement":None,
                                        "detail": [ "波克先锋艺术展本月18日在巴特美术馆内举行，展出艺术家波克·里拉的画作，雕塑，以及其他艺术作品。",
                                                    "波克最著名的作品也将在展览中亮相，这件名为“女教皇”的裸体雕塑充分地展现了女性的肉体之美，也因此广受争议。",
                                                    "此次引进“女教皇”在国内引发反对声浪，如此大幅度裸露，是否是假“艺术”之名行低俗之实？",
                                                    "该作品以女教皇为名，是否有侮辱宗教之嫌？波克本人则表示，不能充分领略“女教皇”的美好是一种难以想象的损失。"],
                                        "opt1":"波克艺术展将在国家巴特美术馆举行",
                                        "opt1_result":{"艺术":1, "压力":2},
                                        "opt2":"尺度大到难以想象，“艺术”是“低俗”的挡箭牌吗？",
                                        "opt2_result":{"社会":1, "煽情":1, "压力":5}
                                    },
                                "2": { "short_description":"",
                                        "hot":0,
                                        "explore_point":0,
                                        "times":0,
                                        "requirement":None,
                                        "detail":"",
                                        "opt1":"",
                                        "opt1_result":{"艺术":0, "压力":0},
                                        "opt2":"",
                                        "opt2_result":{"":0}
                                    },
                                }