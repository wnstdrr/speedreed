MAN_PATH="/usr/local/man/man1"
MAN_PAGE="$MAN_PATH/speedreed.1"
BINARY="/usr/bin/speedreed"

# copy executable to users /usr/bin
echo "Creating copy of binary 'speedreed' in /usr/bin"

if [ -e $BINARY ]
then
    read -p "'$BINARY' already exists, do you wish to replace it? (y or n)? " -n 1 -r
    echo -e "\n"
    if [[ ! $REPLY =~ ^[Nn]$ ]]
        then
	    sudo cp "speedreed" /usr/bin
    fi
fi

# check if '/usr/local/man1' exists, if not mkdir $MAN_PATH
if [ -d $MAN_PATH ]
then
    echo -e "'$MAN_PATH' already exists, skipping\n"
else
    sudo mkdir $MAN_PATH
fi

# copy and compress
sudo cp "manpage/speedreed.1" $MAN_PATH
sudo gzip $MAN_PAGE
sudo cp "manpage/speedreed.1" $MAN_PATH

# Update the database with the new page
sudo mandb
