#encoding=utf-8
import util
import os
import csv
import json

PaperAuthor_path = "../data/dataset/PaperAuthor.csv"
Paper_path = "../data/dataset/Paper.csv"
Author_path = "../data/dataset/.csv"
out_path = "../data/dataset/result.csv"
C_path = "../data/dataset/Conference.csv"
J_path = "../data/dataset/Journal.csv"
out_json = "../data/dataset/result.json"

data1 = util.read_dict_from_csv(PaperAuthor_path)
print("data1 loaded")
data2 = util.read_dict_from_csv(Paper_path)
print("data2 loaded")
data3 = util.read_dict_from_csv(Author_path)
print("data3 loaded")
data4 = util.read_dict_from_csv(C_path)
print("data4 loaded")
data5 = util.read_dict_from_csv(J_path)
print("data5 loaded")

'''
# 将csv写为json文件
def read_dict_from_csv(in_file):
    if not os.path.exists(in_file):
        return []
    with open(in_file,'r') as csvfile:
        return list(csv.DictReader(csvfile))
data6 = read_dict_from_csv(out_path)

dict = {}
for item in data6:
    print("!")
    paperId = int(item["PaperId"])
    FullName = item["FullName"]
    HomePage = item["HomePage"]
    if paperId not in dict:
        dict[paperId] = []
    dict1 = {}
    dict1["FullName"] = FullName
    dict1["HomePage"] = HomePage
    dict[paperId] = dict1
print("dict is OK!")
json.dump(dict, open(out_json, "w"))
'''

'''
# 提取特征，输出为csv格式
out = open(out_path, 'w', newline='',errors='ignore')
writer = csv.writer(out,dialect='excel')
writer.writerow(["PaperId","FullName", "HomePage"])

dict_paperId_to_authors = {}
for item in data1:
    paperId = int(item["PaperId"])
    authorId = int(item["AuthorId"])
    if authorId not in dict_paperId_to_authors:
        dict_paperId_to_authors[authorId] = []
    dict_paperId_to_authors[authorId].append(paperId)
print("dict1 is OK!")

dict2 = {}
for item in data2:
    paperId = int(item["Id"])
    Cid = int(item["ConferenceId"])
    Jid = int(item["JournalId"])
    if paperId not in dict2:
        dict2[paperId] = []
    dict2[paperId].append(Cid)
    dict2[paperId].append(Jid)
print("dict2 is OK!")

dict3 = {}
for item in data4:
    Cid = int(item["Id"])
    #ShortName = item["ShortName"]
    #if len(ShortName)==0:
    #    ShortName = "NULL"
    FullName = item["FullName"]
    HomePage = item["HomePage"]
    if Cid not in dict3:
        dict3[Cid] = []
    #dict3[Cid].append(ShortName)
    dict3[Cid].append(FullName)
    dict3[Cid].append(HomePage)
print("dict3 is OK!")

dict4 = {}
for item in data5:
    Jid = int(item["Id"])
    #ShortName = item["ShortName"]
    FullName = item["FullName"]
    HomePage = item["HomePage"]
    #if len(ShortName)==0:
    #    ShortName = "NULL"
    if Jid not in dict4:
        dict4[Jid] = []
    #dict4[Jid].append(ShortName)
    dict4[Jid].append(FullName)
    dict4[Jid].append(HomePage)
print("dict4 is OK!")
'''


'''
# 论文的会议与期刊信息
for paperId in dict2:
    FullName = ""
    HomePage = ""
    Cid = dict2[paperId][0]
    Jid = dict2[paperId][1]
    if dict3.__contains__(Cid):
        Cid = dict2[paperId][0]
        print("!")
        FullName = dict3[Cid][0]
        HomePage = dict3[Cid][1]
    if dict4.__contains__(Jid):
        Jid = dict2[paperId][1]
        FullName = dict4[Jid][0]
        HomePage = dict4[Jid][1]
    writer.writerow([paperId, FullName, HomePage])
'''
'''
# 作者写过的论文的会议与期刊信息
for authorId in dict_paperId_to_authors:
    papers = dict_paperId_to_authors[authorId]
    n = len(papers)
    str2 = ""
    str3 = ""
    #str5 = ""
    #str6 = ""
    for i in range(n):
        paperId = papers[i]
        if dict2.__contains__(paperId):
            Cid = dict2[paperId][0]
            if dict3.__contains__(Cid):
                print(dict3[Cid])
                #str1 = str1 + dict3[Cid][0] + " "
                str2 = str2 + dict3[Cid][0] + " "
                str3 = str3 + dict3[Cid][1] + " "
            Jid = dict2[paperId][1]
            if dict4.__contains__(Jid):
                #str4 = str4 + dict4[Jid][0] + " "
                str2 = str2 + dict4[Jid][0] + " "
                str3 = str3 + dict4[Jid][1] + " "
    writer.writerow([authorId, str2, str3])
'''
print("OK!!!")
