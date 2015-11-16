import os
[os.rename(f, f.replace('-00', '-')) for f in os.listdir('.') if not f.startswith('.')]
