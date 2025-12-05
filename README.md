# Invaders
Space Invaders written in Python, as part of the Introduction to Programming module.

# Prerequisites
Having Python Installed

# Set Up Instructions

Open CMD

clone:
```Bash
git clone "https://github.com/drak-o/Invaders.git"
```

move to current Invaders Directory:
```Bash
cd Invaders
```

Create a virtual environment:
```Bash
python -m venv .venv
```

Activate the virtual environment:
```Bash
./.venv/Scripts/activate
```

Install required packages:
```Bash
pip install -r requirements.txt
```

# Set up Instructions on university computer

Open CMD

clone:
```Bash
git clone "https://github.com/drak-o/Invaders.git"
```

move to current Invaders Directory:
```Bash
cd Invaders
```

Install required packages:
```Bash
pip install -r requirements.txt
```

Run main.py:
```Bash
python.exe main.py
```

# Image addition to media

To fix the warning (which was causing performance issues):
```bash
libpng warning: iCCP: known incorrect sRGB profile
```

Install [magick](https://imagemagick.org/script/download.php#windows)

run the following command inside the media folder:
```bash
foreach ($f in Get-ChildItem *.png) {
    magick $f.FullName -strip $f.FullName
}
```