# coding: Shift_JIS
import numpy as np
 
from sklearn.datasets import load_digits
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.externals import joblib
 
digits = load_digits(10)
 
train_X = digits.data[:1500]
train_y = digits.target[:1500]
 
test_X = digits.data[1500:]
test_y = digits.target[1500:]
 
# Pipelineを作成
# データの正規化とSVMを定義
pipeline = Pipeline([
        ('standard_scaler', StandardScaler()),
        ('svm', SVC())])
 
# パラメータの探索範囲を指定
# Grid Search用のパラメータは本来であればもっと細かくやったほうがいい
params = {
    'svm__C' : np.logspace(0, 2, 5),
    'svm__gamma' : np.logspace(-3, 0, 5)
}
 
# Grid Searchを行う
clf = GridSearchCV(pipeline, params)
clf.fit(train_X, train_y)
 
pred = clf.predict(test_X)
 
# 結果のレポーティング
print(classification_report(test_y, pred))
print(confusion_matrix(test_y, pred))
 
# モデルの保存
# APIなどで利用する際はjoblib.loadで保存したモデルを読み込んで、入力されたデータに対してpredictを行えば良い
joblib.dump(clf, 'clf.pkl') 
