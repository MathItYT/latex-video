from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd


func: Callable[[np.ndarray], np.ndarray] = lambda x: np.exp(x)


def to_csv(x: np.ndarray, path: Path) -> None:
    y = func(x)
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv(path, index=False)


def func1_to_csv() -> None:
    folder = Path('csv')
    folder.mkdir(exist_ok=True)
    paths = [folder / f'output{i}.csv' for i in range(120)]
    for i, path in enumerate(paths):
        if path.exists():
            continue
        x = np.linspace(0, 5, 120)[:i+1]
        to_csv(x, path)
        print(f'Saved {path}')
    print('Done')


def main() -> None:
    func1_to_csv()


if __name__ == '__main__':
    main()
