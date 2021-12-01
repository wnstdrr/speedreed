% speedreed(1) speedreed v1.0
% Xander Tedder (xandertedder7@gmail.com)
% (Copyright) November, 2021

# NAME
speedreed - concatenate files and print on the standard output (quickly, with style)

# SYNOPSIS
**speedreed** [*FILE*]...
**speedreed** [*OPTION*]...

# DESCRIPTION
Concatenate FILE(s), or standard input, to standard output. 

With no FILE, or when FILE is -, read standard input (quickly, with style).


**-t** **--time**	Set delay between chars, (default .01)

**-m** **--margin**	Set margins or rather limit of chars before newline (only works with files currently)

**-R** **--reverse**	Reverse the given standard input or file contents

**-V** **--version**	Print version and exit

**-h** **--help**	Show this help message and exit

# EXAMPLES

**speedreed**
: Await input from standard in

**fortune | speedreed | lolcat**
: Read a colorful cookie very quickly! (or slowly)

**ls | speedreed**
: Read out files in your system with style

# COPYRIGHT
Copyright (C) 2021 Xander Tedder. License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.
