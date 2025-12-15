import sys
import subprocess
import tempfile

KEYWORDS = {
    "եթե": "if",
    "այլապես": "else",
    "տպել": "print",
    "մինչ": "while",
    "ճշմարիտ": "True",
    "կեղծ": "False",
}

TYPES = [
    "ամբողջ",
    "տող",
    "բուլյան",
]

def translate(code: str) -> str:
    # Remove type keywords
    for t in TYPES:
        code = code.replace(t + " ", "")

    # Replace Armenian keywords
    for arm, py in KEYWORDS.items():
        code = code.replace(arm, py)

    return code

def run_arm_file(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        arm_code = f.read()

    py_code = translate(arm_code)

    with tempfile.NamedTemporaryFile(
        suffix=".py",
        mode="w",
        encoding="utf-8",
        delete=False
    ) as temp:
        temp.write(py_code)
        temp_filename = temp.name

    subprocess.run(["python", temp_filename])

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".arm"):
        print("Օգտագործում: python arm.py ֆայլ.arm")
        sys.exit(1)

    run_arm_file(sys.argv[1])
