# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\cchorseless\\Documents\\GitHub\\untitled3\\untitled88.py'],
             pathex=['C:\\Users\\cchorseless\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\cchorseless\\Documents\\GitHub\\untitled3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='untitled88',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
