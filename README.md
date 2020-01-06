# python-final
## 探讨女性遭受的性暴力风险
[github_url](https://github.com/cheyennellin/python-final)
[pythonanywhere URL](http://doublegood.pythonanywhere.com/)

* 打开方式
   * 下拉框点击跳转
   * 点击导航栏
 
url总共两个
* [主页](http://doublegood.pythonanywhere.com/)
* [女性性暴力](http://nfunm059.gitee.io/index/)

#### Project Structure
    -statics
        - hf(1).css
    -templates
        - 成果.html
		- results2.html
		- base.html
		- entry.html
    - aaa.py
    -js
      -echarts.min.js
    -gender.csv

#### html档描述
- base.html:基础页面，引用了bootstrap模板，导航栏可选择kill 差异等对应页面
- emtru.html:承接页码，用来连接result.html
- results2.html:主页面，用来存放数据页面
- kill:用来展示女性受到暴力程度
- 成果.html:17级所制作图表

#### python档描述
* 导入应用模块
```
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
```
* 传递数据
```
@app.route('/',methods=['GET']) 
def hu_run_2019(): 
 data_str = df.to_html() # 使用pandas 数据框之方法.to_html() !! 取代原 "Hello" 
# pandas真是数据科学家的好朋友! 
 regions_available = regions_available_loaded #下拉选单有内容 
return render_template('results2.html', 
the_res = data_str, # 表 
the_select_region=regions_available)  
  @app.route('/hurun',methods=['POST']) 
def hu_run_select() -> 'html': 
 the_region = request.form["the_region_selected"] ## 取得用户交互输入 
print(the_region) ## 检查用户输入, 在后台 
 dfs = df.query("region=='{}'".format(the_region)) ## 使用df.query()方法. 按用户交互输入the_region过滤 
   data_str = dfs.to_html() # 数据产出dfs, 完成互动过滤呢 
 ## plot_all = "交互式图还没做好" # <------------------交互式图 其實應該放這, 按過濾出的數據來做圖 
## 交互式可视化画图 
fig = go.Figure(data=go.Choropleth( 
locations = dfs['CODE'], 
z = list(dfs['value']), 
text = dfs['country'], 
colorscale = 'Reds', 
autocolorscale=False, 
reversescale=True, 
marker_line_color='white', 
marker_line_width=0.5, 
colorbar_tickprefix = '', 
colorbar_title = '性别差异指数' 
)) 
py.offline.plot(fig, filename="成果.html",auto_open=False) # 備出"成果.html"檔案之交互圖 
with open("成果.html", encoding="utf8", mode="r") as f: # 把"成果.html"當文字檔讀入成字符串 
plot_all = "".join(f.readlines()) 
 regions_available = regions_available_loaded #下拉选单有内容 
shuo= (' '.join(list(dfs.shuoming[0:1]))) 
title=(' '.join(list(dfs.title[0:1]))) 
return render_template('results2.html', 
the_title= title, 
the_plot_all = plot_all, 
the_xixi= shuo, 
the_res = data_str, 
the_select_region=regions_available, 
) 
 
```

##### Web App动作描述：
制作下拉框
```
@app.route('/',methods=['GET'])
def hu_run_2019():

    data_str = df.to_html()  
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,   # 表
                           the_select_region=regions_availal
```




