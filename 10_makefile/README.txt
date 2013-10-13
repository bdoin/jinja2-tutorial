
# Creating the message catalog
make extract

# Initial creation of the french translation file
pybabel init -d locale -l fr -i locale/messages.pot

# Updating all the locale catalog (new strings from the message.pot goes
# in the locale messages.po. Modified original strings are marked as
# fuzzy
make update

# Compile the resulting po file and generate the web site
make

