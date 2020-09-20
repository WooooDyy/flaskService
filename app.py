from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_Wind():
    return 'Hello Wind!'


# 获取列表的。一天执行一次
# 格式 2019-01-20
@app.route('/getList/<string:date>', methods=['GET'])
def getList(date):
    print(request.url)  # 请求的http网址
    # date = request.args.to_dict()  # 解析http中的参数
    # TODO 返回期权列表，一天执行一次



    return str(date)  # 注意，不管什么问题，一定要返回，就算是返回None


@app.route('/getOptions', methods=['GET'])
def getOptions():
    # TODO 返回期权的属性


    return



if __name__ == '__main__':
    app.run()
