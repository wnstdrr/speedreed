import sys
from time import sleep
from os.path import exists

__author__ = "xandertedder7@gmail.com"
__version__ = "v1.0"

R_MODE = "r"
ARGUMENTS = ["-h", "--help", "-t", "--time", "-R", "--reverse", "-m", "--margin"]
HELP = """
Usage: speedreed [FILE, -]... [OPTION]...

Concatenate FILE(s), or standard input, to standard output.
With no FILE, or when FILE is -, read standard input. (quickly!)

  -t  --time\tSet delay between chars, (default .01) 
  -m  --margin\tSet margins or rather limit of chars before newline (only works with files currently)
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
        "margin": None,
        "T_SLEEP": .01
}


def SpeedReed(string):
    index = 0

    while index < len(string):
        sys.stdout.write(string[index])
        sys.stdout.flush()
        sleep(defaults["T_SLEEP"])

        index += 1


def SpeedReadSTDIN():
    # read from the standard in
    stdin_c = sys.stdin.read()
    SpeedReed(stdin_c)


def SpeedReedSTDINReverse():
    stdin_c_rev = sys.stdin.read()[::-1]
    SpeedReed(stdin_c_rev)
    sys.stdout.write("\n")


def SpeedReedFile(FP):
    # read from a file with mode r (Read)
    with open(FP, R_MODE) as reed:
        reed = reed.read()

    SpeedReed(reed)


def SpeedReedFileReverse(FP):
    with open(FP, R_MODE) as rev_reed:
        rev_reed = rev_reed.read()[::-1]

    index = 0
    while index < len(rev_reed):
        sys.stdout.write(rev_reed[index])
        sys.stdout.flush()
        sleep(defaults["T_SLEEP"])

        index += 1



def ReedMargin(fp, margin, f=False):
    # end the line early with a newline if length is hit, reset length parameter.
    index = 0
    if f is True:
        with open(fp, R_MODE) as mreed:
            mreed = mreed.read()
    else:
        mreed = sys.stdin.read()

    while index < len(mreed):
        if index % margin == 0:
            sys.stdout.write("\n")

        sys.stdout.write(mreed[index])
        sys.stdout.flush()
        sleep(defaults["T_SLEEP"])
            
        index += 1


def ReedFiles(args, reverse=False, margin=False, stdin_margin=False):
    for ex in args[1::]:
        if exists(ex) == True:
            if reverse:
                SpeedReedFileReverse(ex)
            elif margin:
                if defaults["margin"] == None or defaults["margin"] == 0:
                    sys.stdout.write("Warning: margin value cannot be None, 0, or greater than the file itself!\n")
                    exit(1)

                else:
                    ReedMargin(ex, defaults["margin"], f=defaults["FILE"])

            else:
                SpeedReedFile(ex)
        else:
            continue


if __name__ == "__main__":
    try:
        if "-V" in sys.argv or "--version" in sys.argv:
            sys.stdout.write(f"{sys.argv[0]} {__version__} (C) 2021 {__author__}\n")
            exit(0)

        if "-h" in sys.argv or "--help" in sys.argv:
            SpeedReed(HELP)
            exit(0)

        if "-t" in sys.argv:
            try:
                defaults["T_SLEEP"] = float(sys.argv[sys.argv.index("-t")+1])
            except Exception: 
                sys.stdout.write(f"Warning: missing operand for -t, applying default of {defaults['T_SLEEP']}\n\n")
                defaults["T_SLEEP"] = .01

        elif "--time" in sys.argv:
            try:
                defaults["T_SLEEP"] = float(sys.argv[sys.argv.index("--time")+1])
            except Exception:
                sys.stdout.write(f"Warning: missing operand for --time, applying default of {defaults['T_SLEEP']}\n\n")
                defaults["T_SLEEP"] = .01

        
        if len(sys.argv) > 1 and sys.argv[1] not in ARGUMENTS:
            
            if "-R" in sys.argv or "--reverse" in sys.argv:
                defaults["FILE"] = True
                ReedFiles(sys.argv, reverse=True)
            
            if "-m" in sys.argv:
                defaults["FILE"] = True
                try:
                    defaults["margin"] = int(sys.argv[sys.argv.index("-m")+1])
                    ReedFiles(sys.argv, margin=True)
                    exit(0)
                except Exception:
                    sys.stdout.write(f"Warning: missing operand for -m, applying default of {defaults['margin']}\n\n")
                    defaults["margin"] = None

            if "--margin" in sys.argv:
                defaults["FILE"] = True
                try:
                    defaults["margin"] = int(sys.argv[sys.argv.index("--margin")+1])
                    ReedFiles(sys.argv, margin=True)
                    exit(0)
                except Exception:
                    sys.stdout.write(f"Warning: missing operand for --margin, applying default of {defaults['margin']}\n\n")
                    defaults["margin"] = None
                    
            else:
                ReedFiles(sys.argv)
                exit(0)
        else:
            SpeedReadSTDIN()

        if "-R" in sys.argv or "--reverse" in sys.argv:
            SpeedReedSTDINReverse()

    except KeyboardInterrupt as e:
        print(str(e)+"\n")
