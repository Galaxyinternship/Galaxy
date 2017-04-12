# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491895483.679398
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/run.mako'
_template_uri = 'workflow/run.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        workflow_dict = context.get('workflow_dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(h.js("libs/bibtex", "libs/jquery/jquery-ui")))
        __M_writer(u'\n')
        __M_writer(unicode(h.css('jquery-ui/smoothness/jquery-ui')))
        __M_writer(u"\n<script>\n    require(['mvc/tool/tool-form-composite'], function( ToolForm ) {\n        $(function() {\n            var form = new ToolForm.View(")
        __M_writer(unicode( h.dumps( workflow_dict ) ))
        __M_writer(u');\n        });\n    });\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"34": 1, "35": 2, "36": 2, "37": 3, "38": 3, "39": 7, "40": 7, "46": 40, "27": 0}, "uri": "workflow/run.mako", "filename": "templates/webapps/galaxy/workflow/run.mako"}
__M_END_METADATA
"""
