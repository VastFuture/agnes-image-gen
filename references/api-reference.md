# Agnes Image 2.1 Flash API Reference

## 目录

1. [端点与认证](#1-端点与认证)
2. [请求参数](#2-请求参数)
3. [尺寸与宽高比](#3-尺寸与宽高比)
4. [响应格式](#4-响应格式)
5. [常见错误](#5-常见错误)

## 1. 端点与认证

- **端点**: `POST https://apihub.agnes-ai.com/v1/images/generations`
- **认证**: `Authorization: Bearer <AGNES_API_KEY>`
- **模型名**: `agnes-image-2.1-flash`
- **价格**: 当前 `$0 / 张`

## 2. 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 是 | `agnes-image-2.1-flash` |
| `prompt` | string | 是 | 生成/编辑指令 |
| `size` | string | 是 | `1K`/`2K`/`3K`/`4K`（兼容 `1024x768` 精确写法） |
| `ratio` | string | 否 | `1:1`/`3:4`/`4:3`/`16:9`/`9:16`/`2:3`/`3:2`/`21:9`，默认 `1:1` |
| `extra_body.image` | string[] | 图生图必填 | 输入图片 URL 或 Data URI Base64，多图合成传多张 |
| `extra_body.response_format` | string | 否 | `url` 或 `b64_json` |

**关键约束：**
- `response_format` 必须在 `extra_body` 里，禁止放在顶层。
- 图生图不需要 `tags: ["img2img"]`。
- 输入图片需公开 HTTPS URL，或使用 Data URI Base64。

## 3. 尺寸与宽高比

建议 `size`（档位）+ `ratio`（宽高比）配合使用。

| Ratio | 1K | 2K | 3K | 4K |
|-------|----|----|----|----|
| 1:1 | 1024x1024 | 2048x2048 | 3072x3072 | 4096x4096 |
| 3:4 | 864x1152 | 1728x2304 | 2592x3456 | 3456x4608 |
| 4:3 | 1152x864 | 2304x1728 | 3456x2592 | 4608x3456 |
| 16:9 | 1312x736 | 2624x1472 | 3936x2208 | 5248x2944 |
| 9:16 | 736x1312 | 1472x2624 | 2208x3936 | 2944x5248 |
| 2:3 | 832x1248 | 1664x2496 | 2496x3744 | 3328x4992 |
| 3:2 | 1248x832 | 2496x1664 | 3744x2496 | 4992x3328 |
| 21:9 | 1568x672 | 3136x1344 | 4704x2016 | 6272x2688 |

**注意：** `1920x1080` 和 `2560x1440` 不是原生尺寸，会被标准化（如映射为 16:9 的 1K `1312x736`）。需要 16:9 显示素材时用 `size: "2K"` + `ratio: "16:9"` 再裁剪。

## 4. 响应格式

```json
{
  "created": 1780000000,
  "data": [
    {
      "url": "https://platform-outputs.agnes-ai.space/images/t2i/xxx.png",
      "b64_json": null,
      "revised_prompt": null
    }
  ]
}
```

- URL 输出路径：`data[0].url`
- Base64 输出路径：`data[0].b64_json`

## 5. 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 400 | 顶层放了 `response_format` | 移到 `extra_body` |
| 400 | 图生图缺 `extra_body.image` | 补充输入图片 |
| 400 | 精确尺寸不受支持 | 用档位 `1K`~`4K` + `ratio` |
| 超时 | 图片较大/负载高 | 客户端超时设 `60s`-`360s` |
