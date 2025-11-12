"""
Generate all visualizations for Violin Plot Cheat Sheet
Run this script to generate all 4 visualizations at once
"""
import subprocess
import sys
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (project root)
project_root = os.path.dirname(script_dir)
# Set output directory
output_dir = os.path.join(project_root, 'output')

scripts = [
    'generate_anatomy.py',
    'generate_patterns.py',
    'generate_pitfalls.py',
    'generate_construction.py'
]

print("Generating all visualizations...\n")

for script in scripts:
    script_path = os.path.join(script_dir, script)
    print(f"Running {script}...")
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True,
                              cwd=script_dir)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}:")
        print(e.stderr)
    print()

print("All visualizations generated!")
print(f"\nGenerated files in '{output_dir}':")
print("  - anatomy_visualization.png")
print("  - patterns_visualization.png")
print("  - pitfalls_visualization.png")
print("  - construction_visualization.png")

