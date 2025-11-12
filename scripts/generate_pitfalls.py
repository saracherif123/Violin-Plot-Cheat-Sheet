"""
Generate Common Pitfalls Visualization for Violin Plot Cheat Sheet
Shows 8 common pitfalls with visual examples - no axes
Uses only matplotlib and numpy (standard packages)
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# Consistent color scheme - blue and purple shades
COLORS = {
    'error': '#667eea',      # blue
    'warning': '#764ba2',    # purple
    'info': '#3498db',       # bright blue
    'purple': '#9b59b6',     # medium purple
    'median': '#2c3e50',
    'background': '#f8f9fa'
}

plt.style.use('default')
fig, axes = plt.subplots(2, 4, figsize=(20, 10), facecolor='white')

# Pitfall 1: Small Sample Size
np.random.seed(42)
data1 = np.random.normal(0, 1, 15)  # Small sample
ax1 = axes[0, 0]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data1:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax1.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['error'])
ax1.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['error'])
ax1.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['error'])
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
ax1.set_title('Small Sample (n<20)\nUnreliable', fontweight='bold', 
              fontsize=11, color=COLORS['error'], pad=8)
ax1.text(0, -3.5, '', ha='center', fontsize=11, 
         fontweight='bold', color=COLORS['error'])
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.set_facecolor(COLORS['background'])

# Pitfall 2: Wrong Bandwidth (too smooth)
data2 = np.concatenate([np.random.normal(-1, 0.5, 50),
                        np.random.normal(1, 0.5, 50)])
ax2 = axes[0, 1]
# Manual KDE using gaussian smoothing with larger bandwidth (too smooth)
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data2:
    density += np.exp(-0.5 * ((y_kde - val) / 0.6) ** 2)  # Larger bandwidth = smoother
density = density / np.max(density) * 0.2  # Normalize and scale
ax2.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['info'])
ax2.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['info'])
ax2.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['info'])
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
whisker_min = data2_min - 0.8
whisker_max = data2_max + 0.8
whisker_width = 0.05
ax2.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax2.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax2.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax2.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
ax2.set_xlim(-0.5, 0.5)
# Adjust y-limits to show full whiskers - ensure they're fully visible
ax2.set_ylim(whisker_min - 0.3, whisker_max + 0.3)
ax2.set_title('Wrong Bandwidth\nToo smooth - hides features', 
              fontweight='bold', fontsize=11, color='#666', pad=8)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_facecolor(COLORS['background'])

# Pitfall 3: Extends Beyond Data Range
data3 = np.random.normal(0, 1, 100)
ax3 = axes[1, 0]
# Manual KDE using gaussian smoothing
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data3:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2  # Normalize and scale
ax3.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['purple'])
ax3.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['purple'])
ax3.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['purple'])
# Add box plot manually
q1, median, q3 = np.percentile(data3, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax3.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax3.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data3_min = np.min(data3)
data3_max = np.max(data3)
# Extend whiskers visually by 0.5 on each end
whisker_min = data3_min - 0.5
whisker_max = data3_max + 0.5
whisker_width = 0.05
ax3.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax3.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax3.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax3.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
# Show actual data range
actual_min = np.min(data3)
actual_max = np.max(data3)
ax3.axhline(actual_min, color=COLORS['error'], linestyle='--', linewidth=2, alpha=0.7)
ax3.axhline(actual_max, color=COLORS['error'], linestyle='--', linewidth=2, alpha=0.7)
ax3.text(0.4, actual_min - 0.3, 'Actual min', fontsize=9, color=COLORS['error'], fontweight='bold')
ax3.text(0.4, actual_max + 0.3, 'Actual max', fontsize=9, color=COLORS['error'], fontweight='bold')
ax3.set_xlim(-0.5, 0.5)
ax3.set_ylim(-4, 4)
ax3.set_title('Beyond Data Range\nKDE extends', fontweight='bold', 
              fontsize=11, color='#666', pad=8)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.set_facecolor(COLORS['background'])

# Pitfall 4: Too Many Groups
np.random.seed(42)
data4_list = [np.random.normal(i*0.4, 0.4, 30) for i in range(6)]
ax4 = axes[1, 1]
positions = list(range(6))
# Manual KDE for each group
y_kde = np.linspace(-2, 4, 100)
colors_list = ['#667eea', '#764ba2', '#3498db', '#9b59b6', '#5a67d8', '#4facfe']
for i, data4 in enumerate(data4_list):
    density = np.zeros_like(y_kde)
    for val in data4:
        density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
    density = density / np.max(density) * 0.15  # Normalize and scale
    x_pos = positions[i]
    ax4.fill_betweenx(y_kde, x_pos - density, x_pos + density, 
                      alpha=0.6, color=colors_list[i])
    ax4.plot(x_pos - density, y_kde, '-', linewidth=2.5, color=colors_list[i])
    ax4.plot(x_pos + density, y_kde, '-', linewidth=2.5, color=colors_list[i])
    # Add box plot for each violin
    q1, median, q3 = np.percentile(data4, [25, 50, 75])
    iqr_height = q3 - q1
    box_width = 0.03
    ax4.add_patch(plt.Rectangle((x_pos - box_width/2, q1), box_width, iqr_height,
                                facecolor='white', edgecolor='black', linewidth=1.2, zorder=8))
    ax4.plot([x_pos - box_width/2, x_pos + box_width/2], [median, median], 'k-', linewidth=1.2, zorder=8)
    # Add whiskers for each violin
    data4_min = np.min(data4)
    data4_max = np.max(data4)
    whisker_min = data4_min - 0.5
    whisker_max = data4_max + 0.5
    whisker_width = 0.03
    ax4.plot([x_pos, x_pos], [whisker_min, q1], 'k-', linewidth=0.8, zorder=9)
    ax4.plot([x_pos, x_pos], [q3, whisker_max], 'k-', linewidth=0.8, zorder=9)
    ax4.plot([x_pos - whisker_width/2, x_pos + whisker_width/2], [whisker_min, whisker_min],
             'k-', linewidth=1, zorder=10)
    ax4.plot([x_pos - whisker_width/2, x_pos + whisker_width/2], [whisker_max, whisker_max],
             'k-', linewidth=1, zorder=10)
ax4.set_xlim(-0.5, 5.5)
ax4.set_ylim(-2, 4)
ax4.set_title('Too Many Groups\nHard to compare', fontweight='bold', 
              fontsize=11, color='#666', pad=8)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['bottom'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.set_facecolor(COLORS['background'])

# Pitfall 5: Using for Discrete Data
np.random.seed(42)
# Discrete data (e.g., ratings 1-5)
data5 = np.random.choice([1, 2, 3, 4, 5], size=100, p=[0.1, 0.2, 0.3, 0.25, 0.15])
ax5 = axes[0, 2]
# Manual KDE - but this is misleading for discrete data
y_kde = np.linspace(0, 6, 100)
density = np.zeros_like(y_kde)
for val in data5:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2
ax5.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['warning'])
ax5.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['warning'])
ax5.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['warning'])
# No box plot or whiskers for discrete data - that's part of the pitfall
# Show actual discrete values
for val in [1, 2, 3, 4, 5]:
    count = np.sum(data5 == val)
    ax5.scatter([0], [val], s=count*3, color=COLORS['error'], alpha=0.7, zorder=11)
ax5.set_xlim(-0.5, 0.5)
ax5.set_ylim(0, 6)
ax5.set_title('Discrete Data\nMisleading', fontweight='bold', 
              fontsize=11, color='#666', pad=8)
ax5.set_xticks([])
ax5.set_yticks([])
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['bottom'].set_visible(False)
ax5.spines['left'].set_visible(False)
ax5.set_facecolor(COLORS['background'])

# Pitfall 6: Different Scales
np.random.seed(42)
data6a = np.random.normal(0, 1, 100)
data6b = np.random.normal(5, 1, 100)  # Different mean
ax6 = axes[0, 3]
# Two violins with different scales
y_kde = np.linspace(-4, 4, 100)
density_a = np.zeros_like(y_kde)
for val in data6a:
    density_a += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density_a = density_a / np.max(density_a) * 0.15
# Second violin shifted and scaled differently
y_kde_b = np.linspace(1, 9, 100)
density_b = np.zeros_like(y_kde_b)
for val in data6b:
    density_b += np.exp(-0.5 * ((y_kde_b - val) / 0.3) ** 2)
density_b = density_b / np.max(density_b) * 0.15
# Draw first violin at x=-0.2
ax6.fill_betweenx(y_kde, -0.2 - density_a, -0.2 + density_a, 
                  alpha=0.6, color=COLORS['info'])
ax6.plot(-0.2 - density_a, y_kde, '-', linewidth=2.5, color=COLORS['info'])
ax6.plot(-0.2 + density_a, y_kde, '-', linewidth=2.5, color=COLORS['info'])
# Add box plot and whiskers for first violin
q1a, mediana, q3a = np.percentile(data6a, [25, 50, 75])
iqr_height_a = q3a - q1a
box_width = 0.03
ax6.add_patch(plt.Rectangle((-0.2 - box_width/2, q1a), box_width, iqr_height_a,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax6.plot([-0.2 - box_width/2, -0.2 + box_width/2], [mediana, mediana], 'k-', linewidth=1.2)
data6a_min = np.min(data6a)
data6a_max = np.max(data6a)
whisker_min_a = data6a_min - 0.5
whisker_max_a = data6a_max + 0.5
whisker_width = 0.03
ax6.plot([-0.2, -0.2], [whisker_min_a, q1a], 'k-', linewidth=0.8, zorder=9)
ax6.plot([-0.2, -0.2], [q3a, whisker_max_a], 'k-', linewidth=0.8, zorder=9)
ax6.plot([-0.2 - whisker_width/2, -0.2 + whisker_width/2], [whisker_min_a, whisker_min_a],
         'k-', linewidth=1, zorder=10)
ax6.plot([-0.2 - whisker_width/2, -0.2 + whisker_width/2], [whisker_max_a, whisker_max_a],
         'k-', linewidth=1, zorder=10)
# Draw second violin at x=0.2 with different scale
ax6.fill_betweenx(y_kde_b, 0.2 - density_b, 0.2 + density_b, 
                  alpha=0.6, color=COLORS['purple'])
ax6.plot(0.2 - density_b, y_kde_b, '-', linewidth=2.5, color=COLORS['purple'])
ax6.plot(0.2 + density_b, y_kde_b, '-', linewidth=2.5, color=COLORS['purple'])
# Add box plot and whiskers for second violin
q1b, medianb, q3b = np.percentile(data6b, [25, 50, 75])
iqr_height_b = q3b - q1b
ax6.add_patch(plt.Rectangle((0.2 - box_width/2, q1b), box_width, iqr_height_b,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax6.plot([0.2 - box_width/2, 0.2 + box_width/2], [medianb, medianb], 'k-', linewidth=1.2)
data6b_min = np.min(data6b)
data6b_max = np.max(data6b)
whisker_min_b = data6b_min - 0.5
whisker_max_b = data6b_max + 0.5
ax6.plot([0.2, 0.2], [whisker_min_b, q1b], 'k-', linewidth=0.8, zorder=9)
ax6.plot([0.2, 0.2], [q3b, whisker_max_b], 'k-', linewidth=0.8, zorder=9)
ax6.plot([0.2 - whisker_width/2, 0.2 + whisker_width/2], [whisker_min_b, whisker_min_b],
         'k-', linewidth=1, zorder=10)
ax6.plot([0.2 - whisker_width/2, 0.2 + whisker_width/2], [whisker_max_b, whisker_max_b],
         'k-', linewidth=1, zorder=10)
ax6.set_xlim(-0.5, 0.5)
ax6.set_ylim(-4, 9)
ax6.set_title('Different Scales\nInvalid comparison', fontweight='bold', 
              fontsize=11, color='#666', pad=8)
ax6.set_xticks([])
ax6.set_yticks([])
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['bottom'].set_visible(False)
ax6.spines['left'].set_visible(False)
ax6.set_facecolor(COLORS['background'])

# Pitfall 7: Not Showing Individual Points
np.random.seed(42)
data7 = np.random.normal(0, 1, 12)  # Small sample
ax7 = axes[1, 2]
# Manual KDE
y_kde = np.linspace(-4, 4, 100)
density = np.zeros_like(y_kde)
for val in data7:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2
ax7.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['info'])
ax7.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['info'])
ax7.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['info'])
# Add box plot
q1, median, q3 = np.percentile(data7, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax7.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax7.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data7_min = np.min(data7)
data7_max = np.max(data7)
whisker_min = data7_min - 0.5
whisker_max = data7_max + 0.5
whisker_width = 0.05
ax7.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax7.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax7.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax7.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
# SOLUTION: For small samples (n=12 here), individual data points should be overlaid
# Show the actual data points on top of the violin plot
x_jitter = np.random.normal(0, 0.02, len(data7))
ax7.scatter(x_jitter, data7, s=50, color=COLORS['error'], alpha=0.9, 
           zorder=11, edgecolors='white', linewidths=1)
ax7.set_xlim(-0.5, 0.5)
ax7.set_ylim(-4, 4)
ax7.set_title('Smoothed KDE hides real data\nOverlay points for n<30', fontweight='bold', 
              fontsize=11, color=COLORS['error'], pad=8)
ax7.set_xticks([])
ax7.set_yticks([])
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
ax7.spines['bottom'].set_visible(False)
ax7.spines['left'].set_visible(False)
ax7.set_facecolor(COLORS['background'])

# Pitfall 8: Ignoring Outliers
np.random.seed(42)
data8 = np.concatenate([
    np.random.normal(0, 1, 90),
    np.array([-5, -4.5, 4.5, 5])  # Outliers
])
ax8 = axes[1, 3]
# Manual KDE - outliers distort the shape
y_kde = np.linspace(-6, 6, 100)
density = np.zeros_like(y_kde)
for val in data8:
    density += np.exp(-0.5 * ((y_kde - val) / 0.3) ** 2)
density = density / np.max(density) * 0.2
ax8.fill_betweenx(y_kde, -density, density, alpha=0.6, color=COLORS['warning'])
ax8.plot(-density, y_kde, '-', linewidth=2.5, color=COLORS['warning'])
ax8.plot(density, y_kde, '-', linewidth=2.5, color=COLORS['warning'])
# Add box plot
q1, median, q3 = np.percentile(data8, [25, 50, 75])
iqr_height = q3 - q1
box_width = 0.04
ax8.add_patch(plt.Rectangle((-box_width/2, q1), box_width, iqr_height,
                            facecolor='white', edgecolor='black', linewidth=1.2))
ax8.plot([-box_width/2, box_width/2], [median, median], 'k-', linewidth=1.2)
# Add whiskers
data8_min = np.min(data8)
data8_max = np.max(data8)
whisker_min = data8_min - 0.5
whisker_max = data8_max + 0.5
whisker_width = 0.05
ax8.plot([0, 0], [whisker_min, q1], 'k-', linewidth=1, zorder=9)
ax8.plot([0, 0], [q3, whisker_max], 'k-', linewidth=1, zorder=9)
ax8.plot([-whisker_width/2, whisker_width/2], [whisker_min, whisker_min],
         'k-', linewidth=1.2, zorder=10)
ax8.plot([-whisker_width/2, whisker_width/2], [whisker_max, whisker_max],
         'k-', linewidth=1.2, zorder=10)
# Show outliers
outliers = data8[np.abs(data8) > 3]
ax8.scatter([0]*len(outliers), outliers, s=50, color=COLORS['error'], 
           marker='x', linewidths=2, zorder=11, label='Outliers')
ax8.set_xlim(-0.5, 0.5)
ax8.set_ylim(-6, 6)
ax8.set_title('Ignoring Outliers\nDistorts shape', fontweight='bold', 
              fontsize=11, color='#666', pad=8)
ax8.set_xticks([])
ax8.set_yticks([])
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)
ax8.spines['bottom'].set_visible(False)
ax8.spines['left'].set_visible(False)
ax8.set_facecolor(COLORS['background'])

# Adjust spacing so titles and violins fit perfectly
plt.subplots_adjust(
    left=0.03,    # more space on left
    right=0.97,   # more space on right
    top=0.92,     # space for the title
    bottom=0.05,  # space for tails or skewed plots
    wspace=0.15,  # horizontal spacing
    hspace=0.25   # vertical spacing
)

# Get output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

# Save without tight layout cropping issues
output_path = os.path.join(output_dir, 'pitfalls_visualization.png')
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches=None,        # Avoid automatic cropping
    facecolor='white',
    edgecolor='none'
)

print(f"✓ Pitfalls visualization saved as '{output_path}'")
plt.close()
