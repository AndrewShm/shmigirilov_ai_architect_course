import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder
import random

                # Функция для создания DataFrame и записи в CSV файл
                def createFrame(filename='data.csv'):
    data = {
        'python_language': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'sql_language': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'machine learning': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'music': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'philosophy': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'economy': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'time_fw_in_min': [int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)] * 400,
        'final_work': ['удовлетворительно', 'хорошо', 'отлично', 'удовлетворительно', 'хорошо'] * 400
    }

df = pd.DataFrame(data)
df.to_csv('train_data.csv', index=False)

