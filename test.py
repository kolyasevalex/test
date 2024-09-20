# from torch.utils.tensorboard import SummaryWriter
# # tensorboard --logdir=C:\Users\b\PycharmProjects\test\logs
#
# writer = SummaryWriter("logs")
# for i in range(100):
#     writer.add_scalar("y=2x", 2 * i, i)
# writer.close()

import numpy as np
import pandas as pd
import os

# Указываем путь к директории
directory = "D:/mxi-924"

# Получаем список файлов
files = os.listdir(directory)
# for elem in files:
#     abs_file_path = os.path.join(directory, elem)
#     abs_file_path2=os.path.join(directory, elem[-10:])
#     try:
#         os.rename(abs_file_path, abs_file_path2)
#     except FileNotFoundError:
#         print("Файл не найден")
#     except PermissionError:
#         print("Нет доступа для переименования файла")

# Выводим список файлов
dest = []
for elem in files:
    abs_file_path = os.path.join(directory, elem)
    df = pd.read_csv(abs_file_path, sep=';', header=None)
    df = np.asarray(df)
    now=100000
    numBuy=0
    numSell=0
    volBuy=0
    volSell=0
    for row in df:
        if row[1] >= 100000:
            if row[1] > now+59:
                ln=[0]*8
                ln[0]=row[0]
                ln[1]= now
                ln[2]= close
                ln[3]=numBuy
                ln[4]=volBuy
                ln[5]=numSell
                ln[6]=volSell
                dest.append(ln)
                numBuy = 0
                numSell = 0
                volBuy = 0
                volSell = 0
                now=row[1]
            close=row[2]
            if row[5] == 'B' :
                numBuy+=1
                volBuy+=row[3]
            else:
                numSell += 1
                volSell += row[3]
    ln = [0] * 8
    ln[0] = row[0]
    ln[1] = now
    ln[2] = close
    ln[3] = numBuy
    ln[4] = volBuy
    ln[5] = numSell
    ln[6] = volSell
    dest.append(ln)
df=pd.DataFrame(dest)
abs_file_path = os.path.join(directory, "mxi924min.csv")
df.to_csv(abs_file_path, sep=';', index=False,header=False)
#    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in



