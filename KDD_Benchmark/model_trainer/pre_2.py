#encoding=utf-8
import util
import os
import csv
import json
import jieba
import gc

PaperAuthor_path = "../data/dataset/PaperAuthor.csv"
Paper_path = "../data/dataset/Paper.csv"
out_path = "../data/dataset/result.csv"

print("data loading...")
data1 = util.read_dict_from_csv(PaperAuthor_path)
print("data1 loaded!")
data2 = util.read_dict_from_csv(Paper_path)
print("data2 loaded!")

out = open(out_path, 'w', newline='',errors='ignore')
writer = csv.writer(out,dialect='excel')
writer.writerow(["AuthorId","Keyword"])

dict_paperId_to_authors = {}
for item in data1:
    paperId = int(item["PaperId"])
    authorId = int(item["AuthorId"])
    if authorId not in dict_paperId_to_authors:
        dict_paperId_to_authors[authorId] = []
    dict_paperId_to_authors[authorId].append(paperId)
    #gc.collect()
print("dict1 is OK!")

dict2 = {}
for item in data2:
    paperId = int(item["Id"])
    Keyword = item["Title"] + item["Keyword"]
    seg = jieba.cut(Keyword, cut_all=True)
    if paperId not in dict2:
        dict2[paperId] = ' '.join(seg)
    #gc.collect()
print("dict2 is OK!")

for authorId in dict_paperId_to_authors:
    papers = dict_paperId_to_authors[authorId]
    n = len(papers)
    str = ""
    for i in range(n):
        paperId = papers[i]
        if dict2.__contains__(paperId):
            str += dict2[paperId]
    print("!")
    writer.writerow([authorId, str])
    #gc.collect()
print("OK!")