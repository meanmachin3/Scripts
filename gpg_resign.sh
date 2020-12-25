#!/bin/sh

cd $1

git filter-branch --commit-filter '

if [ "$GIT_COMMITTER_EMAIL" = "your@email.com" ]
then
git commit-tree -S "$@";
fi

' -- --all

git push origin master --force
