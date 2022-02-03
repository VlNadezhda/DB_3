import numpy as np
import pandas

#Считываем данные из  csv файла и оставляем нужные нам столбцы.
data = pandas.read_csv('EAR_4MTH_SEX_OCU_CUR_NB_A.csv')
data = data[['ref_area','sex','classif1','classif2','time','obs_value']]

data_ref_area = pandas.read_csv('ref_area_en.csv', index_col = 'ref_area')

#Переименовываем столбец в таблице со странами.
data_ref_area = data_ref_area.rename(columns={' ref_area.label':'ref_area_label'})
data_ref_area = data_ref_area[['ref_area_label']]

#Добавляем столбец чтобы лучше понимать к какой стране относятся данные.
data = data.join(data_ref_area, on = ['ref_area'])

#Выведем данные по России за период от 2010 до 2015 года.
# print(data[(data.ref_area == 'RUS') & ((data.time >= 2010) & (data.time <= 2015))])
first_data = data;
# first_data = first_data[['ref_area','classif1','classif2','obs_value']]
data_classif1 = pandas.read_csv('classif1_en.csv', index_col = 'classif1')
data_classif1 = data_classif1.rename(columns={' classif1.label':'classif1_label'})
data_classif1 = data_classif1[['classif1_label']]
first_data = first_data.join(data_classif1, on = ['classif1'])
col = "classif1_label"
first_data = first_data[['obs_value','ref_area','sex','classif2','time','classif1_label']]
first_data[col] = first_data[col].str.split(':').str[1]
#Топ 20 профессий с самой высокой почасовой оплатой(в долларах)
# print(data[(data.classif2 == 'CUR_TYPE_USD') & (data.sex == 'SEX_F') & (data.classif1 == 'OCU_ISCO08_TOTAL')].sort_values(by = 'obs_value', ascending = False)[:20])

#Топ 20 профессий (на которых работают женщины) с самой высокой почасовой оплатой(в долларах) за 2019 год
print(first_data[(first_data.classif2 == 'CUR_TYPE_USD') & (first_data.time == 2019)& (first_data.sex == 'SEX_F') & (first_data.classif1_label != ' Total')].sort_values(by = 'obs_value', ascending = False)[:20])


# print(first_data)
# print(first_data[(first_data.ref_area == 'USA')][:20])
#Максимальная средняя почасовая зарплата в долларах по миру(любой год):
# print(data[(data.classif2 == 'CUR_TYPE_USD') & (data.sex == 'SEX_T') & (data.classif1 == 'OCU_ISCO08_TOTAL')].obs_value.max())

#Средняя средняя почасовая зарплата в долларах по миру(любой год):
# print(data[(data.classif2 == 'CUR_TYPE_USD') & (data.sex == 'SEX_T') & (data.classif1 == 'OCU_ISCO08_TOTAL')].obs_value.mean())

#Медианная средняя почасовая зарплата в долларах по миру(любой год):
# print(data[(data.classif2 == 'CUR_TYPE_USD') & (data.sex == 'SEX_T') & (data.classif1 == 'OCU_ISCO08_TOTAL')].obs_value.median())

#Топ 20 стран с максимальной почасовой зарплатой за все годы:
# print(data[(data.classif2 == 'CUR_TYPE_USD') & (data.sex == 'SEX_T') & (data.classif1 == 'OCU_ISCO08_TOTAL')].sort_values(by = 'obs_value', ascending = False)[:20])
