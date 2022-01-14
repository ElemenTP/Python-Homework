# Python程序设计-大作业

班级：2019XXXXXX

学号：2019XXXXXX

姓名：XXX

## 作业题目

### 数据

gpw-v4-population-count-rev11_2020_30_sec_asc.zip是一个全球人口分布数据压缩文件，解压后包括了8个主要的asc后缀文件，他们是全球网格化的人口分布数据文件，这些文件分别是：

* gpw-v4-population-count-rev11_2020_30_sec_1.asc
* gpw-v4-population-count-rev11_2020_30_sec_2.asc
* gpw-v4-population-count-rev11_2020_30_sec_3.asc
* gpw-v4-population-count-rev11_2020_30_sec_4.asc
* gpw-v4-population-count-rev11_2020_30_sec_5.asc
* gpw-v4-population-count-rev11_2020_30_sec_6.asc
* gpw-v4-population-count-rev11_2020_30_sec_7.asc
* gpw-v4-population-count-rev11_2020_30_sec_8.asc 

这些文件分布对应地球不同经纬度的范围。

![image-20211221140354827](C:\Users\pirenjie\AppData\Roaming\Typora\typora-user-images\image-20211221140354827.png)

压缩文件下载网页：https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-rev11/data-download

### 服务端

压缩文件（gpw-v4-population-count-rev11_2020_30_sec_asc.zip）是一个全球人口分布数据。基于Sanic实现一个查询服务，服务包括：

* 按给定的经纬度范围查询人口总数，查询结果采用JSON格式。
* 不可以采用数据库，只允许使用文件方式存储数据。
* 可以对现有数据进行整理以便加快查询速度，尽量提高查询速度。

查询参数格式 采用GeoJSON（https://geojson.org/）的多边形（每次只需要查询一个多边形范围，只需要支持凸多边形）

![image-20211221144313148](C:\Users\pirenjie\AppData\Roaming\Typora\typora-user-images\image-20211221144313148.png)

### 客户端

针对上面的查询服务，实现一个服务查询客户端，数据获取后使用Matplotlib散点图（Scatter）进行绘制。

* 横坐标（x轴）为经度。
* 纵坐标（y轴）为维度。

## 服务端代码

程序源代码嵌入下方的code block中。

```python
def fn(x):
    pass

if __name__ == '__main__':
    pass
```

### 代码说明

源代码中不要出现大段的说明注释，代码说明在本节描述。

## 客户端代码

客户端代码嵌入下发的code block中。

```python
import logging

if __name__ == '__main__':
	pass
```

### 代码说明

源代码中不要出现大段的说明注释，代码说明在本节描述。

