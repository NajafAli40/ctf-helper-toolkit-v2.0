#!/usr/bin/env python3
"""
CTF Helper Toolkit v2.0
Created by Najaf Ali """

import os, sys, base64, hashlib, re, urllib.parse, time
from collections import Counter

# ── ANSI CODES ──────────────────────────────────────────────────────
class C:
    R="\033[0m"; B="\033[1m"; DIM="\033[2m"; IT="\033[3m"
    K="\033[30m"; RED="\033[31m"; GRN="\033[32m"; YEL="\033[33m"
    BLU="\033[34m"; MAG="\033[35m"; CYN="\033[36m"; WHT="\033[37m"
    BRED="\033[91m"; BGRN="\033[92m"; BYEL="\033[93m"; BBLU="\033[94m"
    BMAG="\033[95m"; BCYN="\033[96m"; BWHT="\033[97m"
    BG0="\033[40m"; BG1="\033[48;2;10;14;26m"; BG2="\033[48;2;15;32;64m"
    FG_GOLD="\033[38;2;255;215;0m"
    FG_NEON="\033[38;2;0;212;255m"
    FG_MINT="\033[38;2;16;185;129m"
    FG_ROSE="\033[38;2;244;63;94m"
    FG_PURP="\033[38;2;168;85;247m"
    FG_AMB="\033[38;2;245;158;11m"
    FG_DIM="\033[38;2;42;96;128m"
    FG_MID="\033[38;2;74;144;160m"
    FG_PALE="\033[38;2;139;179;200m"

def c(text,*codes): return "".join(codes)+str(text)+C.R

W = 110  # terminal width

# ── BANNER ──────────────────────────────────────────────────────────
BANNER_LINES = [
    r" ██████╗████████╗███████╗    ██╗  ██╗███████╗██╗     ██████╗ ",
    r"██╔════╝╚══██╔══╝██╔════╝    ██║  ██║██╔════╝██║     ██╔══██╗",
    r"██║        ██║   █████╗      ███████║█████╗  ██║     ██████╔╝",
    r"██║        ██║   ██╔══╝      ██╔══██║██╔══╝  ██║     ██╔═══╝ ",
    r"╚██████╗   ██║   ██║         ██║  ██║███████╗███████╗██║     ",
    r" ╚═════╝   ╚═╝   ╚═╝         ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ",
]

def banner():
    os.system("clear")
    print()
    print(c("╔" + "═"*W + "╗", C.FG_NEON, C.B))
    print(c("║" + " "*W + "║", C.FG_NEON, C.B))
    for line in BANNER_LINES:
        pad = (W - len(line)) // 2
        row = " "*pad + line + " "*(W - pad - len(line))
        print(c("║", C.FG_NEON, C.B) + c(row, C.FG_NEON, C.B) + c("║", C.FG_NEON, C.B))
    print(c("║" + " "*W + "║", C.FG_NEON, C.B))
    sub = "T  O  O  L  K  I  T"
    pad = (W - len(sub)) // 2
    row = " "*pad + sub + " "*(W - pad - len(sub))
    print(c("║", C.FG_NEON, C.B) + c(row, C.BMAG, C.B) + c("║", C.FG_NEON, C.B))
    print(c("║" + " "*W + "║", C.FG_NEON, C.B))
    cr = "✦   Created by  Najaf Ali  ·  Cybersecurity Student   ✦"
    pad = (W - len(cr)) // 2
    row = " "*pad + cr + " "*(W - pad - len(cr))
    print(c("║", C.FG_NEON, C.B) + c(row, C.FG_GOLD, C.B) + c("║", C.FG_NEON, C.B))
    print(c("║" + " "*W + "║", C.FG_NEON, C.B))
    print(c("╚" + "═"*W + "╝", C.FG_NEON, C.B))
    print()

MODULES = [
    ("1", "⌥", C.FG_NEON,  "Encoding / Decoding",   "Base64 · Hex · Caesar · Vigenère · Binary · URL",  "7 tools"),
    ("2", "#", C.FG_PURP,  "Hashing",               "MD5 · SHA-1/224/256/384/512 · Hash Identifier",    "8 tools"),
    ("3", "⊕", C.FG_AMB,   "Crypto Helpers",         "XOR Cipher · Frequency Analysis",                 "4 tools"),
    ("4", "◈", C.FG_MINT,  "Steganography",          "EXIF · LSB Detect · Magic Bytes · Hex Dump",       "4 tools"),
    ("5", "⚙", C.FG_ROSE,  "Misc Utilities",         "Morse · Bit Ops · Base Converter · ASCII codes",   "7 tools"),
]

