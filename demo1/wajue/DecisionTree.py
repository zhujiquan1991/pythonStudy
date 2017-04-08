# -* - coding:UTF-8 -* -
# 回归决策树
# 1.数据处理变成整形 2.选择嫡算法 3.进行python算法 4.进行决策树可视化
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
import csv
filePath = '../resource/DecisionTree.csv'
allElectronicsData = open(filePath,'r')
reader = csv.reader(allElectronicsData)
headers = reader.next() #打印第一行 label
print headers
# 数据的预处理
# youth middle_age senor 1 0 0 high medium low 1 0 0 转为三维格式
featureList = [] #特征值的值
labelList = [] #目的列
# 把包含字典数据的list 转换成三维格式 DictVectorizer()
for row in reader:
    #labelDict['class_busy'] = row[len(row) - 1]
    #labelList.append(labelDict)
    labelList.append(row[len(row) -1])
    rowDict = {}
    for i in range(1,len(row) -1):
        rowDict[headers[i]] = row[i] #字典数据插入
    featureList.append(rowDict)
print (featureList)
# 利用DictVectorizer()进行对包含字典数组的list三维格式转换
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print ("dummyX:" + str(dummyX)) #打印三维格式
print (vec.get_feature_names())

print ("labelList:" + str(labelList))

# 进行目标列的转换
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print ("dummY:" + str(dummyY))

# 使用python决策树方法
clf = tree.DecisionTreeClassifier(criterion=('entropy'))
clf = clf.fit(dummyX,dummyY) #建模
print ("clf:" + str(clf))

# 生成决策树图形输出
with open("../resource/DecisionTreeGraph.dot",'w') as f:
    #第二个参数为还原label
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)
# 利用 'dot -Tpdf inis.dot -o outpu.pdf' 命令，可将dot转换成直观的pdf

# 进行数据预测
oneRowX = dummyX[0,:] #二维数组（0代表第一场，':'获取整条数据）
print ("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1 #换成中年人
newRowX[2] = 0 #换成中年人 组合起来就是 1 0 0 中年人(三维)

predictedY  = clf.predict(newRowX)
print ("predictdY: " + str(predictedY))
