#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdfkit
from django.core.files.storage import get_storage_class
from django.conf import settings

try:
    from StringIO import StringIO
except ImportError:
    from cStringIO import StringIO

render_pdf_option = getattr(settings, "RENDER_PDF", {})

options = {
    'page-size': render_pdf_option.get('page-size', 'A4'),
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
    # 'dpi': 220,
    'background': None,
    'encoding': "UTF-8",
    'print-media-type': None,
    'disable-smart-shrinking': None,
    'zoom': 3.0,
    'orientation': 'Portrait',
    'cache-dir': '/tmp/pdf',
    # 'window-status': 'ready_to_print',
    'javascript-delay': 1000,
    # 'disable-javascript': None,
    # 'custom-header' : [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'no-outline': None
}


class RenderPDF(object):

    def __init__(self, *args, **kwargs):
        self.options = options
        storage = get_storage_class()
        self.s = storage()

    def _save_to_file(self, content, filename):
        _filename = filename
        output = StringIO()
        output.write(content)
        self.s.save(name=_filename, content=output)
        output.close()
        return _filename

    def html2pdf_from_string(self, string_list, filename):

        if type(string_list) is not list:
            raise Exception("please input string list")

        _string = ''.join(string_list)
        out_pdf = pdfkit.from_string(_string, False, options=self.options)
        return self._save_to_file(content=out_pdf,
                                  filename=filename)


if __name__ == "__main__":
    render = RenderPDF()



