commit_message=`git diff|grep "+###"|awk 'NR==1{print $0}'|tr -d '+#'`

echo ${commit_message}

git add --all
git commit -m "${commit_message}"
git push origin master