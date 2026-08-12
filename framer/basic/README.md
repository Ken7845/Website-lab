# Framer Basic 阅读索引

`basic` 按职责分成三类。不要默认通读全部文件，先读当前项目 `PROJECT.md`，再按任务路由。

## 强制配套 Checklist

开始 Framer 工作前先阅读 `../checklist.md` 的“强制使用方法”和 Part 路由表。

每完成一个 Section、Component、Variant、图片批次、交互、Breakpoint、Navbar、Footer、Page 或其他明确 Part，必须回到 `../checklist.md`：

```text
查对应部分
→ Targeted readback / Preview
→ Pass / Fix Required / Blocked
→ 自修补
→ 复检
→ 再进入下一个 Part
```

Context 压缩、Session 恢复或长任务续接后必须重新读取对应 Checklist，不依赖开工时的记忆。

```text
framer/basic/
├── README.md
├── standards/   完成标准与命名规范
├── patterns/    Framer 技术结构与交互模式
└── workflows/   开工、执行、审查、连接与恢复流程
```

## Standards：什么才算完成

| 文件 | 用途 |
|---|---|
| `standards/website-baseline.md` | 所有 Framer 网站的最低完成标准 |
| `standards/marketplace-guidelines.md` | Marketplace 商品化与交付附加要求 |
| `standards/layer-naming.md` | Layer、Component、Variant 命名 |

## Patterns：具体使用什么结构

| 文件 | 用途 |
|---|---|
| `patterns/pattern-recipes.md` | 常见需求的默认方案决策表 |
| `patterns/buttons.md` | Button 的 Padding、Fit Content、页面外层 Stack 与 Link 边界 |
| `patterns/navbar-footer.md` | Navbar、Footer、Layout Template |
| `patterns/motion-design.md` | Motion、Hover、Overlay、Lightbox |

## Workflows：怎样低成本执行

| 文件 | 用途 |
|---|---|
| `workflows/build-checklist.md` | 固定建设顺序与三层 Done |
| `workflows/preflight-audit.md` | 报告完成前抓漏 |
| `workflows/token-saving.md` | Targeted read、批量写入、Session 与验证成本 |
| `workflows/image-workflow.md` | 联系表、裁切、上传、Alt 与 reconnect |
| `workflows/agent-connection.md` | 连接 Framer Agent |

## 默认读取组合

### 新建完整网站

1. 当前项目 `PROJECT.md`
2. `standards/website-baseline.md`
3. `workflows/build-checklist.md`
4. `patterns/pattern-recipes.md`
5. 当前功能对应的 Pattern / Workflow

### 新建 Page 或 Section

1. `PROJECT.md` 对应范围
2. `standards/website-baseline.md` 的当前范围 Done
3. `workflows/build-checklist.md`
4. 对应 Pattern

### 小范围修改

1. `workflows/token-saving.md`
2. 相关 Pattern / Workflow

不重复读取无关规范。

### 完成前审查

1. `workflows/preflight-audit.md`
2. 项目实际使用的 Patterns
3. Marketplace 项目追加 `standards/marketplace-guidelines.md`

## 完成报告

只有通过当前范围的 Build Checklist 和 Preflight Audit，才可以报告完成。

报告至少说明：

- Scope：Section / Page / Website。
- 通过的断点。
- 通过的 Preview 路径。
- Missing 或 Blocked 内容。
- 经过说明的 Baseline 例外。

规则的目的不是增加阅读量，而是让 Agent 使用正确默认方案一次完成。
