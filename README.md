# agnes-image-gen

Agnes Image 2.1 Flash 图像生成 skill，支持文生图、图生图和多图合成。

官方文档：https://www.agnes-ai.com/

## 示例

### 文生图

**浮空城市**（2K / 16:9）：

```
A luminous floating city above a misty canyon at sunrise, cinematic realism, golden light, high detail
```

![文生图示例 - 浮空城市](assets/example-float-city.png)

**VR 头显爆炸视图海报**（2K / 16:9）：

```
Vertical exploded view of a Meta Quest 3 VR headset, 9 stacked layers of internal components: outer shell, camera sensors, mainboard with chip, Pancake lenses, internal frame, battery pack, side straps, top head strap, facial interface pad. Clean high-tech 3D render, studio lighting, glowing accents, soft purple-blue gradient background, commercial poster layout
```

![文生图示例 - VR 头显爆炸视图](assets/example-quest3-exploded-view.png)

**成都吃货暴走地图**（2K / 16:9）：

```
Hand-drawn tourist map infographic of Chengdu on aged parchment, watercolor and ink illustration, vintage style, landmarks and food spots, giant panda centerpiece, retro compass, high visual density
```

![文生图示例 - 成都美食地图](assets/example-chengdu-food-map.png)

**超市抓拍人像**（2K / 9:16 竖版）：

```
Vertical candid photo on smartphone, young adult woman shopping in modern supermarket at night, showing an open egg carton toward camera, face blurred, realistic photography, shallow depth of field, fashion lifestyle aesthetic
```

![文生图示例 - 超市抓拍](assets/example-supermarket-candid.png)

**Instagram 信息图**（2K / 1:1）：

```
Instagram infographic about how advertisers exploit cognitive biases, high information density, modern flat design, grid layout, numbered sections with icons, professional marketing design
```

![文生图示例 - 认知偏差信息图](assets/example-cognitive-bias-infographic.png)

### 图生图

**构图保留改色**（1K / 1:1）：

```
Make the object orange while preserving the original composition
```

![图生图示例 - 玻璃立方体改色](assets/example-img2img-orange.png)

## 结构

```
agnes-image-gen/
├── SKILL.md                    # 工作流 + Iron Law
├── scripts/generate.py         # 生图脚本
├── references/
│   ├── api-reference.md        # API 参数、尺寸表、错误处理
│   ├── prompt-guide.md         # 提示词结构指南
│   └── example-test-log.md     # 实测示例与验证结果
└── assets/
    ├── example-float-city.png               # 文生图示例（2K/16:9 浮空城市）
    ├── example-quest3-exploded-view.png     # 文生图示例（2K/16:9 VR 爆炸视图）
    ├── example-chengdu-food-map.png         # 文生图示例（2K/16:9 成都美食地图）
    ├── example-supermarket-candid.png       # 文生图示例（2K/9:16 超市抓拍）
    ├── example-cognitive-bias-infographic.png  # 文生图示例（2K/1:1 信息图）
    └── example-img2img-orange.png           # 图生图示例（构图保留改色）
```

## 环境要求

- 设置环境变量 `AGNES_API_KEY`（从 https://www.agnes-ai.com/ 获取）

## 使用

```bash
# 文生图
python3 scripts/generate.py "A luminous floating city above a misty canyon at sunrise, cinematic realism" --size 2K --ratio 16:9 -o output.png

# 图生图
python3 scripts/generate.py "Make the object orange while preserving the original composition" --image ./input.png -o output.png

# 多图合成
python3 scripts/generate.py "Combine the two characters into a fantasy battle scene" --image ./a.png ./b.png -o output.png
```

### 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--size` | `2K` | 1K / 2K / 3K / 4K |
| `--ratio` | `1:1` | 1:1 / 16:9 / 9:16 / 3:4 / 4:3 / 2:3 / 3:2 / 21:9 |
| `--image` | 无 | 图生图/多图合成输入（路径或 URL） |
| `-o` | `./output.png` | 输出路径 |
| `--b64` | 否 | 以 Base64 返回并保存 |

## 能力

- 文生图：根据文本提示词生成图像
- 图生图：转换、重绘、风格化编辑，保留原始构图
- 多图合成：组合多张参考图像生成新图
- 尺寸控制：1K~4K 档位配合宽高比
- URL / Base64 输出

## 安装

将本目录放到你的 skill 加载路径（如 `~/.agents/skills/`）即可。
