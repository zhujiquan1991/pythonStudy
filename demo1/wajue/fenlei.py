# -* - coding:UTF-8 -* -
# 分类数据
import sklearn
import pandas
df = pandas.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.3,'class1']])
df.columns = ['color','size','price','classlabel']
#进行有序
size_mapping = {
    'XL':3,
    'L':2,
    'M':1
}
df['size'] = df['size'].map(size_mapping)
print df
