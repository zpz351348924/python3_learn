#-*-encoding=utf-8-*-
import requests
import re

#拿到所有股票代码,该网站是JS加载，通过找到API相关规律，用正则提取
def get_all_gupiao():
    url_list = []
    for i in range(1, 8):
        url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22hq%22,%22hs_a%22,%22%22,0,{},500]]&callback=FDC_DC.theTableData'.format(
            i)
        response = requests.get(url)
        item_list = re.findall('[A-Za-z]{2}\d{6}', response.text)
        #print item_list
        #print len(item_list)
        list_to_str = str(item_list)[1:-1]
        #print list_to_str
        url_list.append(list_to_str)
    get_url_str = str(url_list)[1:-1]
    print get_url_str
    return get_url_str

if __name__ == '__main__':
    get_all_gupiao()