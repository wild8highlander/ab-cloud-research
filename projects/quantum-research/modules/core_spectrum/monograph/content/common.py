# -*- coding: utf-8 -*-
"""monograph/content/common.py — общие хелперы серии."""


def _meta(title, subtitle, vol, author, affil, series, date):
    return dict(title=title, subtitle=subtitle, author=author, affil=affil,
                series=series, volume=vol, version='1.2.0', date=date)
