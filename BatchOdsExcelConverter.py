import pyexcel as p
import glob, os

os.chdir(".")
for file in glob.glob("*.ods"):
    sheet = p.get_sheet(file_name = file)
    sheet.save_as(file + '.xlsx')