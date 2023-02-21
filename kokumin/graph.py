import math
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

figsize(17, 9)

# Set the font to a Japanese font
# Replace this with the path to your Japanese font file
font_path = './font/gomarice_mukasi_mukasi.ttf'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = 'MS Gothic'
fig, ax = plt.subplots(facecolor="azure", edgecolor="coral", linewidth=2)

# Data on support ratings for the party over time
times = ['2022年1月', '2022年2月', '2022年3月', '2022年4月', '2022年5月', '2022年6月', '2022年7月', '2022年8月', '2022年9月', '2022年10月', '2022年11月', '2022年12月',
         '2023年1月', '2023年2月']  # time periods (e.g. months or years)
support_ratings = [4, 4, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5, 4, 4]  # 毎日新聞
support_ratings2 = [0.8, 1.3, 1.8, 0.6, 2.1, 2.6,
                    2.5, 3.0, 2.9, 2.6, 3.8, 3.2, 2.2, 3.1]  # 共同通信
support_ratings3 = [1.0, 1.0, 1.0, 1.5, 1.2, 1.3,
                    1.6, 1.5, 2.1, 1.1, 1.2, 1.5, 1.0, 1.3]  # NHK
support_ratings4 = [1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2]  # 朝日新聞
support_ratings5 = [1.7, 1.9, 2.3, 1.5, 2.4, 1.9,
                    2.6, 2.4, 1.4, 2.0, 2.1, 2.8, 1.7, 1.9]  # ANN
support_ratings6 = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3]  # 日経・テレ東
support_ratings7 = [0.7, 1.0, 1.2, 1.5, 1.0, 0.6,
                    1.9, 1.3, 1.3, 1.1, 0.6, 1.4, 1.5, 0.8]  # 時事通信
support_ratings8 = [1.1, 1.6, 1.4, 2.2, 1.1, 1.4,
                    0.6, 1.7, 1.4, 2.6, 2.0, 0.8, 2.0, 1.8]  # TBS・JNN
support_ratings9 = [2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1]  # 読売・NNN
support_ratings10 = [1.3, 0.4, 0.7, 1.4, 1.5,
                     1.4, 2.0, 1.2, 1.3, 1.3, 1.8, 2.1, 1.7, 1.5]  # 産経・FNN

average_ratings = []

# Create the graph
ax.plot(times, support_ratings, label="毎日新聞 2023/2/19 4%")
ax.plot(times, support_ratings2, label="共同通信 2023/2/13 3.1%")
ax.plot(times, support_ratings3, label="NHK 2023/2/13 1.3%")
ax.plot(times, support_ratings4, label="朝日新聞 2023/2/21 2%")
ax.plot(times, support_ratings5, label="ANN 2023/2/20 1.9%")
ax.plot(times, support_ratings6, label="日経・テレ東 2023/1/29 3%")
ax.plot(times, support_ratings7, label="時事通信 2023/2/16 0.8%")
ax.plot(times, support_ratings8, label="TBS・JNN 2023/2/6 1.8%")
ax.plot(times, support_ratings9, label="読売・NNN 2023/2/19 1%")
ax.plot(times, support_ratings10, label="産経・FNN 2023/2/20 1.5%")
for i, txt in enumerate(times):
    average = (support_ratings[i] + support_ratings2[i] + support_ratings3[i] + support_ratings4[i] + support_ratings5[i] +
               support_ratings6[i] + support_ratings7[i] + support_ratings8[i] + support_ratings9[i] + support_ratings10[i]) / 10
    average_ratings.append(average)
ax.plot(times, average_ratings, label="各社平均 2023/2/21 2.0%")
ax.set_facecolor((1, 1, 1, 0))
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)

# Add labels and title using Japanese characters
plt.ylabel("政党支持率(%)")
plt.title("国民民主党の政党支持率推移 2022年1月～2023年2月\n（毎日新聞、共同通信、NHK、朝日新聞、ANN、時事通信、日経・テレ東、TBS・JNN、読売・NNN、産経・FNN）\n　",
          loc='left', fontsize=24)

# 各要素にDataFrameのインデックスの数字をラベルとして付ける
for i, txt in enumerate(times):
    print("i：" + str(i) + ", txt：" + txt +
          ", support_ratings[i]：" + str(support_ratings[i]))
    plt.annotate(str(support_ratings[i]), xy=(txt, support_ratings[i]), fontsize=16, color="blue",
                 arrowprops=dict(color="blue"))
    plt.annotate(str(support_ratings2[i]), xy=(txt, support_ratings2[i]), fontsize=16, color="black",
                 arrowprops=dict(color="orange"))
    plt.annotate(str(support_ratings3[i]), xy=(txt, support_ratings3[i]), fontsize=16, color="green",
                 arrowprops=dict(color="green"))
    plt.annotate(str(support_ratings4[i]), xy=(txt, support_ratings4[i]), fontsize=16, color="red",
                 arrowprops=dict(color="red"))
    plt.annotate(str(support_ratings5[i]), xy=(txt, support_ratings5[i]), fontsize=16, color="purple",
                 arrowprops=dict(color="purple"))
    plt.annotate(str(support_ratings6[i]), xy=(txt, support_ratings6[i]), fontsize=16, color="brown",
                 arrowprops=dict(color="brown"))
    plt.annotate(str(support_ratings7[i]), xy=(txt, support_ratings7[i]), fontsize=16, color="pink",
                 arrowprops=dict(color="pink"))
    plt.annotate(str(support_ratings8[i]), xy=(txt, support_ratings8[i]), fontsize=16, color="gray",
                 arrowprops=dict(color="gray"))
    plt.annotate(str(support_ratings9[i]), xy=(txt, support_ratings9[i]), fontsize=16, color="black",
                 arrowprops=dict(color="yellow"))
    plt.annotate(str(support_ratings10[i]), xy=(txt, support_ratings10[i]), fontsize=16, color="lightskyblue",
                 arrowprops=dict(color="lightskyblue"))
    average = (support_ratings[i] + support_ratings2[i] + support_ratings3[i] + support_ratings4[i] + support_ratings5[i] +
               support_ratings6[i] + support_ratings7[i] + support_ratings8[i] + support_ratings9[i] + support_ratings10[i]) / 10
    plt.annotate(str(math.floor(average * 10) / 10), xy=(txt, average), fontsize=16, color="blue",
                 arrowprops=dict(color="blue"))

plt.annotate("第26回参議院選挙", xy=('2022年7月', 4), fontsize=18, color="black",
             arrowprops=dict(width=1, color="black"), xytext=('2022年7月', 5))

plt.grid(True)
plt.tight_layout()
# Show the graph
plt.show()
