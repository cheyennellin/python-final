#!/usr/bin/env python
# coding: utf-8

# # 在 ipynb交互式环境下模拟后台
# 
# * 用浏览器务必注意后台 port 数字位置
# * port = 8005

# In[ ]:


from flask import Flask, render_template, request
import pandas as pd

# 模块读进来, 组合拳  组合拳  组合拳
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

# 准备工作 
# pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值, 不重覆
df = pd.read_csv('gender.csv', encoding='utf-8')
regions_available_loaded = list(df.region.dropna().unique())
# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])
def hu_run_2019():

    data_str = df.to_html()  # 使用pandas 数据框之方法.to_html() !! 取代原 "Hello"
                             # pandas真是数据科学家的好朋友!
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,   # 表
                           the_select_region=regions_available)   

@app.route('/hurun',methods=['POST'])
def hu_run_select() -> 'html':
    
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)                                 ## 检查用户输入, 在后台

    dfs = df.query("region=='{}'".format(the_region)) ## 使用df.query()方法. 按用户交互输入the_region过滤

    

    data_str = dfs.to_html()  # 数据产出dfs, 完成互动过滤呢

    ## plot_all = "交互式图还没做好" # <------------------交互式图  其實應該放這, 按過濾出的數據來做圖
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
    py.offline.plot(fig, filename="成果.html",auto_open=False)                  # 備出"成果.html"檔案之交互圖
    with open("成果.html", encoding="utf8", mode="r") as f:                     # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())
    
    regions_available =  regions_available_loaded #下拉选单有内容
    shuo= (' '.join(list(dfs.shuoming[0:1])))
    title=(' '.join(list(dfs.title[0:1])))
    return render_template('results2.html',
	                        the_title= title,
                            the_plot_all = plot_all,
							the_xixi= shuo,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )
if __name__ == '__main__':
    app.run(debug=True,port=8002)						 