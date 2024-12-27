# Feature Visualization

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A toolkit for visualizing feature (heat)map by Pyradiomics.

[![asciicast](https://asciinema.org/a/covYfKjW6itQieyx4g85cPOdd.svg)](https://asciinema.org/a/covYfKjW6itQieyx4g85cPOdd?t=3)

Pyradiomics is an excellent tool for feature extraction from medical imaging. However, it hasn't been born with built-in visualization tool. In our manuscript, a *segment-based* extraction mothod was involved, thus, a certain amount of features were extracted by volume of interest, each of which holds a single value.

The hidden meaning of these features can be obscure somehow. To settle this matter, we've developed this toolkit to provide intuitive feature heatmaps as image-level explanation. Both metioned *segment-based* method and this *voxel-based* share same strategy *de facto*. 

## Usage

One should have [uv](https://github.com/astral-sh/uv) installed. Then clone the code to your local machine and tell the program you need more help:

```bash
git clone https://github.com/bioinformatist/feature-visualization.git
cd feature-visualization
uv run plot.py --help
```

Three subcommands were provided. They are:

- `list`: List all available feature names according to provided PARAMS file.
- `plot`: Plot the the feature map of MASKed IMAGE.
- `view`: Save the IMAGE and MASK as tiff format named with OUTPUT.

> [!TIP]
> All images will be rendered in `.tiff` format with `300` ppi resolution and `lzw` compressed (suitable for publication use).

Feel easy to [submit a new issue](https://github.com/bioinformatist/feature-visualization/issues/new) if you encounter any problems.

## Credits

This implementation depends heavily on [zhangjingcode/RadiomicsFeatureVisualization](https://github.com/zhangjingcode/RadiomicsFeatureVisualization).