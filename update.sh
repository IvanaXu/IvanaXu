# 
python3 update.py;echo;

# 
git add *;echo;
git commit -m "Update $(date "+%Y%m%d%H%M%S")";echo;
git push origin master;echo;
