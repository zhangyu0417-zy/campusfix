# AI工程日志

## 记录1（日期：2026-10-19，实验：第1次 · 课程导论与环境体检）

- **我原来的目标**：完成个人开发环境体检，确认 Git / Python / pip / VS Code / SSH / curl 是否可用，并建立 AI 工程日志。
- **我提供给AI的信息（已脱敏）**：各命令的版本号输出（系统版本、Git、Python、pip、VS Code、SSH、curl）。未提供任何密码、Token、私钥、服务器地址。
- **提示词摘要**：①怎么一次性收集六个工具的环境信息；②`code --version` 输出的三行分别是什么；③课1 的证据该怎么打包提交。
- **AI建议摘要**：建议逐项运行 `git --version`、`python --version`、`python -m pip --version`、`code --version`、`ssh -V`、`curl --version` 并记录版本号；指出 `code --version` 三行依次是 VS Code 版本、commit、架构。
- **我采纳/拒绝的部分及理由**：采纳"逐项记录版本号"（体检表需要具体版本才能核对）；采纳"用一条组合命令一次性收集"，避免逐条敲错命令。
- **我实际执行的操作**：在 PowerShell 中运行一条组合命令，依次检查系统版本与六个工具的版本。
- **验证命令/结果**：Git 2.55.0.windows.5；Python 3.14.7；pip 26.2.1；VS Code 1.141.1 (x64)；OpenSSH_for_Windows 9.5p1；curl 8.10.1 —— 六项全部"通过"。
- **我现在能独立解释的内容**：`git --version` 查 Git 客户端版本（管代码）；`python --version` 查解释器版本（跑应用与测试）；`pip` 是 Python 包管理器；`ssh` 用于远程登录服务器；`curl` 用于命令行发 HTTP 请求（后面用它验证 /health 接口）。

---

> 脱敏规则：服务器 IP 写作 <SERVER_IP>，用户名写作 <USER>，Token 写作 <TOKEN_REDACTED>，私钥绝不粘贴。
