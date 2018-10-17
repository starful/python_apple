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
 
# Pipeline���쐬
# �f�[�^�̐��K����SVM���`
pipeline = Pipeline([
        ('standard_scaler', StandardScaler()),
        ('svm', SVC())])
 
# �p�����[�^�̒T���͈͂��w��
# Grid Search�p�̃p�����[�^�͖{���ł���΂����ƍׂ���������ق�������
params = {
    'svm__C' : np.logspace(0, 2, 5),
    'svm__gamma' : np.logspace(-3, 0, 5)
}
 
# Grid Search���s��
clf = GridSearchCV(pipeline, params)
clf.fit(train_X, train_y)
 
pred = clf.predict(test_X)
 
# ���ʂ̃��|�[�e�B���O
print(classification_report(test_y, pred))
print(confusion_matrix(test_y, pred))
 
# ���f���̕ۑ�
# API�Ȃǂŗ��p����ۂ�joblib.load�ŕۑ��������f����ǂݍ���ŁA���͂��ꂽ�f�[�^�ɑ΂���predict���s���Ηǂ�
joblib.dump(clf, 'clf.pkl') 
