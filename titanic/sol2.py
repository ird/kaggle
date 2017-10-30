import numpy as np
import pandas as pd
from sklearn import tree

train = pd.read_csv('train.csv')
train['Sex'][train['Sex'] == 'male'] = 0
train['Sex'][train['Sex'] == 'female'] = 1

train['Age'] = train['Age'].fillna(train.Age.median())
train['Pclass'] = train['Pclass'].fillna(train.Pclass.median())
train['Fare'] = train['Fare'].fillna(train.Fare.median())

target = train['Survived'].values
features = train[['Pclass', 'Sex', 'Age', 'Fare']].values

tr = tree.DecisionTreeClassifier(max_depth=4)
tr = tr.fit(features, target)
print(tr.feature_importances_)
print(tree.export_graphviz(tr, out_file="tree.dot",
      feature_names=['Pclass', 'Sex', 'Age', 'Fare']))

test = pd.read_csv('test.csv')
test['Sex'][test['Sex'] == 'male'] = 0
test['Sex'][test['Sex'] == 'female'] = 1

test['Age'] = test['Age'].fillna(test.Age.median())
test['Pclass'] = test['Pclass'].fillna(test.Pclass.median())
test['Fare'] = test['Fare'].fillna(test.Fare.median())

test_features = test[['Pclass', 'Sex', 'Age', 'Fare']]
test['Survived'] = tr.predict(test_features)
test.to_csv('sol2.csv', index=False,
            columns=['PassengerId', 'Survived'])
# PassengerId = np.array(test['PassengerId']).astype(int)
# sol2 = pd.DataFrame(pred, PassengerId, columns=['Survived'])
# print(sol2)
