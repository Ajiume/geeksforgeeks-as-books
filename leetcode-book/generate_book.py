"""
generate a book
"""

import sys
from subprocess import call
import glob

from clean import clean_html_files
from generate_covers import generate_cover


def generate(book, version):
    print "cleaning html files,", "this might take a while..."
    # clean_html_files(book)
    cleaned_html = sorted(glob.glob(book + "*_cleaned.html"))
    md_file = book + book[:-1] + version + ".md"
    html_file = book + book[:-1] + version + ".html"
    epub_file = book + book[:-1] + version + ".epub"
    cover_image = "covers/" + book[:-1] + ".png"
    print "generating", html_file, "..."
    # call("cat " + "../bookcopyright/leetcode_copyright.html " + " ".join(cleaned_html) + " > " + html_file, shell=True)
    generate_cover(book[:-1], version[1:])
    print "generating", epub_file, "this might take a while..."
    call(['pandoc', '-o', epub_file, html_file,
        '--epub-metadata='+book+'metadata.xml', "--toc", "--toc-depth=2", "--epub-stylesheet=../styles/leetcode.css", "-f", "html-native_divs"])
    print "generating", book + version + book[:-1] + ".mobi", "..."
    call(['kindlegen', epub_file])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "this program takes two arguments"
        sys.exit()
    book = sys.argv[1]
    version = sys.argv[2]
    if book[-1] != "/":
        book = book + "/"
    version = "_" + version
    generate(book, version)
