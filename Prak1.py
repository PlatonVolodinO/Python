import pandas as pd
import csv

# Загрузка данных о продажах и инвентаре
sales_data = pd.read_csv('MS-b1-sell.csv')
inventory_data = pd.read_csv('MS-b1-inventory.csv')
# Расчет оставшегося количества продуктов на складе для каждого дня

mas_sku_num = list(sales_data.sku_num)
mas_date = list(sales_data.date)
cur_day = mas_date[0]
mas_res = []
month_sum_ap = 0
month_sum_pe = 0
for i in range(len(mas_date)-1):
    if mas_date[i] == cur_day:
        if str(mas_sku_num[i])[6] == 'a':
            month_sum_ap += 1
        else:
            month_sum_pe += 1
    else:
        cur_day = mas_date[i]
        mas_res.append([mas_date[i], [month_sum_ap, month_sum_pe]])
        month_sum_ap = 0
        month_sum_pe = 0
        if str(mas_sku_num[i])[6] == 'a':
            month_sum_ap += 1
        else:
            month_sum_pe += 1


with open("old.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["date", "apple", "pen"])
    for i in range(len(mas_res)):
        file_writer.writerow([mas_res[i][0], mas_res[i][1][0], mas_res[i][1][1]])

mas_date = list(inventory_data.date)
mas_ap = list(inventory_data.apple)
mas_pe = list(inventory_data.pen)

k = 0
cur_day = mas_date[k]
cur_ap = mas_ap[k]
cur_pe = mas_pe[k]
for i in range(len(mas_res)):
    if (str(cur_day)[5] == str(mas_res[i][0])[5]) and (str(cur_day)[6] == str(mas_res[i][0])[6]):
        cur_ap = cur_ap - mas_res[i][1][0]
        mas_res[i][1][0] = cur_ap
        cur_pe = cur_pe - mas_res[i][1][1]
        mas_res[i][1][1] = cur_pe
    else:
        k += 1
        cur_day = mas_date[k]
        cur_ap = mas_ap[k]
        cur_pe = mas_pe[k]
        cur_ap = cur_ap - mas_res[i][1][0]
        mas_res[i][1][0] = cur_ap
        cur_pe = cur_pe - mas_res[i][1][1]
        mas_res[i][1][1] = cur_pe


with open("res.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["date", "apple", "pen"])
    for i in range(len(mas_res)):
        file_writer.writerow([mas_res[i][0], mas_res[i][1][0], mas_res[i][1][1]])
