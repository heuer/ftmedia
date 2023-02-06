#!/usr/bin/env python3
import subprocess
import ftmedia

_MINI_MODELLE = {
    # issue   start page(s)
    '2013-4': [4],
    '2014-2': [18],
    '2014-3': [11, 12],
    '2014-4': [7, 8],
    '2015-1': [4],
    '2015-4': [4],
    '2016-1': [5, 14],
    '2016-2': [5, 13],
    '2016-3': [4],
    '2017-1': [8],
    '2017-3': [4],
    '2017-4': [4],
    '2018-1': [5],
    '2018-3': [7],
    '2018-4': [5],
    '2019-3': [4, 6],
    '2019-4': [4],
    '2020-1': [10],
    '2020-2': [4],
    '2020-4': [6],
    '2021-1': [5]
}

def minimodelle():
    for article in sorted(ftmedia.read_overview('artikeluebersicht.csv'), key=lambda x: x.issue):
        pages = _MINI_MODELLE.get(article.issue, ())
        if article.pages[0] not in pages:
            continue
        article.title = ftmedia.remove_minimodel_prefix(article.title)
        yield article


with open('ftpedia-minimodelle.tex', 'w') as f:
    f.write(ftmedia.make_latex_doc(minimodelle(), data_dir='./data/', title='Mini-Modelle'))


for i in range(3):
    subprocess.run(['lualatex', 'ftpedia-minimodelle.tex'])

subprocess.run(['gs', '-sDEVICE=pdfwrite', '-sPAPERSIZE=a5', '-dFIXEDMEDIA', '-dPDFFitPage',
                '-dPDFSETTINGS=/ebook', '-dCompatibilityLevel=1.4', '-oftpedia-mini.pdf', 'ftpedia-minimodelle.pdf'])