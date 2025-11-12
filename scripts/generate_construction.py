"""
Generate Construction Steps Visualization for Violin Plot Cheat Sheet
Shows the 4-step process of creating a violin plot - no axes
Uses only matplotlib and numpy (standard packages)
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# Consistent color scheme
COLORS = {
    'step1': '#667eea',
    'step2': '#764ba2',
    'step3': '#e74c3c',
    'step4': '#2c3e50',
    'median': '#e74c3c',
    'iqr': '#2c3e50',
    'background': '#f8f9fa'
}

plt.style.use('default')
fig, axes = plt.subplots(1, 4, figsize=(16, 5), facecolor='white')

np.random.seed(42)
data = np.random.normal(0, 1, 50)

# Step 1: Raw Data Points
ax1 = axes[0]
ax1.scatter(np.random.uniform(-0.3, 0.3, len(data)), data, 
           s=40, alpha=0.7, color=COLORS['step1'], edgecolors='white', linewidth=0.5)
ax1.set_xlim(-0.5, 0.5)
ax1.set_ylim(-3, 3)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.set_facecolor(COLORS['background'])

# Step 2: Kernel Density (simple KDE using numpy only)
ax2 = axes[1]
# Simple KDE approximation using gaussian smoothing
y_kde = np.linspace(-3, 3, 100)
density = np.zeros_like(y_kde)
for val in data:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax2.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['step2'])
ax2.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['step2'])
ax2.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['step2'])
ax2.set_xlim(-0.5, 0.5)
ax2.set_ylim(-3, 3)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_facecolor(COLORS['background'])

# Step 3: Add Quartiles - Show IQR box inside violin
ax3 = axes[2]
# Use same KDE as step 2 for consistency
y_kde = np.linspace(-3, 3, 100)
density = np.zeros_like(y_kde)
for val in data:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax3.fill_betweenx(y_kde, -density, density, alpha=0.5, color=COLORS['step2'])
ax3.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['step2'])
ax3.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['step2'])
# Draw IQR box manually
q1, median, q3 = np.percentile(data, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax3.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax3.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
ax3.set_xlim(-0.5, 0.5)
ax3.set_ylim(-3, 3)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.set_facecolor(COLORS['background'])

# Step 4: Final Violin - Complete with IQR box and whiskers
ax4 = axes[3]
# Use same KDE as step 2 for consistency
y_kde = np.linspace(-3, 3, 100)
density = np.zeros_like(y_kde)
for val in data:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax4.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['step1'])
ax4.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['step1'])
ax4.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['step1'])
# Draw IQR box manually
q1, median, q3 = np.percentile(data, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax4.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax4.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
iqr = q3 - q1
data_min = np.min(data)
data_max = np.max(data)

# Extend whiskers visually by 0.5 on each end
whisker_min = data_min - 0.5
whisker_max = data_max + 0.5

whisker_width = 0.05
ax4.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax4.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax4.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax4.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)

ax4.set_xlim(-0.5, 0.5)
ax4.set_ylim(-3, 3)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['bottom'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.set_facecolor(COLORS['background'])

# Get output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

plt.tight_layout()
output_path = os.path.join(output_dir, 'construction_visualization.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', pad_inches=0.1)
print(f"✓ Construction visualization saved as '{output_path}'")
plt.close()
