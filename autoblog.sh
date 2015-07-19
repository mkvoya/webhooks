#!/bin/sh

cd ~/blogs;
git pull;
jekyll build;
echo 'done';
