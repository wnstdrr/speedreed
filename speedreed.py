import sys
from time import sleep

__author__ = "xandertedder7@gmail.com"
__version__ = "v1.0"

R_MODE = "r"
ARGUMENTS = ["-h", "--help", "-t", "--time", "-R", "--reverse"]
HELP = """
Usage: speedreed [FILE, -]... [OPTION]...

Concatenate FILE(s), or standard input, to standard output.
With no FILE, or when FILE is -, read standard input. (quickly!)

  -t  --time\tSet delay between chars, (default .01) 
  -R  --reverse\tReverse the given standard input or file contents
  -V  --version\tPrint version and exit
  -h  --help\tShow this help message and exit

Examples:
  fortune | speedreed | lolcat   Read a colorful cookie very quickly! (or slowly)
  speedreed                      Copy standard input to standard output
  ls | speedreed                 Read out files in your system with style
"""


# set defaults for T_SLEEP & FILE
defaults = {
        "FILE": False,
        "T_SLEEP": .01,
}

def SpeedReed(string, T_SLEEP):
    index = 0

    while index < len(string):
        sys.stdout.write(string[index])
        sys.stdout.flush()
        sleep(T_SLEEP)

        index += 1

def SpeedReadSTDIN(T_SLEEP):
    # read from the standard in
    stdin_c = sys.stdin.read()
    SpeedReed(stdin_c, T_SLEEP)

def SpeedReedSTDINReverse(T_SLEEP):
    stdin_c_rev = sys.stdin.read()[::-1]
    SpeedReed(stdin_c_rev, T_SLEEP)
    sys.stdout.write("\n")

def SpeedReedFile(FP, T_SLEEP):
    # read from a file with mode r (Read)
    with open(FP, R_MODE) as reed:
        reed = reed.read()

    SpeedReed(reed, T_SLEEP)

def SpeedReedFileReverse(FP, T_SLEEP):
    with open(FP, R_MODE) as rev_reed:
        rev_reed = rev_reed.read()[::-1]

    index = 0
    while index < len(rev_reed):
        sys.stdout.write(rev_reed[index])
        sys.stdout.flush()
        sleep(T_SLEEP)

        index += 1

if __name__ == "__main__":
    try:
        if "-V" in sys.argv or "--version" in sys.argv:
            sys.stdout.write(f"{sys.argv[0]} {__version__} (C) 2021 {__author__}\n")
            exit(0)

        if "-h" in sys.argv or "--help" in sys.argv:
            SpeedReed(HELP, defaults["T_SLEEP"])
            exit(0)

        if "-t" in sys.argv:
            try:
                defaults["T_SLEEP"] = float(sys.argv[sys.argv.index("-t")+1])
            except Exception: 
                sys.stdout.write(f"Warning: missing operand for -t, applying default {defaults['T_SLEEP']}\n\n")
                defaults["T_SLEEP"] = .01

        elif "--time" in sys.argv:
            try:
                defaults["T_SLEEP"] = float(sys.argv[sys.argv.index("--time")+1])
            except Exception:
                sys.stdout.write(f"Warning: missing operand for --time, applying default {defaults['T_SLEEP']}\n\n")
                defaults["T_SLEEP"] = .01

        
        if len(sys.argv) > 1 and sys.argv[1] not in ARGUMENTS:
            
            if "-R" in sys.argv or "--reverse" in sys.argv:
                defaults["FILE"] = True
                SpeedReedFileReverse(sys.argv[1], defaults["T_SLEEP"])
            else:
                defaults["FILE"] = True
                SpeedReedFile(sys.argv[1], defaults["T_SLEEP"])
    
        else:
            if "-R" in sys.argv or "--reverse" in sys.argv:
                SpeedReedSTDINReverse(defaults["T_SLEEP"])
            else:
                SpeedReadSTDIN(defaults["T_SLEEP"])
    except KeyboardInterrupt as e:
        print(str(e)+"\n")
