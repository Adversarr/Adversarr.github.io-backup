# update whole repo and blog to cloud and fetch
hexo clean
hexo d -g
git add .
git commit
git push
git fetch