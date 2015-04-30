#!/bin/bash          

cd ~/cs390/CS390PYTHON/

git fetch --all
git reset --hard origin/master
chmod -R +x apache/
#apache/bin/apachectl restart

echo "--update complete--"