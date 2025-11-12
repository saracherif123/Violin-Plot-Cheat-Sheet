"""
Generate Anatomy Visualization for Violin Plot Cheat Sheet
Shows the components of a violin plot with labels - no axes
"""
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle

# Consistent color scheme
COLORS = {
    'violin': '#667eea',
    'violin_dark': '#5a67d8',
    'median': '#e74c3c',
    'iqr': '#2c3e50',
    'text': '#2c3e50',
    'text_light': '#666',
    'density': '#764ba2'
}

fig, ax = plt.subplots(figsize=(12, 7), facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Generate data for violin shape - symmetric and smooth
y = np.linspace(1.2, 4.8, 100)
x_center = 5
# Create symmetric violin shape
width = 0.7 * np.exp(-((y - 3) ** 2) / 0.4)

# Draw violin shape
violin_left = x_center - width
violin_right = x_center + width
ax.fill_betweenx(y, violin_left, violin_right, alpha=0.55, color=COLORS['violin'])
ax.plot(violin_left, y, '-', linewidth=3, color=COLORS['violin_dark'])
ax.plot(violin_right, y, '-', linewidth=3, color=COLORS['violin_dark'])

# Draw IQR box - smaller and properly proportioned
box_width = 0.15  # Much smaller box
iqr_box = Rectangle((5 - box_width/2, 2.2), box_width, 1.6, 
                    facecolor='white', edgecolor='black', linewidth=1.2)
ax.add_patch(iqr_box)

# Median line - thinner, inside box
ax.plot([5 - box_width/2, 5 + box_width/2], [3.0, 3.0], '-', linewidth=2, color='black')

# Whiskers - thin black lines
ax.plot([5, 5], [1.4, 2.2], '-', linewidth=1, color='black')
ax.plot([5, 5], [3.8, 4.6], '-', linewidth=1, color='black')
ax.plot([5 - box_width/3, 5 + box_width/3], [1.4, 1.4], '-', linewidth=1.2, color='black')
ax.plot([5 - box_width/3, 5 + box_width/3], [4.6, 4.6], '-', linewidth=1.2, color='black')

# Annotations with arrows
ax.annotate('Maximum', xy=(5.7, 1.4), xytext=(7.2, 1.2), 
            fontsize=13, fontweight='bold', color=COLORS['text'],
            arrowprops=dict(arrowstyle='->', color=COLORS['violin_dark'], lw=2))
ax.text(7.2, 1.0, '(100th %ile)', fontsize=10, color=COLORS['text_light'])

ax.annotate('Q3', xy=(5.35, 2.2), xytext=(7.2, 2.0),
            fontsize=13, fontweight='bold', color=COLORS['text'],
            arrowprops=dict(arrowstyle='->', color=COLORS['violin_dark'], lw=2))
ax.text(7.2, 1.8, '(75th %ile)', fontsize=10, color=COLORS['text_light'])

ax.annotate('MEDIAN', xy=(5.5, 3.0), xytext=(7.8, 3.0),
            fontsize=15, fontweight='bold', color=COLORS['median'],
            arrowprops=dict(arrowstyle='->', color=COLORS['median'], lw=2.5))
ax.text(7.8, 2.7, '(50th %ile)', fontsize=11, color=COLORS['median'])

ax.annotate('Q1', xy=(5.35, 3.8), xytext=(7.2, 4.0),
            fontsize=13, fontweight='bold', color=COLORS['text'],
            arrowprops=dict(arrowstyle='->', color=COLORS['violin_dark'], lw=2))
ax.text(7.2, 4.2, '(25th %ile)', fontsize=10, color=COLORS['text_light'])

ax.annotate('Minimum', xy=(5.7, 4.6), xytext=(7.2, 4.8),
            fontsize=13, fontweight='bold', color=COLORS['text'],
            arrowprops=dict(arrowstyle='->', color=COLORS['violin_dark'], lw=2))
ax.text(7.2, 5.0, '(0th %ile)', fontsize=10, color=COLORS['text_light'])

# Kernel Density annotation
ax.annotate('Kernel Density', xy=(4.3, 3.0), xytext=(1.2, 3.0),
            fontsize=14, fontweight='bold', color=COLORS['density'],
            arrowprops=dict(arrowstyle='->', color=COLORS['density'], lw=2.5))

# Get output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

plt.tight_layout()
output_path = os.path.join(output_dir, 'anatomy_visualization.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.1)
print(f"✓ Anatomy visualization saved as '{output_path}'")
plt.close()
