import subprocess
from datetime import datetime
import os
from os.path import exists

main_file = r"main.tex"
build_lang = r"build_lang.tex"
temp_file_prefix = r"CV_TEMP"
temp_file_sv = f"{temp_file_prefix}_SV"
temp_file_en = f"{temp_file_prefix}_EN"
date = datetime.now().date()

# FORK - REQUIRED - Change this to the correct path
output_dir = r"C:\AltaCV\snapshots"

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

def rename_action_overwrite():
    print("Output file already exists, do you wish to overwrite? yes/no")
    while True:
        ans = str(input(">")).lower().strip()
        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"]:
            return False
        print("Unknown answer, enter yes/no")

def get_output_name(file, i):
    file_split = os.path.splitext(file)
    file_name = file_split[0]
    file_ext = file_split[1]
    return f"{file_name}-{i}{file_ext}"

def get_next_free_name_index(file):
    i = 2
    while exists(get_output_name(file, i)):
        i = i + 1
    return i

def rename_files():
    temp_en_file = os.path.join(output_dir, f"{temp_file_en}.pdf")
    temp_sv_file = os.path.join(output_dir, f"{temp_file_sv}.pdf")

    output_en_name = os.path.join(output_dir, f"{output_name}_EN.pdf")
    output_sv_name = os.path.join(output_dir, f"{output_name}_SV.pdf")

    if exists(output_en_name) or exists(output_sv_name):
        overwrite = rename_action_overwrite()
        if overwrite:
            if exists(output_en_name):
                print("Deleting EN file...")
                os.remove(output_en_name)
            if exists(output_sv_name):
                print("Deleting SV file...")
                os.remove(output_sv_name)
        else:
            en_index = get_next_free_name_index(output_en_name)
            sv_index = get_next_free_name_index(output_sv_name)
            index = max(en_index, sv_index)
            output_en_name = get_output_name(output_en_name, index)
            output_sv_name = get_output_name(output_sv_name, index)

    if exists(temp_en_file):
        print("Temp EN file found, renaming...")
        os.rename(temp_en_file, output_en_name)

    if exists(temp_sv_file):
        print("Temp SV file found, renaming...")
        os.rename(temp_sv_file, output_sv_name)

# Main program
build_prep("EN")
build(temp_file_en)
build_prep("SV")
build(temp_file_sv)
rename_files()