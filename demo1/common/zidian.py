# -* - coding:UTF-8 -* -
import sys
# 两种方式定义
info1 = dict(name = 'zhujiquan') #更优雅
info2 = {'name2':'zhujiquan2'}
# 获取方式
print info1['name']
print info2.get('name') #返回None #更优雅
#print info2['name'] #会抛出keyErro异常
info1.update(name = 'zhujishu') #更新字典
print info1.get('name')
info1.setdefault('name2','jishu') #添加字典
print info1
del info1['name'] #删除字典
print info1.get('name')
print info1.keys() #获取所有key
#获取key,value循环
info1.setdefault('test','test')
for key,value in info1.items():
    print key,':',value
#字典的排序方法 sorted()
#全局字典 sys.moudles 模块 -- 加载到缓存中，具有字典的一切方法
print sys.modules.keys() #自动加载Py默认的模块-包含了你在 IDE 中运行的所有程序所导入的所有模块
print 'os:',sys.modules.get('os')



