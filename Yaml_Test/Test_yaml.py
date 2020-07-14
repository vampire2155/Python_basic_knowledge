import yaml
yamlDir = r'G:\Python_autoAPI\data\testcase.yaml'
with open(yamlDir,'r',encoding='utf-8') as fo:
    res = yaml.load_all(fo,Loader=yaml.FullLoader)
    for one in res:
        print (type(one))
        print (one[1]["retcode"])
# print (res[0]['data']['age'])
# print (type(res[0]['data']['age']))