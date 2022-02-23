import subprocess
from datetime import datetime
import os
from os.path import exists

main_file = "main.tex"
build_lang = "build_lang.tex"
temp_file_prefix = "CV_TEMP"
temp_file_sv = f"{temp_file_prefix}_SV"
temp_file_en = f"{temp_file_prefix}_EN"
date = datetime.now().date()

# FORK - REQUIRED - Change this to the correct path
output_dir = "C:\AltaCV\snapshots"

# FORK: - OPTIONAL - Change this date format if you would like
date_f = f"{date:%Y-%m-%d}"

# FORK: - REQUIRED - Change this to the file name you would like
output_name = f"John_Doe_Resume_{date_f}"

def build(name):
    subprocess.run([
    "latexmk", 
    "-shell-escape", 
    "-synctex=1", 
    "-interaction=nonstopmode", 
    "-file-line-error", 
    "-pdf",
    f"-outdir={output_dir}",
    f"-jobname={name}",
    main_file])

def build_prep(lang):
    if not (lang == "EN" or lang == "SV"):
        raise Exception("Incorrect language parameter in build_prep")

    f = open(build_lang, "w")
    if lang == "EN":
        f.write("\entrue")
    elif lang == "SV":
        f.write("\svtrue")

def rename_files():
    temp_en_file = os.path.join(output_dir, f"{temp_file_en}.pdf")
    temp_sv_file = os.path.join(output_dir, f"{temp_file_sv}.pdf")

    if exists(temp_en_file):
        print("Temp EN file found, renaming...")
        os.rename(temp_en_file, os.path.join(output_dir, f"{output_name}_EN.pdf"))

    if exists(temp_sv_file):
        print("Temp SV file found, renaming...")
        os.rename(temp_sv_file, os.path.join(output_dir, f"{output_name}_SV.pdf"))

# Main program
build_prep("SV")
build(temp_file_sv)
build_prep("EN")
build(temp_file_en)
rename_files()