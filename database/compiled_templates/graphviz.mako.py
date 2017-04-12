# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491898254.744403
_enable_loop = True
_template_filename = 'config/plugins/visualizations/graphviz/templates/graphviz.mako'
_template_uri = 'graphviz.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        visualization_name = context.get('visualization_name', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE HTML>\n<html>\n<head>\n\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">\n\n    <title>')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u' | ')
        __M_writer(unicode(visualization_name))
        __M_writer(u'</title>\n    ')

        root = h.url_for( '/' )
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['root'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n    <script type="text/javascript" src="/static/scripts/libs/jquery/jquery.js"></script>\n\n    ')
        __M_writer(unicode(h.stylesheet_link( root + 'plugins/visualizations/graphviz/static/css/style.css' )))
        __M_writer(u'\n\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/jquery.qtip.js' )))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/cytoscape.min.js' )))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/collapse.js' )))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/toolPanelFunctions.js' )))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/graphVis.js' )))
        __M_writer(u'\n\n</head>\n\n')
        __M_writer(u'<body>\n    ')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/graphviz/static/js/wz_tooltip.js' )))
        __M_writer(u"\n\n    <script>\n        function parseNodeEdge( data ){\n            data = data.data[0];\n            parseJson( data );\n        }\n\n        $(document).ready(function() {\n\n            var hdaName = '")
        __M_writer(filters.html_escape(unicode( hda.name )))
        __M_writer(u"',\n                hdaId = '")
        __M_writer(unicode(trans.security.encode_id( hda.id )))
        __M_writer(u"',\n                hdaExt = '")
        __M_writer(unicode(hda.ext))
        __M_writer(u"',\n                rawUrl = '")
        __M_writer(unicode(h.url_for( controller="/datasets", action="index" )))
        __M_writer(u"',\n                apiUrl = '")
        __M_writer(unicode(h.url_for( "/" ) + "api/datasets"))
        __M_writer(u'\',\n                dataUrl;\n\n            function errorHandler( xhr, status, message ){\n                console.error(x, s, m);\n                alert("error loading data:\\n" + m);\n            }\n\n            switch( hdaExt ){\n                case \'txt\':\n                    dataUrl = rawUrl + \'/\' + hdaId + \'/display?to_ext=txt\';\n                    $.ajax(dataUrl, {\n                        dataType    : \'text\',\n                        success     : parseTextMatrix,\n                        error       : errorHandler\n                    });\n                    break;\n\n                case \'json\':\n                    dataUrl = rawUrl + \'/\' + hdaId + \'/display?to_ext=json\';\n                    $.ajax(dataUrl, {\n                        dataType    : \'json\',\n                        success     : parseJson,\n                        error       : errorHandler\n                    });\n                    break;\n\n                default:\n                    dataUrl = apiUrl + \'/\' + hdaId;\n                    $.ajax(dataUrl, {\n                        dataType    : \'json\',\n                        success     : parseNodeEdge,\n                        error       : errorHandler,\n                        data : {\n                            data_type : \'raw_data\',\n                            provider  : \'node-edge\'\n                        }\n                    });\n            }\n        });\n\n    </script>\n    <div id="cy"></div>\n\n    <!-- left control panel for rendering controls, hiding nodes, etc. - initially hidden -->\n    <div class="panel">\n        <br>\n        <div id="mainselection">\n            <select name="select" id="selectShape">\n                <option value="random" selected>Choose the shape</option>\n                <option value="random">random</option>\n                <option value="circle">circle</option>\n                <option value="grid">grid</option>\n                <option value="concentric">concentric</option>\n                <option value="breadthfirst">breadthfirst</option>\n            </select>\n        </div>\n        <br>\n\n        <input type="checkbox" class="css-checkbox" name="nlabelSelection" id="nodeLabelCheck" />\n        <label for="nodeLabelCheck" name="nodeLabelCheck" class="css-label">\n            show node label\n        </label>\n        <br>\n        <br>\n\n        <input type="checkbox" class="css-checkbox" name="elabelSelection" id="linkLabelCheck" />\n        <label for="linkLabelCheck" name="nodeLabelCheck" class="css-label">\n            show edge label\n        </label>\n        <br>\n        <br>\n\n        <input type="checkbox" class="css-checkbox" name="showOutgoing" id="showOutNode">\n        <label for="showOutNode" name="nodeLabelCheck" class="css-label">\n            highlight outgoing nodes\n        </label>\n        <br>\n        <br>\n\n        <input type="checkbox" class="css-checkbox" name="showInComing" id="showInNode">\n        <label for="showInNode" name="nodeLabelCheck" class="css-label">\n            highlight incoming nodes\n        </label>\n        <br>\n        <br>\n\n        <input type="checkbox" class="css-checkbox" name="showCollapsedNodeNum" id="collapseCount">\n        <label for="collapseCount" name="nodeLabelCheck" class="css-label">\n            show the number of collapsed nodes\n        </label>\n        <br>\n        <br>\n\n        <input type="button" class="btn colNode" name="collapseNode" id="collapseNode" value="Collapse Selected Node " onclick="colNode()" disabled="disabled">\n        <br>\n        <br>\n\n        <input type="button" class="btn expNode" name="expandNode" id="expandNode" value="Expand Selected Node " disabled="disabled">\n        <br>\n        <br>\n\n        <input type="button" class="btn delNode" name="deleteNodes" id="deleteNodes" value="Delete Selected Nodes " onclick="deleteSelectedNodes()" disabled="disabled">\n        <br>\n        <br>\n\n        <input type="button" class="btn" name="restoreNodes" id="restoreNodes" value="Restore Deleted Nodes" onclick="restoreDeletedNodes()">\n        <br>\n        <br>\n        <input type="button" class="btn" name="restore" id="restore" value="Restore The Structure  " onclick="restorGraphStructure()">\n        <br>\n        <br>\n        <input type="button" class="btn" name="export" id="export" value="Export PNG" onclick="exportFunction()">\n        <br>\n        <br>\n        <input type="button" class="btn" name="manual" id="manual" value="More Info" onclick="window.open(\'https://github.com/eteriSokhoyan/GraphVis\')">\n        <br>\n        <br>\n    </div>\n    <!-- button to show above panel -->\n    <a href="javascript:void(0);" class="slider-arrow show">&raquo;</a>\n\n    <!-- right control panel for displaying node data - initially hidden -->\n    <div id="nodeInfoDiv" class="nodePanel">\n        <p> <strong>Node Description </strong></p>\n        <br><br>\n        <p> Please select a node </p>\n    </div>\n    <!-- button to show above panel -->\n    <a href="javascript:void(0);" class="slider-arrow-forNode show">&laquo;</a>\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "25": 1, "26": 8, "27": 8, "28": 8, "29": 8, "30": 9, "36": 11, "37": 15, "38": 15, "39": 17, "40": 17, "41": 18, "42": 18, "43": 19, "44": 19, "45": 20, "46": 20, "47": 21, "48": 21, "49": 26, "50": 27, "51": 27, "52": 37, "53": 37, "54": 38, "55": 38, "56": 39, "57": 39, "58": 40, "59": 40, "60": 41, "61": 41, "67": 61}, "uri": "graphviz.mako", "filename": "config/plugins/visualizations/graphviz/templates/graphviz.mako"}
__M_END_METADATA
"""
