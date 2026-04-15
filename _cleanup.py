import os, glob
for f in glob.glob(r'c:\Projects\REPORTS\тексти\Celsius\_*'):
    os.remove(f)
    print(f'Removed: {os.path.basename(f)}')
print('Done')
