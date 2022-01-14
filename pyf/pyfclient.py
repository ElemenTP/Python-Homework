import aiohttp
import asyncio
import json
import numpy as np
import matplotlib.pyplot as plt
from geojson import Polygon


async def main():
    inquireUrl = "http://localhost:8080/api"
    inputstr = input("输入要查询的多边形角坐标（形如[2.38, 57.322],[23.194, -20.28]，先经度后纬度，点需首尾相接）:\n")
    inputstr = "[[" + inputstr + "]]"
    inputjson = json.loads(inputstr)
    p = Polygon(inputjson, validate=True)
    resultlist = None
    async with aiohttp.ClientSession() as session:
        async with session.post(inquireUrl, data=json.dumps(p)) as response:
            if response.status != 200:
                print("数据获取失败，代码", response.status)
                return
            resultlist = await response.json()
    array = np.array(inputjson[0])
    plt.plot(
        np.asarray(array[:, 0], dtype=np.float64),
        np.asarray(array[:, 1], dtype=np.float64),
        "o-",
        c="#A9A9A9",
        mfc="#FFFFFF",
    )
    maxpop = 0.0
    for s in resultlist:
        curpop = s["population"]
        if curpop > maxpop:
            maxpop = curpop
    xarr = list()
    yarr = list()
    color = list()
    for s in resultlist:
        xarr.append(s["lonlat"][0])
        yarr.append(s["lonlat"][1])
        color.append(int((s["population"] / maxpop) * 100))
    size = int(400 / pow((len(resultlist) / 80), 1.5))
    if size == 0:
        size = 1
    plt.scatter(xarr, yarr, c=color, s=size, cmap="viridis")
    plt.colorbar()
    plt.savefig("res.jpg", dpi=640.0)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
