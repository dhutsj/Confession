from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)
#装饰器加函数一起构成视图
@app.route('/')
def hello_world():
    lucky_number = randint(1,100)
    return render_template('lucky.html',luck_num=lucky_number)
@app.route('/love/')
def love():
    return render_template('love.html')


'''
模板是一种文件，它告诉应用或框架你想要如何显示数据。Flask使用HTML和Jinja的组合。HTML关注如何架构网页，而Jinja的主要任务是把动态的信息插入到页面中，
并且添加一些逻辑，比如for循环或if判断。在创建模板之前，必须准备一个地方来存放它们。在此python脚本所在的同一个目录下创建一个名为templates的文件夹，
将所有的模板都保存在这里。
'''

if __name__ == '__main__':
    app.run()

