from pathlib import Path
base = Path.home()
guia = Path("x","XX")
guia2 = guia.with_name("lawaw.txt")
print(base)
print(guia.parent )




guia3 = Path(Path.home(),"Europa")
for txt in Path(guia3).glob("**/*.txt"):
    print(txt)