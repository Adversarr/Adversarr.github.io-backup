#! /usr/bin/env python

import re
from argparse import ArgumentParser
import os
from os import path
from functools import reduce
import shutil
from pathlib import Path

image_regex = re.compile('\!\[.*\](.*)')
dry_run = False
summary = []

def preprocess_imgpath(r, d, b):
    p = path.join(d, r)
    if path.exists(p):
        return p

    p = path.join(d, b)
    p = path.join(p, r)
    if path.exists(p):
        return p

    global summary
    summary.append(f'In file:{path.join(d, b)}.md, image={p}')

    return None

def process_markdown(s, t, depth):
    p = depth_print(depth)
    dn = path.dirname(s)
    bn = path.basename(s)
    bn_noext = bn[:bn.find('.')]
    tdn = path.dirname(t)
    i = []
    a = []
    with open(file=s, mode='r') as f:
        content = reduce(lambda a, b: a + b, f.readlines())
        f.close()
    for m in image_regex.finditer(content):
        l, r = m.span()
        s = m.group()[2:-1]
        m = s.find('](')
        comment = s[:m]
        img_rel_path = s[m+2:]
        img_path = preprocess_imgpath(img_rel_path, dn, bn_noext)
        if img_path is None:
            p(f'Image {img_rel_path} Invalid.')
            continue
        asset_path = path.join(bn_noext, img_rel_path)
        asset_path = path.join(tdn, asset_path)
        p(f"Img: {img_path}")
        p(f'Ass: {asset_path}')
        i.append(img_path)
        a.append(asset_path)
    return i, a








def depth_print(d):
    if d == 0:
        return print
    prefix = "-" * (2 * d - 1) + ">"
    def prefix_print(*args, **kwargs):
        print(prefix, *args, **kwargs)
    return prefix_print



def process(s, t, depth=0):
    if not path.exists(s):
        raise RuntimeError(f"{s} not exsits. stopping...")
    p = depth_print(depth)

    p(f"P[s: {s} t: {t}]", end='')
    if path.isdir(s):
        process_dir(s, t, depth + 1)
    elif path.isfile(s):
        process_file(s, t, depth + 1)
    else:
        raise RuntimeWarning(f"Will not process {s}, because it is not a dir nor a file.")
    p("E")

    
def process_dir(s, t, depth):
    if path.exists(t):
        print("dir exists.")
    else:
        print(f"mkdir {t}")
        if not dry_run:
            os.mkdir(t)
    sub = os.listdir(s)
    sub_t = [path.join(t, si) for si in sub]
    sub_s = [path.join(s, si) for si in sub]
    for si, ti in zip(sub_s, sub_t):
        process(si ,ti, depth)


def process_file(s, t, depth):
    if s.endswith('.md'):
        print("markdown")
    else:
        print("pass")
        return
    i, a = process_markdown(s, t, depth + 1)
    if dry_run:
        return
    copy_file(s, t)
    for f, t in zip(i, a):
        copy_file(f, t)


def copy_file(f, t):
    td = path.dirname(t)
    if not path.exists(td):
        Path(td).mkdir(parents=True)

    shutil.copy2(f, t)

    
        



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', type=str)
    parser.add_argument('-t', type=str)
    parser.add_argument('--dryrun', type=bool)
    args = parser.parse_args()
    source_dir = args.s
    target_dir = args.t
    dry_run = args.dryrun
    print(f"source-dir = {source_dir}")
    print(f"target-dir = {target_dir}")
    print(f'dryrun     = {dry_run}')
    

    process(source_dir, target_dir)

    print("Summary:")
    for s in summary:
        print(s)



