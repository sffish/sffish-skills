# sffish-skills

可分享的 [Claude Code](https://claude.com/claude-code) skills 集。

A collection of shareable skills for Claude Code (agent skills).

## 安裝 / Install

把想用的 skill 目錄複製（或 symlink）到 `~/.claude/skills/`：

```bash
git clone https://github.com/sffish/sffish-skills.git
ln -s "$(pwd)/sffish-skills/csp-svg-fix" ~/.claude/skills/csp-svg-fix
```

也可以放進專案層級的 `.claude/skills/`，只在該專案生效。

## Skills

| Skill | 說明 |
|---|---|
| [csp-svg-fix](csp-svg-fix/SKILL.md) | 修復 SVG 匯入 Clip Studio Paint (CSP) 時壞掉的問題：診斷 checklist（text、use/symbol、負座標、shape 元素、繼承樣式、transform）、修法階梯（手寫改 → Inkscape CLI → SVG→PDF→SVG 燒絕對座標）、渲染驗證 |

## Skill 格式

每個 skill 是一個目錄，內含 `SKILL.md`，用 YAML frontmatter 宣告 `name` 和 `description`（description 裡埋觸發詞，Claude Code 據此決定何時自動載入）。詳見[官方文件](https://code.claude.com/docs/en/skills)。

## License

MIT
