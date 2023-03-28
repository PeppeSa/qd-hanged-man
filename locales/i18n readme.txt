### FOLDER PATHS VARY AS THE DEVELOPMENT ENVIRONMENT CHANGES! ###

# create .pot files with:
cd {project_folder}
python {anaconda_folder}\Tools\i18n\pygettext.py -d base -o .\locales\base.pot .\src\classModules\impiccato.py

# copy base.pot into both {project_folder}\locales\{lang}\LC_MESSAGES and rename it as base.po
# add the translations to the desired .po files
# then build .mo files starting from .po files
cd {project_folder}\locales\{lang}\LC_MESSAGES
python {anaconda_folder}\Tools\i18n\msgfmt.py -o base.mo base