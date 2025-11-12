"""
Generate Visual Patterns Visualization for Violin Plot Cheat Sheet
Shows 6 different distribution patterns in a 3x2 grid - no axes
Uses only matplotlib and numpy (standard packages)
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# Consistent color scheme - blue and purple shades
COLORS = {
    'unimodal': '#667eea',      # blue
    'bimodal': '#764ba2',        # purple
    'skewed': '#9b59b6',         # medium purple
    'heavy_tails': '#3498db',    # bright blue
    'multimodal': '#5a67d8',     # dark blue
    'uniform': '#4facfe',        # light blue
    'median': '#2c3e50',
    'background': '#f8f9fa'
}

plt.style.use('default')
fig, axes = plt.subplots(3, 2, figsize=(10, 12), facecolor='white')

# Unimodal - Normal distribution
np.random.seed(42)
data1 = np.random.normal(0, 1, 200)
ax1 = axes[0, 0]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data1:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax1.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['unimodal'])
ax1.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['unimodal'])
ax1.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['unimodal'])
# Add box plot manually
q1, median, q3 = np.percentile(data1, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax1.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax1.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data1_min = np.min(data1)
data1_max = np.max(data1)
# Extend whiskers visually by 0.5 on each end
whisker_min = data1_min - 0.5
whisker_max = data1_max + 0.5
whisker_width = 0.05
ax1.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax1.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax1.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax1.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax1.set_xlim(-0.5, 0.5)
ax1.set_ylim(-4, 4)
ax1.set_title('UNIMODAL\nSingle peak', fontweight='bold', fontsize=13, 
              color='#2c3e50', pad=10)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.set_facecolor(COLORS['background'])

# Bimodal - Two normal distributions
data2 = np.concatenate([np.random.normal(-1.5, 0.6, 100), 
                        np.random.normal(1.5, 0.6, 100)])
ax2 = axes[0, 1]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data2:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax2.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['bimodal'])
ax2.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['bimodal'])
ax2.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['bimodal'])
# Add box plot manually
q1, median, q3 = np.percentile(data2, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax2.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax2.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data2_min = np.min(data2)
data2_max = np.max(data2)
# Extend whiskers visually by 0.5 on each end
whisker_min = data2_min - 0.5
whisker_max = data2_max + 0.5
whisker_width = 0.05
ax2.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax2.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax2.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax2.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax2.set_xlim(-0.5, 0.5)
ax2.set_ylim(-4, 4)
ax2.set_title('BIMODAL\nTwo peaks', fontweight='bold', fontsize=13,
              color='#2c3e50', pad=10)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_facecolor(COLORS['background'])

# Skewed - Right skewed distribution (very pronounced, clearly asymmetric)
np.random.seed(42)
# Use log-normal distribution for very clear right skew
data3 = np.random.lognormal(mean=0.5, sigma=0.8, size=200)
ax3 = axes[1, 0]
# Manual KDE using gaussian smoothing
data3_min, data3_max = np.min(data3), np.max(data3)
# Use full data range for KDE, not capped
y_kde = np.linspace(max(0, data3_min - 0.5), data3_max + 0.5, 100)
density = np.zeros_like(y_kde)
for val in data3:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax3.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['skewed'])
ax3.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['skewed'])
ax3.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['skewed'])
# Add box plot manually
q1, median, q3 = np.percentile(data3, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax3.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax3.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
# Extend whiskers visually by 0.5 on each end
whisker_min = max(0, data3_min - 0.5)  # Don't go below 0 for log-normal
whisker_max = data3_max + 0.5
whisker_width = 0.05
ax3.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax3.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax3.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax3.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax3.set_xlim(-0.5, 0.5)
# Set y-limits to show full distribution including extended whiskers
ax3.set_ylim(max(0, whisker_min - 0.2), whisker_max + 0.2)
ax3.set_title('SKEWED\nAsymmetric', fontweight='bold', fontsize=13,
              color='#2c3e50', pad=10)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.set_facecolor(COLORS['background'])

# Heavy Tails - Wide distribution
data4 = np.random.standard_t(3, 200)
ax4 = axes[1, 1]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-6, 6, 100)
density = np.zeros_like(y_kde)
for val in data4:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax4.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['heavy_tails'])
ax4.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['heavy_tails'])
ax4.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['heavy_tails'])
# Add box plot manually
q1, median, q3 = np.percentile(data4, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax4.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax4.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data4_min = np.min(data4)
data4_max = np.max(data4)
# Extend whiskers visually by 0.5 on each end
whisker_min = data4_min - 0.5
whisker_max = data4_max + 0.5
whisker_width = 0.05
ax4.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax4.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax4.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax4.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax4.set_xlim(-0.5, 0.5)
ax4.set_ylim(-6, 6)
ax4.set_title('HEAVY TAILS\nWide spread', fontweight='bold', fontsize=13,
              color='#2c3e50', pad=10)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['bottom'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.set_facecolor(COLORS['background'])

# Multimodal - More than two peaks
np.random.seed(42)
data5 = np.concatenate([
    np.random.normal(-2, 0.5, 70),
    np.random.normal(0, 0.5, 70),
    np.random.normal(2, 0.5, 60)
])
ax5 = axes[2, 0]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data5:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax5.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['multimodal'])
ax5.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['multimodal'])
ax5.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['multimodal'])
# Add box plot manually
q1, median, q3 = np.percentile(data5, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax5.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax5.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data5_min = np.min(data5)
data5_max = np.max(data5)
whisker_min = data5_min - 0.5
whisker_max = data5_max + 0.5
whisker_width = 0.05
ax5.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax5.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax5.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax5.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax5.set_xlim(-0.5, 0.5)
ax5.set_ylim(-4, 4)
ax5.set_title('MULTIMODAL\nSeveral subgroups', fontweight='bold', fontsize=13,
              color='#2c3e50', pad=10)
ax5.set_xticks([])
ax5.set_yticks([])
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['bottom'].set_visible(False)
ax5.spines['left'].set_visible(False)
ax5.set_facecolor(COLORS['background'])

# Uniform/Flat - Even density across values
np.random.seed(42)
data6 = np.random.uniform(-3, 3, 200)
ax6 = axes[2, 1]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-3.5, 3.5, 100)
density = np.zeros_like(y_kde)
for val in data6:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax6.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['uniform'])
ax6.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['uniform'])
ax6.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['uniform'])
# Add box plot manually
q1, median, q3 = np.percentile(data6, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax6.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax6.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data6_min = np.min(data6)
data6_max = np.max(data6)
whisker_min = data6_min - 0.5
whisker_max = data6_max + 0.5
whisker_width = 0.05
ax6.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax6.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax6.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax6.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax6.set_xlim(-0.5, 0.5)
ax6.set_ylim(-3.5, 3.5)
ax6.set_title('UNIFORM/FLAT\nNo central tendency', fontweight='bold', fontsize=13,
              color='#2c3e50', pad=10)
ax6.set_xticks([])
ax6.set_yticks([])
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['bottom'].set_visible(False)
ax6.spines['left'].set_visible(False)
ax6.set_facecolor(COLORS['background'])

# Adjust spacing so titles and violins fit perfectly
plt.subplots_adjust(
    left=0.07,    # more space on left
    right=0.93,   # more space on right
    top=0.95,     # space for the title
    bottom=0.05,  # space for tails or skewed plots
    wspace=0.25,  # horizontal spacing
    hspace=0.30   # vertical spacing
)

# Get output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

# Save without tight layout cropping issues
output_path = os.path.join(output_dir, 'patterns_visualization.png')
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches=None,        # Avoid automatic cropping
    facecolor='white',
    edgecolor='none'
)

print(f"✓ Patterns visualization saved as '{output_path}'")
plt.close()
