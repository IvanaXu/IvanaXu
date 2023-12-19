
cd /Users/ivan/PycharmProjects/IvanaXu

git pull

/Users/ivan/opt/anaconda3/bin/python update.py;echo;

git add *;echo;
git commit -m "Update $(date "+%Y%m%d%H%M%S"|md5sum)";echo;
git push;
