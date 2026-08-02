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

## 验证结论

- 文生图、图生图均正常，输出尺寸与文档规格一致。
- 图生图响应 URL 包含 `i2i` 路径段，文生图为 `t2i`，可用此特征判断请求类型。
- 生成本地文件默认保存在当前目录 `output.png`。
