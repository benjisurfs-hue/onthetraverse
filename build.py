"""Package the static site for hosting. Run: python3 build.py."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
output = root / 'dist'
output.mkdir(exist_ok=True)
for name in ('index.html', 'styles.css'):
    shutil.copy2(root / name, output / name)
shutil.copytree(root / 'assets', output / 'assets', dirs_exist_ok=True)
