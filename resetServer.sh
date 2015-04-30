#!/bin/bash          


git fetch --all
git reset --hard origin/master
chmod -R +x /apache
apache/bin/apachectl restart

