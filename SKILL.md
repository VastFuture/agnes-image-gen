---
name: agnes-image-gen
description: "Agnes AI 图像生成。基于 agnes-image-2.1-flash 模型，支持文生图、图生图、多图合成。当用户想生成图片、画图、做图、AI 绘图、文生图、图生图、风格转换、图片编辑、生成海报/封面/配图/插画/产品图/壁纸/头像时使用。Actions: generate, create, draw, generate image, 生图, 画图, 做图, 生成图片, 生成海报, 配图, 合成. 支持尺寸 1K/2K/3K/4K 与宽高比 1:1/16:9/9:16/3:4/4:3。需要 AGNES_API_KEY 环境变量。"
---

# Agnes Image Gen

IRON LAW: 生成图片前，必须把用户意图转成结构化的英文 prompt（`[主体] + [场景] + [风格] + [光照] + [构图] + [质量]`）。禁止直接丢弃用户描述，也禁止擅自省略尺寸与宽高比——用户没指定时用默认值并明确告知。

## Workflow

Copy this checklist and check off items as you complete them:

```
Agnes Image Gen Progress:

- [ ] Step 1: 解析意图 ⚠️ REQUIRED
  - [ ] 1.1 判断类型：文生图 / 图生图 / 多图合成
  - [ ] 1.2 提取 prompt、尺寸、宽高比、输入图片
  - [ ] 1.3 构造结构化英文 prompt
- [ ] Step 2: 确认 ⚠️ REQUIRED
  - [ ] 展示将要执行的命令与参数
  - [ ] 用户确认后才执行（除非 --quick）
- [ ] Step 3: 执行生成
  - [ ] 检查 AGNES_API_KEY 已设置
  - [ ] 运行 scripts/generate.py
- [ ] Step 4: 交付
  - [ ] 报告输出文件路径与图片 URL
  - [ ] 提示用户查看效果
```

## Step 1: 解析意图 ⚠️ REQUIRED

先判断用户想要哪种生成：

| 类型 | 判定 | 需要参数 |
|------|------|----------|
| 文生图 | 只有文字描述 | `prompt` |
| 图生图 | 提到"编辑/改/转换/风格化"一张已有图片 | `prompt` + `--image <path>` |
| 多图合成 | 提到"合成/结合"多张图 | `prompt` + `--image <a> <b>...` |

问自己：用户给了图片路径吗？给了几张？意图是"从头生成"还是"编辑现有图"？

### 1.2 参数提取

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--size` | `2K` | 1K / 2K / 3K / 4K |
| `--ratio` | `1:1` | 1:1 / 16:9 / 9:16 / 3:4 / 4:3 / 2:3 / 3:2 / 21:9 |
| `--image` | 无 | 图生图/多图合成必填 |
| `-o` | `./output.png` | 输出路径 |

尺寸与宽高比的组合输出规格见 `references/api-reference.md`。

### 1.3 构造 prompt

- 文生图结构：`[主体] + [场景/环境] + [风格] + [光照] + [构图] + [质量要求]`
- 图生图结构：`[改变要求] + [新风格/场景] + [添加/移除元素] + [保留的元素]`（务必包含 "preserving the original composition"）
- 多图合成结构：`[每张参考图角色] + [目标场景] + [图像间关系] + [风格/光照/构图]`

用户用中文描述时，翻译成英文 prompt 传给模型；中文描述保留为辅助信息。

## Step 2: 确认 ⚠️ REQUIRED

展示将执行的完整命令：

```bash
python3 scripts/generate.py "<prompt>" --size <size> --ratio <ratio> [--image <path>] -o <output>
```

除非用户传入 `--quick`，否则必须等待明确确认。

## Step 3: 执行生成

检查 `AGNES_API_KEY` 是否设置：

```bash
echo "${AGNES_API_KEY:+set}"
```

未设置则提示用户设置，不要继续。然后运行命令。生成耗时数秒到几十秒，超时设置 300 秒足够。

## Step 4: 交付

- 告知输出文件绝对路径
- 提供图片 URL（脚本输出中有）
- 提示用户查看，询问是否调整 prompt 重新生成

## Anti-Patterns

- 不要把用户的中文描述原样当 prompt 使用——不结构化会导致语义对齐差
- 不要省略 `preserving the original composition`（图生图时）
- 不要请求 `1920x1080` 这类非原生精确尺寸——会被标准化，改用 `2K` + `16:9`
- 不要把 `response_format` 放在请求顶层——必须在 `extra_body` 里
- 不要传入 `tags: ["img2img"]`——图生图不需要
- 不要硬编码 API Key——只从环境变量 `AGNES_API_KEY` 读取
- 生成失败时，先检查 HTTP 错误码与响应体，不要盲目重试

## Pre-Delivery Checklist

- [ ] 输出文件已生成且存在（脚本返回 `Saved: ...`）
- [ ] prompt 是结构化英文，包含风格与质量要求
- [ ] 尺寸/宽高比符合用户请求或已告知默认值
- [ ] 无 TODO/占位符残留
- [ ] 未修改用户未要求的文件

## References

- `references/api-reference.md` — API 端点、参数、尺寸表、错误处理（需要细节时加载）
- `references/prompt-guide.md` — 提示词结构与示例（构造复杂 prompt 时加载）
- `references/example-test-log.md` — 实测示例与验证结果（确认模型行为时加载）
