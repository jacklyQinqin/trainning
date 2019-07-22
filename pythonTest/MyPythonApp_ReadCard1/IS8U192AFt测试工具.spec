# -*- mode: python -*-

block_cipher = None


a = Analysis(['IS8U192AFt≤‚ ‘π§æﬂ.py'],
             pathex=['D:\\¡∑œ∞\\python¡∑œ∞\\venv\\Lib\\site-packages\\PySmartCard,D:\\¡∑œ∞\\python¡∑œ∞\\venv\\Lib\\site-packages', 'D:\\¡∑œ∞\\python¡∑œ∞\\–°œÓƒø2∂¡ø®∆˜'],
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
          name='IS8U192AFt≤‚ ‘π§æﬂ',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
