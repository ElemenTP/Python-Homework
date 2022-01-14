from sanic import Sanic
from sanic import response
import os
import xml.etree.ElementTree as xml

filePath = os.path.dirname(os.path.realpath(__file__))

app = Sanic("WeatherDataInquireServer")


def getResult(isLower, startYear, endYear) -> list:
    tempDict = dict()
    for k, v in app.config.myDict.items():
        if startYear <= k and k <= endYear:
            tempDict[k] = v[0]
    res = sorted(tempDict.items(), key=lambda d: d[1], reverse=isLower)
    return res


@app.listener("before_server_start")
async def load_file(app, loop):
    app.config.myDict = dict()
    data_path = f"{filePath}/test.txt"
    with open(data_path) as f:
        for line in f.readlines():
            words = line.split()
            if words[0].startswith("#"):
                continue
            year = int(words[0])
            app.config.myDict[year] = (float(words[1]),)


@app.get("/json")
async def returnJson(request):
    isLower = request.args.get("order", "higher") == "lower"
    startYear = int(request.args.get("start", 1880))
    endYear = int(request.args.get("end", 2020))
    res = getResult(isLower, startYear, endYear)
    return response.json(res)


@app.get("/csv")
async def returnCsv(request):
    isLower = request.args.get("order", "higher") == "lower"
    startYear = int(request.args.get("start", 1880))
    endYear = int(request.args.get("end", 2020))
    res = getResult(isLower, startYear, endYear)
    resCsv = "year,temper\n"
    for k in res:
        resCsv = resCsv + (f"{k[0]},{k[1]}\n")
    return response.text(resCsv)


@app.get("/xml")
async def returnXml(request):
    isLower = request.args.get("order", "higher") == "lower"
    startYear = int(request.args.get("start", 1880))
    endYear = int(request.args.get("end", 2020))
    res = getResult(isLower, startYear, endYear)
    root = xml.Element("temperature_table")
    for i in res:
        year = xml.SubElement(root, "year")
        temper = xml.SubElement(root, "temper")
        year.text = str(i[0])
        temper.text = str(i[1])
    return response.text(
        xml.tostring(
            element=root,
            encoding="unicode",
            xml_declaration=True,
            short_empty_elements=True,
        )
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