STATUS_BAR = [
    ("PYTHON","3.6+"), ("PLATFORM","KALI LINUX"),
    ("AUTHOR","NAJAF ALI"), ("MODULES","5"), ("TOOLS","30+"),
]

def main_menu():
    banner()
    # top border
    print(c("  ┌" + "─"*(W-2) + "┐", C.FG_MID))
    lbl = "  SELECT A MODULE"
    print(c("  │", C.FG_MID) + c(lbl, C.FG_NEON, C.B) + " "*(W-2-len(lbl)) + c("│", C.FG_MID))
    print(c("  ├" + "─"*(W-2) + "┤", C.FG_MID))
    print(c("  │" + " "*(W-2) + "│", C.FG_MID))

    for num, icon, col, label, desc, tag in MODULES:
        # build the line
        num_s  = c(f" [{num}]", C.FG_NEON, C.B)
        icon_s = c(f" {icon} ", col, C.B)
        lbl_s  = c(f"{label:<22}", C.BWHT, C.B)
        desc_s = c(f"{desc}", C.FG_PALE)
        tag_s  = c(f" [{tag}]", C.FG_DIM)
        inner  = f"{num_s}{icon_s}{lbl_s}{desc_s}{tag_s}"
        # strip ANSI to measure real length
        raw    = f" [{num}] {icon} {label:<26}{desc} [{tag}]"
        pad    = W - 2 - len(raw)
        print(c("  │", C.FG_MID) + inner + " "*max(pad,0) + c("│", C.FG_MID))
        print(c("  │" + " "*(W-2) + "│", C.FG_MID))

    print(c("  ├" + "─"*(W-2) + "┤", C.FG_MID))
    exit_s = c(" [0]", C.BRED, C.B) + c(" ✕  Exit", C.BWHT, C.B)
    raw_e  = " [0] ✕  Exit"
    print(c("  │", C.FG_MID) + exit_s + " "*(W-2-len(raw_e)) + c("│", C.FG_MID))
    print(c("  └" + "─"*(W-2) + "┘", C.FG_MID))
    print()

    # status bar
    bar = "  "
    for k, v in STATUS_BAR:
        bar += c(k+" ", C.FG_DIM) + c(v, C.FG_MID) + c("  ·  ", C.FG_DIM)
    print(bar.rstrip(" ·  "))
    print()

# ── UI HELPERS ───────────────────────────────────────────────────────
def hdr(title, col=C.FG_NEON):
    os.system("clear")
    print()
    line = f"  ╔══ {title} "
    line += "═" * max(0, W - len(line) + 2) + "╗"
    print(c(line, col, C.B))

def hdr_close(col=C.FG_NEON):
    print(c("  ╚" + "═"*W + "╝", col, C.B))
    print()

def submenu(options, title, col=C.FG_NEON):
    while True:
        hdr(title, col)
        for num, label in options:
            bullet = c(f"    [{num}]", col, C.B)
            print(f"{bullet}  {c(label, C.BWHT)}")
        hdr_close(col)
        ch = prompt("Select option")
        if ch == "0": break
        yield ch

def ok(msg):   print(c("  ✔ ", C.BGRN, C.B) + c(msg, C.BWHT))
def err(msg):  print(c("  ✘ ", C.BRED, C.B) + c(msg, C.BRED))
def info(msg): print(c("  ℹ ", C.FG_AMB, C.B) + c(msg, C.BWHT))

def box(label, value, col=C.FG_NEON):
    print()
    print(c(f"  ╭─ {label}", col, C.B))
    for line in str(value).split("\n"):
        print(c("  │  ", col) + c(line, C.BWHT, C.B))
    print(c("  ╰" + "─"*42, col))

def ruler(col=C.FG_DIM): print(c("  " + "─"*60, col))

def prompt(msg):
    return input(c("\n  ▶ ", C.BMAG, C.B) + c(msg + " : ", C.BWHT))

