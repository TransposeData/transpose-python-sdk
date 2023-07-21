#!/bin/bash

validate_regex="^.*[a-z]{0,6}: .*$"

# get contents of commit message file
commit_message=$(cat $1)

echo "Validating commit message: $commit_message"
if ! [[ "$commit_message" =~ $validate_regex ]]; then
  echo "Invalid commit message format. The commit message should be in the format:\n\n<type>: <message>\n\nFor more information, read: https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/"
  exit 1
fi

exit 0
