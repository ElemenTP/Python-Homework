import json
import numpy as np
from sanic import Sanic
from sanic import response
from geojson import Polygon
from shapely import geometry as geo
import threading

app = Sanic("PopulationDataInquireServer")


def fetchPopulationFromFile(lon, lat):
    global mutex, datafile
    x = int((lat + 90) * 5)
    y = int((lon + 180) * 5)
    offset = (x * 1800 + y) * 15
    mutex.acquire()
    datafile.seek(offset, 0)
    resstr = datafile.read(14)
    mutex.release()
    return float(resstr)


def calcPopulation(polygon: Polygon):
    global step, cellarea
    p = geo.Polygon(polygon["coordinates"][0])
    lonMin, latMin, lonMax, latMax = p.bounds
    resultlist = list()
    for lat in np.arange(latMin, latMax, step, dtype=np.float64):
        for lon in np.arange(lonMin, lonMax, step, dtype=np.float64):
            cellLon1 = lon - lon % step - step
            cellLon2 = lon - lon % step + step
            cellLat1 = lat - lat % step - step
            cellLat2 = lat - lat % step + step
            cellPolygon = geo.Polygon(
                [
                    (cellLon1, cellLat1),
                    (cellLon2, cellLat1),
                    (cellLon2, cellLat2),
                    (cellLon1, cellLat2),
                ]
            )
            intersection = cellPolygon.intersection(p)
            if not intersection.is_empty:
                curpop = fetchPopulationFromFile(cellLon1, cellLat1)
                if curpop > 0.0:
                    resultlist.append(
                        {
                            "lonlat": [lon, lat],
                            "population": (intersection.area / cellarea) * curpop,
                        }
                    )
    return resultlist


@app.listener("before_server_start")
async def open_file(app, loop):
    global datafile
    datafile = open("datagrid.asc", "r")


@app.listener("after_server_stop")
async def close_file(app, loop):
    datafile.close()


@app.post("/api")
async def postapi(request):
    p = Polygon.to_instance(json.loads(request.body))
    resultlist = calcPopulation(p)
    return response.json(body=resultlist)


if __name__ == "__main__":
    datafile = None
    mutex = threading.Lock()
    step = 360 / 1800
    cellarea = geo.Polygon([(0, 0), (0, step), (step, step), (step, 0)]).area
    app.run(host="127.0.0.1", port=8080)