def pause(): input(c("\n  Press ENTER to continue...", C.FG_DIM))

# ── MODULE 1: ENCODING / DECODING ───────────────────────────────────
def caesar(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            b = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch)-b+shift)%26+b)
        else: out += ch
    return out

def vigenere(text, key, decrypt=False):
    key = key.upper(); ki = 0; out = ""
    for ch in text:
        if ch.isalpha():
            s = ord(key[ki%len(key)])-ord("A")
            b = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch)-b+(-s if decrypt else s))%26+b)
            ki += 1
        else: out += ch
    return out

def mod_encoding():
    OPT = [
        ("1","Base64  Encode"), ("2","Base64  Decode"),
        ("3","Hex  Encode"),    ("4","Hex  Decode"),
        ("5","ROT13"),
        ("6","Caesar  Cipher — Encrypt / Decrypt"),
        ("7","Caesar  Cipher — Brute Force ALL 25 shifts"),
        ("8","Vigenère — Encrypt"), ("9","Vigenère — Decrypt"),
        ("10","Binary ↔ ASCII Converter"),
        ("11","URL  Encode / Decode"),
        ("0","← Back"),
    ]
    while True:
        hdr("MODULE 1  —  ENCODING / DECODING", C.FG_NEON)
        for n,l in OPT:
            print(c(f"    [{n}]", C.FG_NEON, C.B) + f"  {c(l,C.BWHT)}")
        hdr_close(C.FG_NEON)
        ch = prompt("Select")

        if ch=="1":
            t=prompt("Text to encode"); box("Base64",base64.b64encode(t.encode()).decode())
        elif ch=="2":
            t=prompt("Base64 to decode")
            try: box("Decoded",base64.b64decode(t).decode())
            except: err("Invalid Base64")
        elif ch=="3":
            t=prompt("Text to hex"); box("Hex",t.encode().hex())
        elif ch=="4":
            t=prompt("Hex to decode")
            try: box("Decoded",bytes.fromhex(t.replace(" ","")).decode())
            except: err("Invalid hex")
        elif ch=="5":
            t=prompt("Text for ROT13")
            r=t.translate(str.maketrans(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))
            box("ROT13",r)
        elif ch=="6":
            t=prompt("Text"); s=int(prompt("Shift (1-25)"))
            m=prompt("(e)ncrypt / (d)ecrypt").lower()
            box("Result", caesar(t,-s if m=="d" else s))
        elif ch=="7":
            t=prompt("Ciphertext to brute-force")
            print(); info("All 25 Caesar shifts:"); ruler()
            for s in range(1,26):
                print(c(f"  Shift {s:2d} : ",C.FG_AMB)+c(caesar(t,s),C.BWHT))
        elif ch=="8":
            t=prompt("Plaintext"); k=prompt("Key")
            box("Vigenère Encrypted", vigenere(t,k))
        elif ch=="9":
            t=prompt("Ciphertext"); k=prompt("Key")
            box("Vigenère Decrypted", vigenere(t,k,True))
        elif ch=="10":
            d=prompt("(1) Text→Binary  (2) Binary→Text")
            if d=="1":
                t=prompt("Text")
                box("Binary"," ".join(format(ord(c2),"08b") for c2 in t))
            else:
                t=prompt("Binary (space-separated bytes)")
                try: box("ASCII","".join(chr(int(b,2)) for b in t.split()))
                except: err("Invalid binary")
        elif ch=="11":
            d=prompt("(1) Encode  (2) Decode"); t=prompt("Text")
            box("Result", urllib.parse.quote(t) if d=="1" else urllib.parse.unquote(t))
        elif ch=="0": break
        else: err("Invalid option")
        pause()

# ── MODULE 2: HASHING ────────────────────────────────────────────────
HP = {
    r"^[a-f0-9]{32}$":"MD5", r"^[a-f0-9]{40}$":"SHA-1",
    r"^[a-f0-9]{56}$":"SHA-224", r"^[a-f0-9]{64}$":"SHA-256",
    r"^[a-f0-9]{96}$":"SHA-384", r"^[a-f0-9]{128}$":"SHA-512",
    r"^\$2[ayb]\$.{56}$":"bcrypt", r"^\$1\$.{1,8}\$.{22}$":"MD5-crypt",
    r"^\$5\$.+\$.{43}$":"SHA-256-crypt", r"^\$6\$.+\$.{86}$":"SHA-512-crypt",
}
ALGOS = [("MD5",hashlib.md5),("SHA-1",hashlib.sha1),("SHA-224",hashlib.sha224),
          ("SHA-256",hashlib.sha256),("SHA-384",hashlib.sha384),("SHA-512",hashlib.sha512)]

