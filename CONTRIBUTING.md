# 贡献指南

感谢您对 BuyBuy 项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告 Bug

如果您发现了 bug，请创建一个 issue，并包含以下信息：

1. Bug 的详细描述
2. 重现步骤
3. 期望的行为
4. 实际的行为
5. 您的环境信息（操作系统、Python 版本、Django 版本等）
6. 相关的错误信息或截图

### 提出新功能

如果您有新功能的想法：

1. 先搜索现有的 issues，看看是否已经有人提出
2. 创建一个新的 issue，详细描述您的想法
3. 说明这个功能为什么有用
4. 如果可能，提供实现的建议

### 提交代码

1. **Fork 项目**
   - 点击右上角的 Fork 按钮

2. **克隆到本地**
   ```bash
   git clone https://github.com/your-username/buybuy.git
   cd buybuy
   ```

3. **创建新分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **进行修改**
   - 编写代码
   - 添加必要的测试
   - 确保代码符合 PEP 8 规范

5. **提交更改**
   ```bash
   git add .
   git commit -m "Add: 描述您的更改"
   ```

6. **推送到 GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**
   - 在 GitHub 上创建 PR
   - 详细描述您的更改
   - 引用相关的 issues

## 代码规范

### Python 代码

- 遵循 PEP 8 代码风格
- 使用有意义的变量名和函数名
- 添加适当的注释和文档字符串
- 每个函数应该只做一件事

### 提交信息

使用清晰的提交信息格式：

```
类型: 简短描述（不超过50个字符）

详细描述（如果需要）

相关 issue: #123
```

类型包括：
- `Add`: 添加新功能
- `Fix`: 修复 bug
- `Update`: 更新现有功能
- `Refactor`: 重构代码
- `Docs`: 文档更新
- `Style`: 代码格式调整
- `Test`: 添加或修改测试
- `Chore`: 其他修改

### 测试

- 为新功能编写测试
- 确保所有测试通过
- 运行测试：`python manage.py test`

## 开发环境设置

1. 创建虚拟环境
2. 安装开发依赖
3. 配置数据库
4. 运行迁移
5. 创建测试数据

详细步骤请参考 `setup_guide.md`

## 问题和讨论

- 对于问题和讨论，请使用 GitHub Issues
- 对于实时交流，可以加入我们的社区（如果有）

## 行为准则

- 尊重所有贡献者
- 保持友好和专业
- 欢迎新手
- 接受建设性的批评

## 许可证

提交代码即表示您同意将您的贡献以 MIT 许可证开源。

---

再次感谢您的贡献！🎉

