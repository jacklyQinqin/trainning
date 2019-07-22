# -*- mode: python -*-

block_cipher = None


a = Analysis(['1503BootLoader图形界面的SPI指令转换工具.py', '工具.exe'],
             pathex=['C:\\Users\\Administrator.USER-20190321CH\\python练习\\小项目'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='1503BootLoader图形界面的SPI指令转换工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
