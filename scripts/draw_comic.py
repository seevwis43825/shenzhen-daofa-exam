#!/usr/bin/env python3
"""试卷漫画题插图绘制脚手架（黑白简笔画，仿真题版式）。

用法：复制本文件，在 main() 中仿照示例逐元素绘制，输出 PNG 到试卷 HTML 同目录。
嵌入规范见 references/exam-format.md（width 用像素、src 需绝对路径）。

Pillow 依赖：PYTHONPATH 指向 C:\\Users\\16323\\.workbuddy\\binaries\\python\\envs\\htmldocx-libs
"""
import sys

from PIL import Image, ImageDraw, ImageFont

F_REG = "C:/Windows/Fonts/msyh.ttc"
F_BOLD = "C:/Windows/Fonts/msyhbd.ttc"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
W, H = 1400, 950  # 标准画布


def font(sz, bold=False):
    return ImageFont.truetype(F_BOLD if bold else F_REG, sz)


def title(d, w, text):
    """画布顶部居中加粗标题《...》。"""
    f = font(52, bold=True)
    bbox = d.textbbox((0, 0), text, font=f)
    d.text(((w - bbox[2]) / 2, 40), text, font=f, fill=BLACK)


def bubble(d, x0, y0, x1, y1, lines, tail_to, fsize=40):
    """椭圆对话气泡 + 居中文字 + 尾巴（tail_to 指向说话者头顶）。"""
    d.ellipse([x0, y0, x1, y1], outline=BLACK, width=6)
    cx = (x0 + x1) // 2
    d.polygon([(cx - 30, y1 - 10), (cx + 30, y1 - 10), tail_to], fill=WHITE, outline=BLACK)
    d.line([(cx - 30, y1 - 10), tail_to], fill=BLACK, width=6)
    d.line([(cx + 30, y1 - 10), tail_to], fill=BLACK, width=6)
    txt = "\n".join(lines)
    f = font(fsize)
    bbox = d.multiline_textbbox((0, 0), txt, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.multiline_text(((x0 + x1 - tw) / 2, (y0 + y1 - th) / 2 - bbox[1]), txt,
                     font=f, fill=BLACK, align="center")


def person(d, hx, hy, r=45):
    """火柴人（头圆 + 躯干 + 双腿双臂），(hx, hy) 为头部圆心。"""
    d.ellipse([hx - r, hy - r, hx + r, hy + r], outline=BLACK, width=7)
    d.line([hx, hy + r, hx, hy + 220], fill=BLACK, width=8)
    d.line([hx, hy + 220, hx - 70, hy + 340], fill=BLACK, width=8)
    d.line([hx, hy + 220, hx + 70, hy + 340], fill=BLACK, width=8)
    d.line([hx, hy + 90, hx - 90, hy + 170], fill=BLACK, width=8)
    d.line([hx, hy + 90, hx + 90, hy + 170], fill=BLACK, width=8)


def main(out_path="comic-demo.png"):
    """示例：意见箱讽刺漫画（演示各辅助函数用法，替换为实际命题素材）。"""
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    title(d, W, "《漫画标题》")
    # 场景元素示例：意见箱
    d.rectangle([820, 320, 1140, 500], outline=BLACK, width=8)
    d.rectangle([880, 380, 1080, 410], fill=BLACK)
    d.text((900, 440), "意见箱", font=font(42), fill=BLACK)
    # 火柴人 + 对话气泡
    person(d, 380, 400)
    bubble(d, 200, 130, 700, 330, ["提了意见，", "却石沉大海……"], (380, 340))
    img.save(out_path)
    print("saved:", out_path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "comic-demo.png")
