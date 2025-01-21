import zipfile
import os

num_cards_per_zipfile = 25

old_cwd = os.getcwd()
os.chdir("generated_cards")
try:
    zip_idx: int = 0
    zip_name = f"generated_cards_{zip_idx:03}.zip"
    try:
        os.unlink(zip_name)
    except IOError:
        pass
    zp = zipfile.ZipFile(file=zip_name, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
    file_idx: int = 0
    while True:
        top = f"card_top_{file_idx:03}.png"
        bot = f"card_bot_{file_idx:03}.png"
        if os.path.exists(top) and os.path.exists(bot):
            zp.write(top)
            zp.write(bot)
        else:
            break
        file_idx += 1
        if (file_idx % num_cards_per_zipfile) == 0:
            zp.close()
            zip_idx += 1
            zip_name = f"generated_cards_{zip_idx:03}.zip"
            try:
                os.unlink(zip_name)
            except IOError:
                pass
            zp = zipfile.ZipFile(file=zip_name, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
    zp.close()
finally:
    os.chdir(old_cwd)