def mod_hashing():
    OPT = [("1","MD5"),("2","SHA-1"),("3","SHA-224"),("4","SHA-256"),
           ("5","SHA-384"),("6","SHA-512"),("7","ALL hashes at once"),
           ("8","Hash Identifier"),("0","← Back")]
    while True:
        hdr("MODULE 2  —  HASHING", C.FG_PURP)
        for n,l in OPT:
            print(c(f"    [{n}]",C.FG_PURP,C.B)+f"  {c(l,C.BWHT)}")
        hdr_close(C.FG_PURP)
        ch=prompt("Select")
        if ch in [str(i+1) for i in range(6)]:
            name,fn=ALGOS[int(ch)-1]; t=prompt(f"Text for {name}")
            box(name+" Hash", fn(t.encode()).hexdigest(), C.FG_PURP)
        elif ch=="7":
            t=prompt("Text"); ruler(); print()
            for name,fn in ALGOS:
                print(c(f"  {name:<8} : ",C.FG_AMB)+c(fn(t.encode()).hexdigest(),C.BWHT))
        elif ch=="8":
            h=prompt("Hash to identify").strip()
            found="Unknown"
            for pat,name in HP.items():
                if re.match(pat,h,re.I): found=name; break
            box("Hash Type",found,C.FG_PURP); info(f"Length: {len(h)} chars")
        elif ch=="0": break
        else: err("Invalid")
        pause()

# ── MODULE 3: CRYPTO HELPERS ─────────────────────────────────────────
ENG = {'e':12.70,'t':9.06,'a':8.17,'o':7.51,'i':6.97,'n':6.75,'s':6.33,
       'h':6.09,'r':5.99,'d':4.25,'l':4.03,'c':2.78,'u':2.76,'m':2.41,
       'w':2.36,'f':2.23,'g':2.02,'y':1.97,'p':1.93,'b':1.49,'v':0.98,
       'k':0.77,'j':0.15,'x':0.15,'q':0.10,'z':0.07}

def mod_crypto():
    OPT=[("1","XOR — Text key"),("2","XOR — Hex key"),
         ("3","Frequency Analysis"),("4","Freq Analysis vs English"),("0","← Back")]
    while True:
        hdr("MODULE 3  —  CRYPTO HELPERS", C.FG_AMB)
        for n,l in OPT:
            print(c(f"    [{n}]",C.FG_AMB,C.B)+f"  {c(l,C.BWHT)}")
        hdr_close(C.FG_AMB)
        ch=prompt("Select")
        if ch=="1":
            t=prompt("Text"); k=prompt("Key")
            tb=t.encode(); kb=k.encode()
            xr=bytes([tb[i]^kb[i%len(kb)] for i in range(len(tb))])
            box("XOR hex",xr.hex(),C.FG_AMB); box("XOR b64",base64.b64encode(xr).decode(),C.FG_AMB)
        elif ch=="2":
            try:
                t=bytes.fromhex(prompt("Hex data")); k=bytes.fromhex(prompt("Hex key"))
                xr=bytes([t[i]^k[i%len(k)] for i in range(len(t))])
                box("XOR hex",xr.hex(),C.FG_AMB)
                try: box("XOR ASCII",xr.decode(),C.FG_AMB)
                except: pass
            except: err("Invalid hex")
        elif ch=="3":
            t=prompt("Ciphertext")
            lets=[x.lower() for x in t if x.isalpha()]
            if not lets: err("No letters"); pause(); continue
            total=len(lets); cnt=Counter(lets)
            freqs=sorted(cnt.items(),key=lambda x:-x[1])
            print(); info("Letter frequencies:")
            ruler()
            for ch2,n in freqs:
                pct=n/total*100; bar="█"*int(pct/1.5)
                print(c(f"  {ch2.upper()} ",C.FG_AMB,C.B)+c(f"{pct:5.2f}% ",C.BWHT)+c(bar,C.FG_NEON))
        elif ch=="4":
            t=prompt("Ciphertext")
            lets=[x.lower() for x in t if x.isalpha()]
            total=len(lets); cnt=Counter(lets)
            print()
            print(c(f"  {'LTR':<5}{'YOURS':>8}{'ENGLISH':>10}{'DIFF':>8}",C.BWHT,C.B)); ruler()
            for letter in sorted(ENG):
                mine=cnt.get(letter,0)/total*100 if total else 0
                eng=ENG[letter]; diff=mine-eng
                dc=C.BGRN if abs(diff)<2 else C.BRED
                print(c(f"  {letter.upper():<5}",C.FG_AMB)+c(f"{mine:>8.2f}",C.BWHT)+
                      c(f"{eng:>10.2f}",C.FG_NEON)+c(f"{diff:>+8.2f}",dc))
        elif ch=="0": break
        else: err("Invalid")
        pause()

