from pathlib import Path

README = Path("README.md")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
START = "<!-- WALLPAPER GALLERY START -->"
END = "<!-- WALLPAPER GALLERY END -->"

images = sorted(
    p for p in Path(".").iterdir()
    if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
)

rows = [START, "", "| | | |", "|---|---|---|"]

for i in range(0, len(images), 3):
    cells = []
    for image in images[i:i + 3]:
        name = image.name
        cells.append(
            f'<a href="{name}"><img src="{name}" alt="{name}" width="240"></a>'
            f"<br>`{name}`"
        )
    cells.extend([""] * (3 - len(cells)))
    rows.append("| " + " | ".join(cells) + " |")

rows.extend(["", END])
gallery = "\n".join(rows)

text = README.read_text() if README.exists() else "# Wallpapers\n"
if START in text and END in text:
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    text = before.rstrip() + "\n\n" + gallery + after
else:
    text = text.rstrip() + "\n\n" + gallery + "\n"

README.write_text(text)
print(f"Added previews for {len(images)} wallpapers to {README}")
