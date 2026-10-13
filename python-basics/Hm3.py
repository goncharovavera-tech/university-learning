import pandas as pd
import numpy as np

# НАСТРОЙКА ВЫВОДА PANDAS: заставляем его выводить всё без сокращений
pd.set_option('display.max_rows', None)      # Выводить ВСЕ строки (без многоточий)
pd.set_option('display.max_columns', None)   # Выводить ВСЕ столбцы
pd.set_option('display.width', 1000)         # Ширина экрана для вывода (чтобы строки не переносились)


df = pd.read_csv("Hm3_task_file.txt", skipinitialspace=True)
df_copy = pd.DataFrame(columns = ['EMAIL', 'NAME', 'LAST_NAME', 'TEL', 'CITY'])
for i in range(len(df)):
    if pd.notna(df.loc[i, "NAME"]):
        if pd.notna(df.loc[i, "LAST_NAME"]) and pd.notna(df.loc[i, "TEL"]) and pd.notna(df.loc[i, "CITY"]):
           if len(df.loc[i]["TEL"]) == 7:
               email_name = str(df.loc[i, 'NAME'])[0].lower()
               email_last = str(df.loc[i, 'LAST_NAME']).lower()
               generated_email = f"{email_name}.{email_last}@gmail.com"

               df_copy.loc[len(df_copy)] = [
                   generated_email,
                   df.loc[i, 'NAME'],
                   df.loc[i, 'LAST_NAME'],
                   df.loc[i, 'TEL'],
                   df.loc[i, 'CITY']
               ]
df_copy.to_csv('Hm3_result.txt', sep=' ', index=False, encoding='utf-8')