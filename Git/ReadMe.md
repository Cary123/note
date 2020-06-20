# <center>Git的基本使用</center>
## [Details](http://www.cnblogs.com/xueweihan/p/5703144.html)

## Git分支
```
1. master: 主分支，主要用来版本发布。
2. develop：日常开发分支，该分支正常保存了开发的最新代码。
3. feature：具体的功能开发分支，只与 develop 分支交互。
4. release：release 分支可以认为是 master 分支的未测试版。比如说某一期的功能全部开发完成，那么就将 develop 分支合并5. release 分支，测试没有问题并且到了发布日期就合并到 master 分支，进行发布。
6. hotfix：线上 bug 修复分支。
```

## 提交
```shell
1. git add .
2. git status
3. git commit -m "comments"
4. git push
```

## 从远成拉取分支
```shell
1. git checkout -b localbranch(Release-1.5) origin/remoteBranch(Release-1.5)
2. git checkout --track origin/Release-1.5
```

## 创建新分支
```shell
1. git checkout Release-1.5
2. git checkout -b Task5001
3. git push origin Task5001 --把Task5001分支提交到远程(origin == https://gitee.com/xxx.git)
```

## 修改内容提交分支
```
1. first commit local change:
- git add .
- git commit -m "comments"
2. git pull origin Task5001--拉取服务器上的代码
```

## 撤销修改
```
1. 撤销本地修改
- git checkout .（本地所有修改的，没有的提交的，都返回到原来的状态，谨慎使用）
- git checkout -- filepathname (放弃指定文件:git checkout -- java/spring/spring-context.md)
- git stash (把所有没有提交的修改暂存到stash里面, 可用git stash pop恢复)

2. 撤销git add的文件
- git reset head spring.md

3. 撤销git commit的文件
- 先 git log 找到比这次提交更前一次提交的commit_id(4a814707ca4f18e8cdf1417cc09b0242da1ae4e2)
- 再 git reset 4a814707ca4f18e8cdf1417cc09b0242da1ae4e2（回退到上一个 提交的节点 代码还是原来你修改的） 
- git reset –hard 4a814707ca4f18e8cdf1417cc09b0242da1ae4e2 （回退到上一个commit节点， 代码也发生了改变，变成上一次的, 慎用）

4. 撤销已经push的代码
- git revert HEAD（撤销前一次 commit ）
- git revert HEAD^ （撤销前前一次 commit）
- git revert commit-id (撤销指定的commit-id版本，撤销也会作为一次提交进行保存） 
```

## 覆盖本地分支
```shell
1. git checkout dev: --切换到dev分支
2. git fetch --all
3. git reset --hard origin/dev --拉取服务器上的代码覆盖本地
```

## 分支操作
```shell
1. 从 develop 分支建一个 feature 分支，并切换到 feature 分支
$ git checkout -b myfeature develop
Switched to a new branch "myfeature"

2. 合并feature 分支到 develop
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff myfeature
Updating ea1b82a..05e9557
(Summary of changes)
$ git branch -d myfeature
Deleted branch myfeature
$ git push origin develop

3. 新建 release 分支
$ git checkout -b release-1.2 develop
Switched to a new branch "release-1.2"
$ ./bump-version.sh 1.2
File modified successfully, version bumped to 1.2.
$ git commit -a -m "Bumped version number to 1.2"
[release-1.2 74d9424] Bumped version number to 1.2
1 files changed, 1 insertions(+), 1 deletions(-)

4. release 分支合并到 master 分支
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2

5. release 分支合并到 develop 分支
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)

6. 删除 release 分支
$ git branch -d release-1.2
Deleted branch release-1.2 (was ff452fe).

7. 新建 hotfix 分支
$ git checkout -b hotfix-1.2.1 master
Switched to a new branch "hotfix-1.2.1"
$ ./bump-version.sh 1.2.1
Files modified successfully, version bumped to 1.2.1.
$ git commit -a -m "Bumped version number to 1.2.1"
[hotfix-1.2.1 41e61bb] Bumped version number to 1.2.1
1 files changed, 1 insertions(+), 1 deletions(-)

8. bug fix 之后，hotfix 合并到 master
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2.1

9. hotfix 合并到 develop 分支
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)

10. 删除 hotfix 分支
$ git branch -d hotfix-1.2.1
Deleted branch hotfix-1.2.1 (was abbe5d6).
```

## Just test

# OK

## 切换分支
```shell
1. git checkout test
2. $ git push --set-upstream origin test --设置默认push分支，否则每次需要制定分支push，pull
```

## 删除分支test
```shell
1. git branch -d test --删除本地分支
2. git branch -r -d origin/test --删除远程分支
3. git push origin --delete test
```

## 合并分支
```shell
1. 想把test分支合并到master分支
2. 先切换到master分支
3. git merge test
3. 冲突合并
4. git mergetool
5. beyond compare
```

## 创建tag并提交
```
git tag -a Release-1.0.0 -m "第一个版本"
git push origin Release-1.0.0
```

## Git全局忽略
```
1.vi ~/.gitignore_global 
在gitignore_global中写入： 
.DS_Store 
*/.DS_Store 
2.vi ~/.gitconfig 
配置.gitconfig 文件如下： 
[user] 
name = xiaoronglv 
email = xxxxx@gmail.com 
[push] 
default = matching 
[core] 
excludesfile = /Users/holy/.gitignore_global 
其中：/Users/holy 可以在命令行输入pwd即可查看。
```

## Git秘钥生成
```
cd ~/.ssh       //检查本机中是否有公钥信息
mkdir key_backup
cp id_rsa*key_backup        
rm id_rsa       //删除已有公钥
"新生成公钥"
ssh-keygen -t rsa -C "git注册账号邮箱"        //回车后会让输入用户名，再回车输入密码，在是确认密码
cat ~/.ssh/id_rsa.pub  //显示刚生成的公钥

/*将公钥添加到本地*/
<windows>
clip < ~/.ssh/id_rsa.pub
<Mac>
pbcopy < ~/.ssh/id_rsa.pub
<Linux>
xclip -sel clip < ~/.ssh/id_rsa.pub
然后在 .ssh文件中的 id_rsa就为公钥
把公钥添加到coding中
然后运行 ssh -T git@git.coding.net 看是否已经联通

## other
```
这个是重点要说的内容，过程比本地回滚要复杂
应用场景：自动部署系统发布后发现问题，需要回滚到某一个commit，再重新发布
原理：先将本地分支退回到某个commit，删除远程分支，再重新push本地分支
操作步骤：
1、git checkout the_branch
2、git pull
3、git branch the_branch_backup //备份一下这个分支当前的情况
4、git reset --hard the_commit_id //把the_branch本地回滚到the_commit_id
5、git push origin :the_branch //删除远程 the_branch
6、git push origin the_branch //用回滚后的本地分支重新建立远程分支
7、git push origin :the_branch_backup //如果前面都成功了，删除这个备份分支
```