# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import common
import content

OUT = os.path.join(os.path.dirname(__file__), "..")


def write(path, text):
    full = os.path.join(OUT, path)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", full, len(text), "bytes")


def main():
    write("index.html", common.build_index())
    for unit_id, _title, _sub, _cat, _desc, _tags in common.UNITS:
        body = content.BODIES[unit_id]()
        write(f"{unit_id}.html", common.page(unit_id, body))


if __name__ == "__main__":
    main()
