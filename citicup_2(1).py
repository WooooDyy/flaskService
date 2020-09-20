# # 获得信息API格式：[所有认购期权的list]和[所有认沽期权的list]
# {
# name:string
# price: int   //价格
# execPrice：int //行权价
# ETFName：string //对应的ETF名称
# ETFPrice：int
# delta：double
# 买一买二：int（这个还在问商院具体概念）

# 期权价格 现价
# 行权价格 转股价格
# ETF价格 正股价格

# }

# #例7. 获取沪股通最新一笔的行情数据
# hksh=w.wset("sectorconstituent","date=2018-06-12;sectorid=1000014938000000").Data[1]
# mk_data=w.wsq(hksh,"rt_last,rt_vol,rt_amt,rt_chg,rt_pct_chg,rt_swing,rt_vwap,rt_upward_vol,rt_downward_vol,rt_ask1,rt_ask2,rt_ask3,rt_ask4,rt_ask5,rt_bid1,rt_bid2,rt_bid3,rt_bid4,rt_bid5")
# #pd.DataFrame(tradecode.Data,index=future.Data[2],columns=tradecode.Times).T
# pd.DataFrame(data.Data,index=data.Fields,columns=data.Codes).T

from WindPy import *
import json

def get_info_data_from_wind(test_resource):
    test_data = test_resource.Data
    test_codes = test_resource.Codes
    test_fields = test_resource.Fields
    test_row = 0
    if len(test_data) != 0:
        test_row = len(test_data[0])

    res_data = []

    for i in range(test_row):
        dict = {
            "code": test_codes[i]
        }

        for idx_field in range(len(test_fields)):
            field = test_fields[idx_field]
            dict[field] = test_data[idx_field][i]

        dict['first_tradedate'] = dict['first_tradedate'].strftime('%Y-%m-%d')
        dict['last_tradedate'] = dict['last_tradedate'].strftime('%Y-%m-%d')
        dict['curr_status'] = None
        res_data.append(dict)

    return res_data

def get_status_data_from_wind(test_resource):
    test_data = test_resource.Data
    test_codes = test_resource.Codes
    test_fields = test_resource.Fields
    test_dict = {}
    test_row = 0
    if len(test_data) != 0:
        test_row = len(test_data[0])
    test_column = 7

    res_data = {}

    for i in range(test_row):
        dict = {}

        for idx_field in range(len(test_fields)):
            field = test_fields[idx_field]
            dict[field] = test_data[idx_field][i]

        res_data[test_codes[i]] = dict

    return res_data

if __name__ == '__main__':
    w.start()

    res_r = {
        'res_option_codes': "",
    }

    info_res = w.wset("optionchain","date=2020-09-16;us_code=510050.SH;option_var=全部;call_put=全部")
    info_res = get_info_data_from_wind(info_res)
    query_list = []
    for r in info_res:
        query_list.append(r['option_code'])
    query_str = ','.join(query_list)

    status_res = w.wsq(query_str, "rt_bid1,rt_bid2,rt_conv_price,rt_last,rt_ustock_price,rt_delta")
    status_res = get_status_data_from_wind(status_res)
    w.stop()

    for idx in range(len(query_list)):
        info_res[idx]['curr_status'] = status_res[query_list[idx]]

    print(json.dumps(info_res, ensure_ascii=False))

