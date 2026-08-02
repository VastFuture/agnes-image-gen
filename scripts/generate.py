#!/usr/bin/env python3
"""
Agnes Image 2.1 Flash 图像生成脚本。

支持文生图、图生图、多图合成。
API Key 从环境变量 AGNES_API_KEY 读取。

用法:
    # 文生图
    python3 generate.py "prompt" --size 2K --ratio 16:9 -o output.png

    # 图生图
    python3 generate.py "编辑指令" --image ./ref.png -o output.png

    # 多图合成
    python3 generate.py "合成指令" --image ./a.png ./b.png -o output.png

输出:
    保存到 -o 指定的本地文件（默认 ./output.png），同时打印图片 URL。
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://apihub.agnes-ai.com/v1/images/generations"
DEFAULT_MODEL = "agnes-image-2.1-flash"
VALID_SIZES = ("1K", "2K", "3K", "4K")
VALID_RATIOS = ("1:1", "3:4", "4:3", "16:9", "9:16", "2:3", "3:2", "21:9")


def load_images(paths):
    """把本地图片文件转成 Data URI Base64。"""
    uris = []
    for p in paths:
        if p.startswith(("http://", "https://", "data:")):
            uris.append(p)
            continue
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        uris.append(f"data:image/png;base64,{b64}")
    return uris


def generate(prompt, size, ratio, images, return_base64, timeout):
    payload = {
        "model": DEFAULT_MODEL,
        "prompt": prompt,
        "size": size,
    }
    if ratio:
        payload["ratio"] = ratio
    extra = {"response_format": "b64_json" if return_base64 else "url"}
    if images:
        extra["image"] = load_images(images)
    payload["extra_body"] = extra

    api_key = os.environ.get("AGNES_API_KEY")
    if not api_key:
        print("Error: 环境变量 AGNES_API_KEY 未设置。", file=sys.stderr)
        sys.exit(2)

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Error: HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: 网络请求失败: {e.reason}", file=sys.stderr)
        sys.exit(1)

    item = data.get("data", [{}])[0]
    return item.get("url"), item.get("b64_json")


def save_b64(b64, path):
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))


def main():
    parser = argparse.ArgumentParser(description="Agnes Image 2.1 Flash 图像生成")
    parser.add_argument("prompt", help="图像生成/编辑的文本指令")
    parser.add_argument("--size", default="2K", choices=list(VALID_SIZES) + ["1024x768"],
                        help="尺寸档位 (默认 2K)")
    parser.add_argument("--ratio", default=None, choices=list(VALID_RATIOS),
                        help="宽高比 (默认 1:1，配合档位式 size 使用)")
    parser.add_argument("--image", nargs="+", default=None,
                        help="输入图片路径/URL，支持多张（图生图或多图合成）")
    parser.add_argument("-o", "--output", default="./output.png",
                        help="输出文件路径 (默认 ./output.png)")
    parser.add_argument("--b64", action="store_true",
                        help="以 Base64 返回并保存")
    parser.add_argument("--timeout", type=int, default=300,
                        help="请求超时秒数 (默认 300)")
    args = parser.parse_args()

    url, b64 = generate(args.prompt, args.size, args.ratio,
                        args.image, args.b64, args.timeout)

    if args.b64 and b64:
        save_b64(b64, args.output)
        print(f"Saved: {args.output}")
    elif url:
        print(f"URL: {url}")
        if args.output and not args.output.startswith("none"):
            req = urllib.request.Request(url)
            try:
                with urllib.request.urlopen(req, timeout=args.timeout) as resp:
                    data = resp.read()
                with open(args.output, "wb") as f:
                    f.write(data)
                print(f"Saved: {args.output}")
            except Exception as e:
                print(f"Warning: 图片下载失败: {e}", file=sys.stderr)
    else:
        print("Error: 响应中无图片数据。", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
