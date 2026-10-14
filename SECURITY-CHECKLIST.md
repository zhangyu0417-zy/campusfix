# 安全审查清单

适用于 CampusFix 项目（含 GitHub Actions CI）。

- [ ] 代码库中无明文密钥：`grep -riE "token|secret|password"` 检查，Secret 只以 `${{ secrets.X }}` 形式引用
- [ ] 提交历史中无敏感信息：`git log --all -p` 抽查，确认 `.env` 从未入库
- [ ] Actions 日志中无 Secret 明文：`使用Secret` 步骤只输出 `token长度=14`，全文搜 `demo-token` 无结果
- [ ] `.gitignore` 覆盖 `.env`、`instance/`、`__pycache__/`、`.venv/`、`.pytest_cache/`
- [ ] 仓库中无个人信息：学号、姓名、密码、Personal Access Token 均不入库
- [ ] 密钥一旦疑似泄露：立即在 Settings → Secrets 中删除并轮换新值

制定日期：2026-10-14
