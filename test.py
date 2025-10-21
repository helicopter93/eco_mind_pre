import matplotlib.pyplot as plt
import numpy as np

# Данные
years = [2020, 2021, 2022, 2023, 2024, 2025]
x_data = [201.3, 276.8, 361.4, 408.1, 458.4, 451.4]
y_data = [200.64, 201.62, 170.22, 132.68, 70.97, 56.9]

# Создание графика
fig, ax = plt.subplots(figsize=(10, 7))

# Настройка осей
ax.set_xlim(100, 500)
ax.set_ylim(0, 300)
ax.set_xlabel('Вакансии', fontsize=18)
ax.set_ylabel('', fontsize=18)
ax.set_title('2022-2025. Новая экономика', fontsize=20, fontweight='bold', pad=20)

# Добавление текста "Безработные" в левом верхнем углу
ax.text(120, 285, 'Безработные', fontsize=18)

# Настройка сетки
ax.grid(True, color='#e0e0e0', linewidth=1, linestyle='-')
ax.set_axisbelow(True)

# Настройка делений
ax.set_xticks(range(100, 501, 50))
ax.set_yticks(range(0, 301, 50))
ax.tick_params(labelsize=18)

# Биссектриса (черная прямая)
x_bisector = [100, 300]
y_bisector = [100, 300]
ax.plot(x_bisector, y_bisector, 'k-', linewidth=2.5, label='Биссектриса')

# Красная кривая тренда: y = 344920 * x^(-1.356)
x_curve = np.linspace(180, 500, 200)
y_curve = 344920 * np.power(x_curve, -1.356)
ax.plot(x_curve, y_curve, color=(0.863, 0.196, 0.196), linewidth=3, label='Линия тренда')

# Точки данных
ax.scatter(x_data, y_data, s=100, color='steelblue', edgecolors='white', 
           linewidths=2, zorder=5, label='Данные')

# Подписи годов
for i, year in enumerate(years):
    ax.text(x_data[i] + 25, y_data[i] + 5, str(year), 
            fontsize=18, ha='center', va='center')

# Рамка графика
for spine in ax.spines.values():
    spine.set_linewidth(2)
    spine.set_color('black')

# Настройка внешнего вида
plt.tight_layout()

# Показать график
plt.show()