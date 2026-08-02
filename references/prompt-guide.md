# Prompt 指南

## 文生图

结构：`[主体] + [场景/环境] + [风格] + [光照] + [构图] + [质量要求]`

```
中文：日出时分薄雾峡谷上方的发光浮空城市，电影级写实风格，广角构图，丰富建筑细节，柔和金色光线，高视觉密度
英文：A luminous floating city above a misty canyon at sunrise, cinematic realism, wide-angle composition, rich architectural detail, soft golden light, high visual density
```

## 图生图

结构：`[改变要求] + [新风格/场景] + [添加或移除元素] + [保留的元素]`

```
中文：将白天街道改为赛博朋克夜景，添加霓虹招牌和湿滑路面倒影，保留原始街道布局、相机角度和主要建筑形状
英文：Transform the day street scene into a cyberpunk night, add neon signs and wet road reflections, while preserving the original street layout, camera angle, and main building shapes
```

**务必包含** `preserving the original composition`，否则模型可能重绘整个画面。

## 多图合成

结构：`[每张参考图角色] + [目标场景] + [图像间关系] + [风格/光照/构图]`

```
英文：Use the first image as the main character and the second as the product reference, generate a cinematic event poster, preserve the character identity and product shape, natural lighting, clean commercial composition
```

## 高信息密度图像

清晰描述视觉层次：主要主体、背景环境、重要次要细节、风格、光照、构图约束。

```
英文：A large fantasy port city built on a cliff, hundreds of small boats, stacked stone bridges, glowing windows, distant mountains, cloudy sunset sky, cinematic fantasy realism, wide-angle composition, rich architectural detail, high visual density
```

## 通用规则

- 风格词越具体越好：`cinematic realism`、`flat vector`、`watercolor`、`3D render`
- 质量词统一用：`high detail`、`high visual density`、`high quality`
- 负面词：模型不支持负面提示词，通过正面描述规避（如"无文字"→"no text"放正面）
