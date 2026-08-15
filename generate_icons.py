from PIL import Image, ImageDraw

def make(size):
    S = 1024  # supersample
    img = Image.new("RGB", (S, S), "#1e222b")
    d = ImageDraw.Draw(img)
    oak = "#cf9a4f"
    chalk = "#ecebe4"

    # bold forward slash with round caps
    w = int(S * 0.13)
    x1, y1 = int(S*0.34), int(S*0.72)   # lower-left
    x2, y2 = int(S*0.66), int(S*0.28)   # upper-right
    d.line([(x1, y1), (x2, y2)], fill=oak, width=w)
    r = w // 2
    for (cx, cy) in [(x1, y1), (x2, y2)]:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=oak)

    # short chalk floor-line beneath the mark
    fw = int(S * 0.045)
    fx1, fx2 = int(S*0.36), int(S*0.64)
    fy = int(S*0.80)
    d.line([(fx1, fy), (fx2, fy)], fill=chalk, width=fw)
    fr = fw // 2
    for cx in (fx1, fx2):
        d.ellipse([cx-fr, fy-fr, cx+fr, fy+fr], fill=chalk)

    return img.resize((size, size), Image.LANCZOS)

for s in (180, 192, 512):
    make(s).save(f"/mnt/user-data/outputs/training-sheet/icon-{s}.png")
    print("wrote icon-%d.png" % s)
