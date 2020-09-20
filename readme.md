# 测试连通性的Mock

1. 在本地启动pycharm

2. 服务地址是http://127.0.0.1:5000/

3. 调用getListMock方法：

   ```
   http://127.0.0.1:5000/getListMock/date
   ```

   其中date是一个参数，可以是2019-01-02，返回的是date

- Mock仅仅用来测试连通性。真正的数据还没拿到的。