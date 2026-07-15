---
name: csp-svg-fix
description: 修復 SVG 匯入 Clip Studio Paint (CSP) 時壞掉的問題（數字消失、爆版、被裁切、只顯示部分圖形）。當使用者說 SVG import 進 CSP 是壞的、要修 SVG 給 CSP 用、或處理卡牌 SVG 資產匯入問題時使用。Fix SVG files that break when imported into Clip Studio Paint.
---

# 修 SVG 給 CSP 匯入

CSP 的 SVG 匯入器非常保守：只可靠支援「絕對正座標的 `<path>`，樣式直接寫在元素上」。任何超出這個範圍的寫法都可能壞。

## 第一步：診斷 checklist

對目標 SVG 逐項掃描（用 grep 或直接讀檔，小檔案直接讀）：

| 地雷 | 症狀 | 檢查方式 |
|---|---|---|
| `<text>` / `<tspan>` + 字型 | 文字整個消失 | `grep -E '<text|<tspan'` |
| `<symbol>` + `<use>` | 圖案爆版、縮放錯亂 | `grep -E '<symbol|<use'` |
| 負座標元素或負原點 viewBox（如 `viewBox="-1 -1 …"`） | 圖形被裁切、只剩一個反轉圖形 | 看 viewBox 和座標值 |
| `<polygon>` / `<polyline>` / `<rect>` / `<circle>` 等 shape 元素 | 不穩定，可能不顯示 | `grep -E '<polygon|<polyline|<rect|<circle|<ellipse|<line'` |
| 樣式掛在根元素或 `<g>` 靠繼承（fill/stroke/stroke-width） | 顏色、線寬遺失 | 看 `<svg>` 和 `<g>` 上的 presentation attributes |
| `transform` 屬性 | 位置錯亂；注意 CSP 是**先裁切再套 transform**，所以加 translate wrapper 救不了負座標 | `grep 'transform='` |
| `<style>` / CSS class | 樣式遺失 | `grep -E '<style|class='` |

## 第二步：修法階梯（由輕到重）

1. **手寫改**（檔案小、結構簡單時優先）：
   - 座標整體平移到全正值，viewBox 改成 `0 0 w h`
   - shape 元素改寫成絕對座標 `<path d="M … L … Z">`
   - `fill` / `stroke` / `stroke-width` 明確寫在每個 `<path>` 上，不靠繼承
   - 保留原本的 `id` 和 width/height
2. **Inkscape CLI**（結構複雜時）：
   - 文字轉路徑：`inkscape file.svg --actions="select-all;object-to-path" -o out.svg`
   - 展開 `<use>`：`--actions="select-all;object-unlink-clones"`
3. **大絕招 SVG → PDF → SVG**（transform 巢狀複雜、負座標頑固時）：
   - `inkscape in.svg -o mid.pdf && inkscape mid.pdf -o out.svg`
   - Inkscape 輸出 PDF 時會把所有 transform 燒進絕對座標，座標全部變正值

## 第三步：驗證

修完**必須**渲染成 PNG 目視確認，不要等 import 進 CSP 才發現還是壞的：

```bash
rsvg-convert -o out.png fixed.svg        # 有裝的話優先
qlmanage -t -s 320 -o <scratchpad> fixed.svg   # macOS 內建備援
```

用 Read 工具看 PNG，確認：圖形完整、沒被裁切、顏色線條正確。

## 慣例

- 改檔前先 `cp file.svg file.svg.bak` 留備份，修好後告訴使用者備份位置
- 修完回報踩到哪幾顆雷、各做了什麼修正