# ── MODULE 4: STEGANOGRAPHY ──────────────────────────────────────────
MAGIC={b"\xff\xd8\xff":"JPEG Image",b"\x89PNG":"PNG Image",b"GIF8":"GIF Image",
       b"BM":"BMP Image",b"%PDF":"PDF Document",b"PK\x03\x04":"ZIP Archive",
       b"\x1f\x8b":"GZIP Archive",b"Rar!":"RAR Archive",b"\x7fELF":"ELF Executable",
       b"MZ":"Windows EXE/DLL",b"ID3":"MP3 Audio",b"fLaC":"FLAC Audio",
       b"RIFF":"WAV/AVI",b"OggS":"OGG",b"II*\x00":"TIFF (LE)",b"MM\x00*":"TIFF (BE)"}

def mod_steg():
    OPT=[("1","Extract Metadata / EXIF"),("2","LSB Steganography Detector"),
         ("3","Magic Bytes / File Signature"),("4","Hex Dump (first 256 bytes)"),("0","← Back")]
    while True:
        hdr("MODULE 4  —  STEGANOGRAPHY", C.FG_MINT)
        for n,l in OPT:
            print(c(f"    [{n}]",C.FG_MINT,C.B)+f"  {c(l,C.BWHT)}")
        hdr_close(C.FG_MINT)
        ch=prompt("Select")
        if ch=="0": break
        if ch not in ("1","2","3","4"): err("Invalid"); pause(); continue
        fp=prompt("Full path to file")
        if not os.path.isfile(fp): err("File not found!"); pause(); continue

        if ch=="1":
            info(f"Reading: {fp}")
            print(c(f"\n  {'FIELD':<28}VALUE",C.BWHT,C.B)); ruler()
            print(c(f"  {'File size':<28}",C.FG_AMB)+c(str(os.path.getsize(fp))+" bytes",C.BWHT))
            with open(fp,"rb") as f: hdr_b=f.read(32)
            found="Unknown"
            for sig,name in MAGIC.items():
                if hdr_b.startswith(sig): found=name; break
            print(c(f"  {'File type (magic)':<28}",C.FG_AMB)+c(found,C.BWHT))
            print(c(f"  {'Header hex':<28}",C.FG_AMB)+c(hdr_b[:16].hex(),C.BWHT))
            try:
                from PIL import Image
                from PIL.ExifTags import TAGS
                img=Image.open(fp)
                print(c(f"  {'Image dimensions':<28}",C.FG_AMB)+c(f"{img.width}x{img.height}",C.BWHT))
                print(c(f"  {'Color mode':<28}",C.FG_AMB)+c(img.mode,C.BWHT))
                exif=img._getexif()
                if exif:
                    for tid,val in exif.items():
                        tag=TAGS.get(tid,tid)
                        print(c(f"  {str(tag)[:28]:<28}",C.FG_AMB)+c(str(val)[:60],C.BWHT))
            except ImportError: info("Install Pillow for EXIF: pip install Pillow")
            except: pass
        elif ch=="2":
            try:
                from PIL import Image
                img=Image.open(fp).convert("RGB")
                pixels=list(img.getdata())[:1000]
                bits=[b for r,g,bv in pixels for b in [r&1,g&1,bv&1]]
                ones=sum(bits); ratio=ones/len(bits)
                box("LSB Analysis",f"1-bits: {ones}  |  0-bits: {len(bits)-ones}  |  Ratio: {ratio:.4f}",C.FG_MINT)
                if 0.45<=ratio<=0.55: ok("LSB ratio ≈ 0.5 → possible steganography detected!")
                else: info("LSB ratio seems normal → unlikely LSB steganography")
            except ImportError: err("Install Pillow: pip install Pillow")
            except Exception as e: err(str(e))
        elif ch=="3":
            with open(fp,"rb") as f: raw=f.read(32)
            box("Magic Bytes (hex)",raw[:16].hex(),C.FG_MINT)
            found="Unknown"
            for sig,name in MAGIC.items():
                if raw.startswith(sig): found=name; break
            box("Detected Type",found,C.FG_MINT)
        elif ch=="4":
            with open(fp,"rb") as f: data=f.read(256)
            print(); info("Hex Dump (first 256 bytes):"); print()
            for i in range(0,len(data),16):
                chunk=data[i:i+16]
                hp=" ".join(f"{b:02x}" for b in chunk)
                ap="".join(chr(b) if 32<=b<127 else "." for b in chunk)
                print(c(f"  {i:04x}  ",C.FG_DIM)+c(f"{hp:<48}",C.FG_NEON)+c(f"  {ap}",C.FG_AMB))
        pause()

