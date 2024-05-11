import matplotlib.pyplot as plt
import numpy as np
with open('settings.txt','r') as settings:
    tmp=[float(i) for i in settings.read().split("\n")] #чтение из settings
plt.style.use('default')
data_array=np.loadtxt("data.txt", dtype=int) #чтение из data
data_array=[i*tmp[1] for i in data_array] #перевод в вольты
fig, ax = plt.subplots(figsize=(16,10),dpi=400)
time_array=np.linspace(0,len(data_array)*tmp[0],164)
ax.plot(time_array,data_array, color='#FFA500', linewidth=4, linestyle='-',marker='.',markersize=3,label='U(T)') #настройка линии и маркеров
ax.set_xlabel('Время,c',fontsize=18) #заголовки
ax.set_ylabel('Напряжение,В',fontsize=18)
ax.set_title('Процесс заряда конденсатора в RC-цепочке\nГрафик зависимости\n U(T)', fontsize=20)
ax.text(1.25, 1.176, r'Время заряда = 2.1976 с',fontsize=18)
ax.grid(color='blue',linestyle='--',alpha=0.5) #основная сетка
ax.set_yscale('linear')
ax.tick_params(top=False, labeltop=False, color='#FFA500', axis='x', #настройка штрихов
               labelcolor='#008080')
ax.tick_params(top=False, labeltop=False, color='#FFA500', axis='y',
               labelcolor='#008080')
plt.minorticks_on() #дополнительные штрихи
plt.grid(which='minor', linestyle=':')
ax.set_xticks(np.linspace(0,len(data_array)*tmp[0],5)) #расстановка штрихов
ax.set_yticks(np.linspace(0,2.5,8))
ax.set_xlim(0,2.3) #границы осей
ax.set_ylim(0,2.5)
ax.legend(loc='lower right',fontsize=18) #легенда
fig.savefig("test.png")
