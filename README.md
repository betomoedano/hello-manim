# Hello Manim

A minimal [Manim Community](https://www.manim.community/) project that draws a pink circle.

## Setup

Install the macOS system dependencies:

```bash
brew install cairo pkg-config
```

Install the Python dependencies:

```bash
uv sync
```

Confirm that Manim is ready:

```bash
uv run manim checkhealth
```

## Render the animation

```bash
uv run manim -pql src/hello_manim/__init__.py CreateCircle
```

The `-p` option opens the video when rendering finishes, and `-ql` uses low quality for a fast preview. Generated files are saved in the `media` directory.
