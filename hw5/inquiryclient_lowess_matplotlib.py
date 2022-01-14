#!/usr/bin/python3
import asyncio
import json
import xml.etree.ElementTree as xml

import aiohttp
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

lowess = sm.nonparametric.lowess


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

    resList.sort(key=lambda d: d[0])

    resList = np.array(resList)

    xarr = np.asarray(resList[:, 0], dtype=np.uint16)
    yarr = np.asarray(resList[:, 1], dtype=np.float64)

    yest = lowess(
        endog=yarr,
        exog=xarr,
        frac=float(10 / len(resList)),
        is_sorted=True,
        return_sorted=True,
    )[:, 1]

    plt.plot(xarr, yarr, "o-", c="#A9A9A9", mfc="#FFFFFF")
    plt.plot(xarr, yest, c="#000000")
    plt.title("Temperature anomaly by year")
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly")
    plt.grid(c="#808080", linewidth="0.2")
    plt.show()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
