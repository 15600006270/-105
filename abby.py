# 人生苦短，为我happy

#查看分支
git branch

#新建分支levi_dev
git branch levi_dev

#合并分支文件
git merge levi_dev

#查看当前分支状态
git status

#提交到缓存区
git add *

#提交到本地仓库
git commit -m 'add'
git commit -m 'abby work'

#切换到分支levi_dev
git checkout levi_dev

#删除分支levi_dev
#(-d 删除已合并的分支 -D 删除未合并分支)
git branch -d levi_dev
