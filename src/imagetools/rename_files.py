import os
[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]
