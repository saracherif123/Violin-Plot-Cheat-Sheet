# Violin Plot Cheat Sheet

## Project Structure

```
.
├── scripts/                    # Python scripts for generating visualizations
│   ├── generate_all_visuals.py # Run all visualizations at once
│   ├── generate_anatomy.py     # Generate anatomy visualization
│   ├── generate_construction.py # Generate construction steps visualization
│   ├── generate_patterns.py    # Generate visual patterns visualization
│   └── generate_pitfalls.py    # Generate pitfalls visualization
├── output/                     # Generated visualization images (PNG files)
├── violin_plot_cheatsheet.html # Final cheat sheet HTML file
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Generating Visualizations

To generate all visualizations:
```bash
python scripts/generate_all_visuals.py
```

Or generate individual visualizations:
```bash
python scripts/generate_anatomy.py
python scripts/generate_construction.py
python scripts/generate_patterns.py
python scripts/generate_pitfalls.py
```

All generated images will be saved in the `output/` directory.

