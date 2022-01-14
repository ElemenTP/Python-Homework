#!/usr/bin/python3
import aiohttp
import asyncio
import json
import xml.etree.ElementTree as xml


async def getInquireResult(url, startYear, endYear, isLower) -> str:
    params = dict()
    if startYear != "":
        params["start"] = int(startYear)
    if endYear != "":
        params["end"] = int(endYear)
    if isLower:
        params["order"] = "lower"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            res = await response.text()
            return res


async def main():
    inquireUrl = "http://localhost:8080"

    typeChoice = input("选择数据查询格式：1 for json，2 for csv，3 for xml:")
    if typeChoice == "2":
        inquireUrl = inquireUrl + "/csv"
    elif typeChoice == "3":
        inquireUrl = inquireUrl + "/xml"
    else:
        inquireUrl = inquireUrl + "/json"

    startYear = input("输入起始年份：")
    endYear = input("输入结束年份：")
    isLower = input("是否倒序排列结果：y for yes，n for no：") == "y"

    res = await getInquireResult(inquireUrl, startYear, endYear, isLower)

    resList = list()
    if typeChoice == "2":
        lines = res.split("\n")
        lines.pop(0)
        lines.pop(len(lines) - 1)
        for line in lines:
            words = line.split(",")
            resList.append(words)
    elif typeChoice == "3":
        root = xml.fromstring(res)
        tempList = list()
        for child in root:
            tempList.append(child.text)
            if len(tempList) == 2:
                resList.append(list(tempList))
                tempList.clear()
    else:
        resList = json.loads(res)

    print("查询结果：")
    print("年份\t温度")
    for k, v in resList:
        print(k, "\t", v)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
