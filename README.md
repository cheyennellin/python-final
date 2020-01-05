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
		- results.html
		- base.html
		- entry.html
    - aaa.py
	-js
	   -echarts.min.js
	-gender.csv

#### html档描述
- base.html:基础页面，引用了bootstrap模板，导航栏可选择kill 差异等对应页面
- emtru.html:承接页码，用来连接result.html
- results.html:主页面，用来存放数据页面
- kill:用来展示女性受到暴力程度
- 成果.html:17级所制作图表

#### python档描述
```
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
```

##### Web App动作描述：
```
@app.route('/',methods=['GET'])
def hu_run_2019():

    data_str = df.to_html()  
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,   # 表
                           the_select_region=regions_availal
```




