#! /usr/bin/env bash

pwd
./source/script/export_posts.py -s posts-origin -t source/_posts

npm run server
