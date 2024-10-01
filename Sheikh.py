import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import py
