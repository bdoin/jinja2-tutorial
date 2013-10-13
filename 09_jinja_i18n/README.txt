
# Creating the message catalog
pybabel extract -F babel.cfg -o locale/messages.pot ./

# Initial creation of the french translation file
pybabel init -d locale -l fr -i locale/messages.pot

# Updating the french catalog (new strings from the message.pot goes
# in the french messages.po. Modified original strings are marked as
# fuzzy
pybabel update -d locale -l fr -i locale/messages.pot

# Compile the resulting po file
pybabel compile -d locale -l fr -i locale/fr/LC_MESSAGES/messages.po

