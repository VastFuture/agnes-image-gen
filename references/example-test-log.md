# 示例测试记录

> 使用 `scripts/generate.py` 对 Agnes Image 2.1 Flash 进行的实测记录。用于确认模型行为，生成图片见 `assets/`。

## 测试 1：文生图（2K / 16:9）

```bash
python3 generate.py "A luminous floating city above a misty canyon at sunrise, cinematic realism, golden light, high detail" --size 2K --ratio 16:9 -o float-city.png
```

- **结果**：成功，耗时数秒
- **输出**：`assets/example-float-city.png`，尺寸 `2624x1472`（符合 2K/16:9 规格）
- **URL**：`https://platform-outputs.agnes-ai.space/images/t2i/6b3cac2151e245979602aacb12ec914a.png`

## 测试 2：文生图（1K / 1:1）

```bash
python3 generate.py "A clean product photo of a glass cube on a white studio background, soft shadows, high detail" --size 1K --ratio 1:1 -o glass-cube.png
```

- **结果**：成功
- **输出**：`1024x1024`（符合 1K/1:1 规格）

## 测试 3：图生图（保留构图）

```bash
python3 generate.py "Make the object orange while preserving the original composition" --image glass-cube.png --size 1K --ratio 1:1 -o glass-cube-orange.png
```

- **结果**：成功，路径 `/images/i2i/` 确认走了图生图流程
- **输出**：`1024x1024`，构图保留

## 测试 4：产品爆炸视图海报（2K / 16:9）

```bash
python3 generate.py "Vertical exploded view of a Meta Quest 3 VR headset, 9 stacked layers of internal components: outer shell, camera sensors, mainboard with chip, Pancake lenses, internal frame, battery pack, side straps, top head strap, facial interface pad. Clean high-tech 3D render, studio lighting, glowing accents, soft purple-blue gradient background. Product poster with header, 8 callout labels with leader lines, commercial layout, high detail, high visual density" --size 2K --ratio 16:9 -o quest3-exploded.png
```

- **结果**：成功，验证"高信息密度图像"能力
- **输出**：`assets/example-quest3-exploded-view.png`，`2624x1472`

## 测试 5：手绘地图信息图（2K / 16:9）

```bash
python3 generate.py "Hand-drawn tourist map infographic of Chengdu on aged parchment, watercolor and ink illustration, vintage style. ... Retro compass, red chili mascot, vintage cartography style" --size 2K --ratio 16:9 -o chengdu-food-map.png
```

- **结果**：成功，验证复古插画风格 + 多元素地图布局
- **输出**：`assets/example-chengdu-food-map.png`，`2624x1472`

## 测试 6：竖版人像抓拍（2K / 9:16）

```bash
python3 generate.py "Vertical candid photo taken on smartphone, young adult woman shopping in supermarket at night, face blurred, showing open egg carton toward camera, realistic photography, shallow depth of field, fashion lifestyle aesthetic, vertical 9:16 composition" --size 2K --ratio 9:16 -o supermarket-woman.png
```

- **结果**：成功，验证 9:16 竖版写实人像 + 隐私模糊
- **输出**：`assets/example-supermarket-candid.png`，`1472x2624`

## 测试 7：Instagram 信息图（2K / 1:1）

```bash
python3 generate.py "Instagram infographic about how advertisers exploit cognitive biases, high information density, modern flat design, grid layout, numbered sections with icons, professional marketing design" --size 2K --ratio 1:1 -o cognitive-bias-infographic.png
```

- **结果**：成功，验证高信息密度 + 1:1 方形信息图
- **输出**：`assets/example-cognitive-bias-infographic.png`，`2048x2048`

## 验证结论

- 文生图、图生图均正常，输出尺寸与文档规格一致。
- 图生图响应 URL 包含 `i2i` 路径段，文生图为 `t2i`，可用此特征判断请求类型。
- 生成本地文件默认保存在当前目录 `output.png`。
- 高信息密度场景（海报/地图/信息图）均可生成；长文字标注渲染不可靠，属模型通病。
