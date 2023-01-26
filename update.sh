# 
python3 update.py;echo;

# 
git add *;echo;
git commit -m "Update $(date "+%Y%m%d%H%M%S"|md5sum|cut -d '' -f1)";echo;
git push origin master;echo;
