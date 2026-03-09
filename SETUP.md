# 项目设置指南

## 1. 生成 SSH 密钥对

项目已自动生成 SSH 密钥对：
```
~/.ssh/id_rsa       # 私钥（保密）
~/.ssh/id_rsa.pub   # 公钥（需要添加到 GitHub）
```

## 2. 将公钥添加到 GitHub 账号

### 步骤：
1. 登录你的 GitHub 账号
2. 点击右上角头像，选择 "Settings"（设置）
3. 点击左侧菜单中的 "SSH and GPG keys"（SSH 和 GPG 密钥）
4. 点击 "New SSH key"（添加 SSH 密钥）
5. 在 "Title" 字段中输入一个描述性名称（如 "Scrapling-html2text-skill"）
6. 在 "Key" 字段中粘贴以下公钥：

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCY3grofPaZYCzd8kohk5zRp4cYaju3S5MZfLS/bYdIWGLjrpOaoASmwnLegroXCBneio8c/Tdr9wRYapjJ1H+2juBmbYjYrlx3ODOu9GADPISLR2gtlIvTL7eg+4tbLMM22Q/KFqRdMRXtiB+ykWOzgCdWgOOb/nNg0bCT7GIz3bXSI61/d6BlpuTklbouupCB8hZReWt1vAen6dpzCQRqEyMEMXmUAo5myzDyijOlK1YrvfVgQEsd6/kpu1kWMQjEOPOw3UdftQWvuqc2phm7ZaWTAdEnEiqhsMyJ2MCvqq1oc0WEGC7/eGJdxK3t+L1A9z8g+r2FEh1AEiIkBogPYJ/H67VTJBU/eMyxZijX6t2a7LTIlhCQdaP4jRD3jZcc6ypDicrBZPZYiWNPfvELM3ks2/ziupOqky82D6XQNOzZ5CYrYhJPZa8xcPVoo8KCoPShducn6be44YNyqlbsOob4srqYycpRli1syTgaX3OhR+dHY5KCq0anGtFADlHgkiW4MEYH9tu0t46kJEpTlO84tYpLUQPFnyTuLAnaHaKZO5UOzvW+BF4crrvwRHnQbaPoD3LyETCTMR9qhptomJuNiDXChQkzMLyTKDgFiBYcPxKSk81J5cSmqCkCnxlMJVq7OF+f/CFks6w3qkf+t2kOXBy0Axu+gSogpQ2ksw== your_email@example.com
```

7. 点击 "Add SSH key"（添加 SSH 密钥）完成

## 3. 创建 GitHub 仓库

### 步骤：
1. 登录 GitHub 账号
2. 点击页面右上角的 "+" 图标，选择 "New repository"（新建仓库）
3. 输入仓库名称，建议使用 `scrapling-html2text-skill`
4. 选择仓库可见性（公开或私有）
5. 点击 "Create repository"（创建仓库）

## 4. 配置并上传项目

### 在项目根目录执行以下命令：

```bash
# 进入项目根目录
cd /root/.openclaw/workspace/skills/scrapling-html2text-skill

# 初始化 git 仓库（如果尚未初始化）
git init

# 设置远程仓库（请替换为你的仓库地址）
git remote add origin git@github.com:你的用户名/scrapling-html2text-skill.git

# 配置 git 身份信息
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱地址"

# 添加所有文件到暂存区
git add .

# 提交代码
git commit -m "初始提交：Scrapling+html2text 网页内容提取技能"

# 推送到远程仓库
git push -u origin master
```

**注意：** 请将上述命令中的 `你的用户名` 和 `你的邮箱地址` 替换为你的实际信息。

## 5. 验证配置

完成后，你可以在 GitHub 上查看你的仓库是否包含以下内容：
- `SKILL.md` - 技能文档
- `README.md` - 项目说明文档
- `LICENSE` - 许可证文件
- `script/scrapling_fetch.py` - 主程序文件
- `config/config.json` - 配置文件
- `test_skill.py` - 测试脚本

## 6. 常见问题

### 问题 1：Push 失败，提示 "Permission denied (publickey)"

**解决方法：**
- 检查是否已正确添加 SSH 密钥到 GitHub
- 确保使用正确的邮箱地址
- 尝试重新生成 SSH 密钥并重新添加

### 问题 2：Git 命令未找到

**解决方法：**
```bash
# 安装 git（适用于 Debian/Ubuntu）
sudo apt-get update
sudo apt-get install git
```

### 问题 3：远程仓库地址错误

**解决方法：**
```bash
# 查看当前远程仓库
git remote -v

# 删除旧的远程仓库
git remote remove origin

# 添加新的远程仓库
git remote add origin git@github.com:你的用户名/scrapling-html2text-skill.git
```

## 7. 技能使用

项目已包含完整的技能代码和配置文件，可以直接使用。详细使用方法请参考 README.md 文件。