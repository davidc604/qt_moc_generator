#!/usr/bin/env python
#
# qt_moc_generator.py
#
# This script takes the header files and uses the Qt MOC to generate the Meta-Object source.
# The output files will be named: {header file name}.moc.cc
#
# Copyright (c) David Chen, 2017

import argparse
import os.path
import subprocess
import sys


def StripHeaderExtension(filename):
    if not filename.endswith(".h"):
        raise RuntimeError("Invalid header extension: "
                           "{0} .".format(filename))
    return filename.rsplit(".", 1)[0]


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--header-in-dir",
                        help="Base directory with source protos.")
    parser.add_argument("--cc-out-dir",
                        help="Output directory for generated moc files.")

    parser.add_argument("headers", nargs="+",
                        help="Input header file(s).")

    options = parser.parse_args()

    moc_dir = os.path.relpath(options.header_in_dir)
    cc_out_dir = options.cc_out_dir
    headers = options.headers

    for header in headers:
        stripped_name = StripHeaderExtension(header)
        output_cc = os.path.join(cc_out_dir, stripped_name) + ".moc.cc"

        ret = subprocess.call(["moc", os.path.join(moc_dir, header), "-o", output_cc])
        if ret != 0:
            raise RuntimeError("Moc has returned non-zero status: "
                               "{0} .".format(ret))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except RuntimeError as e:
        sys.exit(1)
