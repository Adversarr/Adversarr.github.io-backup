#! /usr/bin/env bash

pwd
rm -rf source/_posts
./source/script/export_posts.py -s posts-origin -t source/_posts

npm run server
