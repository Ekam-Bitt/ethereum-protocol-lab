import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_csv(csv_path: str, x: str, y: str, title: str, out_path: str | None = None) -> None:
    """Simple CSV → PNG line plot."""
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(6,4))
    plt.plot(df[x], df[y])
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    os.makedirs(os.path.dirname(out_path or "artifacts/"), exist_ok=True)
    out = out_path or csv_path.replace(".csv", ".png")
    plt.savefig(out, bbox_inches="tight")
    plt.close()