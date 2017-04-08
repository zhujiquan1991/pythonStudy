# -* - coding:UTF-8 -* -
# 缺失值处理
from io import StringIO
from sklearn.preprocessing import Imputer
import pandas
csv_data = '''A,b,C,D
              1.0,2.0,3.0,4.0
              5.0,6.0,,8.0
              0.0,11.0,12.0'''
csv_data = unicode(csv_data)
df = pandas.read_csv(StringIO(csv_data))
imr = Imputer(missing_values='NaN',strategy='mean',axis=0)
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print df.values
print "**" * 15
print imputed_data