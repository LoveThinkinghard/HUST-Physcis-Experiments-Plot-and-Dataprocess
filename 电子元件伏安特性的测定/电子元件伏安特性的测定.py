import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Source Han Serif CN'  # 用来正常显示中文标签, 如果系统中不存在Source Han Sans CN字体，即使设置了也无法正常显示，需要根据系统字体进行设置

voltageRange_10_Ohm=1
milliampRange_10_Ohm=75

voltageRange_1k_Ohm=5
milliampRange_1k_Ohm=7.5

forwardBiasVoltageRange=1
forwardBiasMilliampRange=30
reverseBiasVoltageRange=10
reverseBiasMilliampRange=15

# 输入的电压和电流数据
voltages_10_Ohm = np.array([6.5,16.1,8,67,42.1,59,32,20.8,58,31.1,51.8,40.1,34.6]) /100 *voltageRange_10_Ohm
currents_10_Ohm = np.array([12,30.2,14.5,135.0,83.2,117,61.5,39.5,115,61,101.6,79.1,67.8]) /150 *milliampRange_10_Ohm

voltages_1k_Ohm = np.array([59,75.8,45.1,80.1,44.1,68.3,95,98.3,5,41.1,23.8,47,83.2,34.3]) /100 *voltageRange_1k_Ohm
currents_1k_Ohm = np.array([57,73.8,42.8,77.6,41.7,66.1,92.3,96.2,4.8,38.8,21.5,44.2,81.4,31.9]) /150 *milliampRange_1k_Ohm

forwardBiasVoltages = np.array([8.1,18,35,47.4,63.3,73.8,77.2,78.2,79.2,80,80.3,80.8,81.2,82]) /100 *forwardBiasVoltageRange
forwardBiasCurrents = np.array([0.7,1,1.9,3.1,4.1,10.2,30.1,45.5,61.6,76.8,92,103.9,129.1,147]) /150 *forwardBiasMilliampRange
reverseBiasVoltages = np.array([8.2,20.1,35.1,49,52.6,52.9,53,52.7,53.1,15.2,26.4,42.5,51.6]) /150 *reverseBiasVoltageRange
reverseBiasCurrents = np.array([2,3,4,6,30.9,46.8,137.9,33.8,145.6,1.9,3.7,5.0,9.5]) /150 *reverseBiasMilliampRange

# 使用numpy的polyfit进行最小二乘法拟合，1代表拟合的是一次多项式（线性拟合）
coefficients_10_Ohm= np.polyfit(currents_10_Ohm, voltages_10_Ohm, 1)
coefficients_1k_Ohm= np.polyfit(currents_1k_Ohm, voltages_1k_Ohm, 1)
# 得到拟合的斜率和截距
slope_10_Ohm, intercept_10_Ohm = coefficients_10_Ohm
slope_1k_Ohm, intercept_1k_Ohm = coefficients_1k_Ohm

# 我们将使用numpy的linspace函数来创建这些数组，其中起始值为0，结束值为原始数据的最大值，点数自定

currents_range_10_Ohm = np.linspace(0, currents_10_Ohm.max(), 100)
currents_range_1k_Ohm = np.linspace(0, currents_1k_Ohm.max(), 100)


# 使用拟合系数计算新的电压值，确保拟合线从0开始
fitted_voltages_range_10_Ohm = slope_10_Ohm * currents_range_10_Ohm + intercept_10_Ohm
fitted_voltages_range_1k_Ohm = slope_1k_Ohm * currents_range_1k_Ohm + intercept_1k_Ohm

# 重新绘制图形
plt.figure(1,figsize=(10, 6))
plt.scatter(currents_10_Ohm, voltages_10_Ohm, color='red', label='10欧姆外接法原始数据')
plt.scatter(currents_1k_Ohm, voltages_1k_Ohm, color='blue', label='1000欧姆内接法原始数据')
plt.plot(currents_range_10_Ohm, fitted_voltages_range_10_Ohm, color='red', linestyle='--', label='10欧姆外接法拟合曲线')
plt.plot(currents_range_1k_Ohm, fitted_voltages_range_1k_Ohm, color='blue', linestyle='--', label='1000欧姆内接法拟合曲线')


plt.grid(True,color='gray',linestyle='--',linewidth=0.5)
plt.xlabel('I/mA')
plt.ylabel('U/V')
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.title('线性电阻的伏安特性曲线')
plt.legend()
plt.savefig('线性电阻.png')
plt.show()

reverseBiasVoltages = -reverseBiasVoltages
reverseBiasCurrents = -reverseBiasCurrents

# 合并正向偏置和反向偏置的数据
combinedVoltages = np.concatenate((reverseBiasVoltages, forwardBiasVoltages))
combinedCurrents = np.concatenate((reverseBiasCurrents, forwardBiasCurrents))


# 绘制二极管的伏安特性曲线及其拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(reverseBiasVoltages, reverseBiasCurrents, color='purple', label='二极管反向偏置原始数据')
plt.scatter(forwardBiasVoltages, forwardBiasCurrents, color='green', label='二极管正向偏置原始数据')

plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('U/V')
plt.ylabel('I/mA')
plt.title('二极管的伏安特性曲线')
plt.legend()
plt.savefig('二极管整体拟合.png')
plt.show()
