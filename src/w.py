import re
readmePath="../README.md"
barPath="../progressBar.md"
with open(readmePath, "r",encoding="utf-8") as readme:
    content = readme.read()

with open(barPath, "r",encoding="utf-8") as barmd:
    bar = barmd.read()

newContent = re.sub(r"(?<=<!\-\-START_SECTION:progressBar\-\->)[\s\S]*(?=<!\-\-END_SECTION:progressBar\-\->)", f"\n{bar}\n", content)

with open(readmePath, "w",encoding="utf-8") as readme:
    readme.write(newContent)

