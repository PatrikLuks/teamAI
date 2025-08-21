# Automatická aktualizace dokumentace
from pathlib import Path

README = Path("README.md")
SRC = Path("src")

content = "# Projekt AI Tým\n\n"
content += "## Soubory projektu\n"
for f in sorted(SRC.glob("*.py")):
    content += f"- {f.name}\n"

README.write_text(content, encoding="utf-8")
print("README.md aktualizován")