# ── MODULE 5: MISC UTILITIES ─────────────────────────────────────────
MORSE={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---",
       "K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
       "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
       "0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....",
       "6":"-....","7":"--...","8":"---..","9":"----."," ":"/"}
REV_MORSE={v:k for k,v in MORSE.items() if k!=" "}
MAG_TABLE=[("FF D8 FF","JPEG Image"),("89 50 4E 47","PNG Image"),("47 49 46 38","GIF Image"),
           ("42 4D","BMP Image"),("25 50 44 46","PDF Document"),("50 4B 03 04","ZIP Archive"),
           ("1F 8B","GZIP Archive"),("52 61 72 21","RAR Archive"),("7F 45 4C 46","ELF Executable"),
           ("4D 5A","Windows EXE/DLL"),("49 44 33","MP3 Audio"),("66 4C 61 43","FLAC Audio"),
           ("52 49 46 46","WAV/AVI"),("4F 67 67 53","OGG File"),("D0 CF 11 E0","MS Office (old)")]

def mod_misc():
    OPT=[("1","String Reverse"),("2","Full Hex Dump of text"),
         ("3","Magic Bytes Reference Table"),("4","String ↔ Decimal ASCII codes"),
         ("5","Morse Code Encode / Decode"),("6","Bit Manipulation  AND/OR/XOR/NOT"),
         ("7","Base Converter  Dec · Hex · Oct · Bin"),("0","← Back")]
    while True:
        hdr("MODULE 5  —  MISC UTILITIES", C.FG_ROSE)
        for n,l in OPT:
            print(c(f"    [{n}]",C.FG_ROSE,C.B)+f"  {c(l,C.BWHT)}")
        hdr_close(C.FG_ROSE)
        ch=prompt("Select")
        if ch=="1":
            t=prompt("Text to reverse"); box("Reversed",t[::-1],C.FG_ROSE)
        elif ch=="2":
            t=prompt("Text for hex dump"); data=t.encode(); print()
            for i in range(0,len(data),16):
                chunk=data[i:i+16]; hp=" ".join(f"{b:02x}" for b in chunk)
                ap="".join(chr(b) if 32<=b<127 else "." for b in chunk)
                print(c(f"  {i:04x}  ",C.FG_DIM)+c(f"{hp:<48}",C.FG_NEON)+c(f"  {ap}",C.FG_AMB))
        elif ch=="3":
            print(); print(c(f"  {'MAGIC BYTES':<20}FILE TYPE",C.BWHT,C.B)); ruler()
            for sig,name in MAG_TABLE:
                print(c(f"  {sig:<20}",C.FG_NEON)+c(name,C.BWHT))
        elif ch=="4":
            d=prompt("(1) Text→ASCII  (2) ASCII→Text")
            if d=="1":
                t=prompt("Text"); box("ASCII codes"," ".join(str(ord(c2)) for c2 in t),C.FG_ROSE)
            else:
                t=prompt("Decimal codes (space-separated)")
                try: box("Text","".join(chr(int(x)) for x in t.split()),C.FG_ROSE)
                except: err("Invalid input")
        elif ch=="5":
            d=prompt("(1) Encode  (2) Decode")
            if d=="1":
                t=prompt("Text").upper()
                box("Morse"," ".join(MORSE.get(c2,"?") for c2 in t),C.FG_ROSE)
            else:
                t=prompt("Morse (space=letters, /=words)")
                out=""
                for word in t.split(" / "):
                    for code in word.split(): out+=REV_MORSE.get(code,"?")
                    out+=" "
                box("Decoded",out.strip(),C.FG_ROSE)
        elif ch=="6":
            a=int(prompt("Integer A"),0); b=int(prompt("Integer B"),0)
            print()
            for op,val in [("AND",a&b),("OR",a|b),("XOR",a^b)]:
                print(c(f"  A {op} B = ",C.FG_AMB)+c(f"{val}",C.BWHT)+c(f"  (hex: {hex(val)})",C.FG_PALE))
            na=~a
            print(c(f"  NOT A   = ",C.FG_AMB)+c(f"{na}",C.BWHT)+c(f"  (hex: {hex(na&0xFFFFFFFF)})",C.FG_PALE))
        elif ch=="7":
            t=prompt("Integer (0x=hex, 0o=oct, 0b=bin)")
            try:
                n=int(t,0)
                for lbl,val in [("Decimal",str(n)),("Hex",hex(n)),("Octal",oct(n)),("Binary",bin(n))]:
                    print(c(f"\n  {lbl:<12}",C.FG_AMB)+c(val,C.BWHT,C.B))
            except: err("Invalid integer")
        elif ch=="0": break
        else: err("Invalid")
        pause()

