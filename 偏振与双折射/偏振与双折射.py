# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#%%
# 做出 I-cos^2(Θ) 曲线，验证马吕斯定律

# 生成 x 轴数据，即 cos^2(Θ)，Θ = [90, 80, 70, ,,, ,0]
x = np.cos(np.radians(np.arange(90, -1, -10)))**2

# 输入 y 轴的数据，即 I，包括右旋（Ⅰ）和左旋（Ⅱ）两组数据
y = [[4.19, 11.27, 24.0, 69.4, 114.7, 164.3, 214, 251, 276, 285],
     [4.50, 15.76, 41.8, 80.0, 127.7, 175.3, 224, 258, 280, 285]]

# 开始绘图
fig1, ax1 = plt.subplots()
ax1.scatter(x, y[0], marker='x')  # 在图上标点
ax1.scatter(x, y[1], marker='+')
ax1.plot(x, y[0], '-', x, y[1], '--')
ax1.set(xlabel='cos^2(Θ)', ylabel='I (*e-07 A)', title='I - cos^2(Θ)')
ax1.grid()

fig1.savefig('I-cos^2(Θ) 曲线')
plt.show()

#%%
# 生成极角 theta = [0, 10, 20, ,,, , 350]
x2 = np.radians(np.arange(0, 351, 10))

# 输入极径
y2 = [53.5, 46.8, 44.1, 45.2, 51.0, 58.4, 68.6, 82.1, 92.8,
     100.4, 105.5, 109.1, 109.9, 107.5, 97.4, 83.2, 75.0, 63.4,
     53.0, 47.4, 43.4, 45.2, 49.9, 57.9, 69.4, 80.4, 90.4,
     98.3, 105.6, 109.1, 108.7, 101.1, 94.7, 87.1, 73.1, 62.5]

ax2 = plt.subplot(111, projection='polar')
ax2.plot(x2, y2, 'x', x2, y2, '--')
ax2.grid(True)

plt.savefig('I-θ on polor axis')
plt.show()
