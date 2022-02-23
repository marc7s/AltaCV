## *** IMPORTANT ***
Before running the build script, open it and edit the commented values in the top of the file: `output_dir` and `output_name` are required, `date_f` is optional. Read more about the build script in the following section

## Forked additions
This is a fork of `https://github.com/NicolasOmar/AltaCV` with some additions and changes I wanted.
I have made the following changes:

1. Added dual language support. Use 
```latex
  \en{
    English text
  }
  \sv{
    Svensk text
  }
``` 
to create a translated version of your resume. Then use the build script to create both versions

2. Added a build script `build.py` that outputs both versions of your resume, and adds it to the `/snapshots` folder. Everytime you run the script, two new versions are added to the folder with the date of today, so you can keep track of older versions of your resume.
To run it, install `python` and then run 
```bash 
  py .\build.py
```

3. Updated `\linkedin` command and added `\link` with separate display texts. Both take two parameters - the first is the display text and the second is the link. Use them like this:
```latex
\linkedin{John Doe}{john-doe-123}

\link{Website}{https://website.com}
```

4. Added a new colour for the About Me section

5. Updated the default `\divider` space and added support for optional custom spacing. Use it like this:
```latex
  \divider        % Default spacing
  \divider[3cm]   % Custom spacing
```
