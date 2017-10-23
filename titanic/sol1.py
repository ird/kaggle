import pandas as pd

if __name__ == "__main__":
    test = pd.read_csv('test.csv')
    test['Survived'] = 0
    test['Survived'][test['Sex'] == 'female'] = 1
    test.to_csv('solution.csv', index=False,
                columns=['PassengerId', 'Survived'])