# ── ABOUT ────────────────────────────────────────────────────────────
def about():
    os.system("clear"); print()
    lines=[
        ("",C.R),("  CTF HELPER TOOLKIT  v2.0",C.FG_GOLD+C.B),("",C.R),
        ("  Created by",C.FG_PALE),("  Najaf Ali",C.FG_NEON+C.B),("",C.R),
        ("  Cybersecurity Student",C.BWHT),("",C.R),
        ("  "+"─"*42,C.FG_DIM),("",C.R),
        ("  Modules:",C.BWHT+C.B),
        ("  ⌥  Encoding / Decoding          7 tools",C.FG_NEON),
        ("  #  Hashing                      8 tools",C.FG_PURP),
        ("  ⊕  Crypto Helpers               4 tools",C.FG_AMB),
        ("  ◈  Steganography                4 tools",C.FG_MINT),
        ("  ⚙  Misc Utilities               7 tools",C.FG_ROSE),
        ("",C.R),("  "+"─"*42,C.FG_DIM),("",C.R),
        ("  Platform : Kali Linux / Python 3.6+",C.FG_DIM),
        ("  License  : MIT",C.FG_DIM),("  GitHub   : github.com/najaf-ali",C.FG_DIM),("",C.R),
    ]
    bw=50
    print(c("  ╔"+"═"*bw+"╗",C.FG_NEON,C.B))
    for text,col in lines:
        pad=bw-len(text); row=text+" "*max(pad,0)
        print(c("  ║",C.FG_NEON,C.B)+col+row[:bw]+C.R+c("║",C.FG_NEON,C.B))
    print(c("  ╚"+"═"*bw+"╝",C.FG_NEON,C.B))
    print(); pause()

# ── MAIN ─────────────────────────────────────────────────────────────
def main():
    ACTIONS={"1":mod_encoding,"2":mod_hashing,"3":mod_crypto,"4":mod_steg,"5":mod_misc,"6":about}
    while True:
        main_menu()
        ch=prompt("Select module")
        if ch in ACTIONS: ACTIONS[ch]()
        elif ch=="0":
            os.system("clear"); print()
            print(c("  ✦ Thanks for using CTF Helper Toolkit", C.FG_GOLD, C.B))
            print(c("  ✦ Created by Najaf Ali", C.FG_NEON, C.B))
            print(c("  ✦ Happy Hacking! (ethically 😄)\n", C.BGRN, C.B))
            sys.exit(0)
        else: err("Invalid option — enter 1 to 5")
        time.sleep(0.3)

if __name__=="__main__":
    main()
