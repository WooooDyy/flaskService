from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_Wind():
    return 'Hello Wind!'


# 获取列表的。一天执行一次
# 格式 2019-01-20
@app.route('/getListMock/<string:date>', methods=['GET'])
def getListMock(date):
    print(request.url)  # 请求的http网址
    # date = request.args.to_dict()  # 解析http中的参数
    # TODO 返回期权列表，一天执行一次
    # Mock 仅仅用来测试连通性，原来的数据组织跟现在的数据组织是不一样的，所以返回一个date测试连通性即可，之后的测试要一起来。




    return str(date)


@app.route('/getOptions', methods=['GET'])
def getOptionsMock():
    # TODO 返回期权的属性


    return



if __name__ == '__main__':
    app.run()
