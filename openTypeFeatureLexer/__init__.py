from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import *

_featureKwlist = ["Ascender", "Attach", "CapHeight", "CaretOffset", "CodePageRange",
            "Descender", "FontRevision", "GlyphClassDef", "HorizAxis.BaseScriptList",
            "HorizAxis.BaseTagList", "HorizAxis.MinMax", "IgnoreBaseGlyphs", "IgnoreLigatures",
            "IgnoreMarks", "LigatureCaretByDev", "LigatureCaretByIndex", "LigatureCaretByPos",
            "LineGap", "MarkAttachClass", "MarkAttachmentType", "NULL", "Panose", "RightToLeft",
            "TypoAscender", "TypoDescender", "TypoLineGap", "UnicodeRange", "UseMarkFilteringSet",
            "Vendor", "VertAdvanceY", "VertAxis.BaseScriptList", "VertAxis.BaseTagList",
            "VertAxis.MinMax", "VertOriginY", "VertTypoAscender", "VertTypoDescender",
            "VertTypoLineGap", "XHeight", "anchorDef", "anchor", "anonymous", "anon",
            "by", "contour", "cursive", "device", "enumerate", "enum", "exclude_dflt",
            "featureNames", "feature", "from", "ignore", "include_dflt", "include",
            "languagesystem", "language", "lookupflag", "lookup", "markClass", "mark",
            "nameid", "name", "parameters", "position", "pos", "required", "reversesub",
            "rsub", "script", "sizemenuname", "substitute", "subtable", "sub", "table",
            "useExtension", "valueRecordDef", "winAscent", "winDescent"]

class OpenTypeFeatureLexer(RegexLexer):

    name = "Feature"
    aliases = ['feature', 'fea']
    filenames = ['*.fea']

    tokens = {
            'root': [
                (r'\n', Text),
                (r'#.*$', Comment),
                (r'(anonymous|anon|feature|lookup|table)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Text), 'featurename'),
                (r'(\})((?:\s|\\\s)*)((?:\s|\\\s)*)', bygroups(Punctuation, Text), 'featurename'),
                (r'\[|\]|\{|\}|\:|\(|\)|\.|\,|\;|\\|\-|\=|\%|\*|\/|\<|\>', Punctuation),
                (r'\'', Name.Tag),
                (r'(@[a-zA-Z0-9_.]*)', Name.Function),
                (r'(include)()', Keyword, 'includepath'),
                (r'"|\'+', String, 'string'),
                include('keywords'),
                include('numbers'),
                include('whitespace'),
                (r'[a-zA-Z_][a-zA-Z0-9_.]*', Name),
            ],
            'keywords': [
                        (r'(%s)\b' % ("|".join(_featureKwlist)), Keyword),
            ],
            'numbers': [
                        (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?', Number.Float),
                        (r'\d+[eE][+-]?[0-9]+j?', Number.Float),
                        (r'0[0-7]+j?', Number.Oct),
                        (r'0[xX][a-fA-F0-9]+', Number.Hex),
                        (r'\d+L', Number.Integer.Long),
                        (r'\d+j?', Number.Integer)
                    ],
            'featurename': [
                        (r'\s*[a-zA-Z_][a-zA-Z0-9_]+', Name.Class, '#pop'),
                    ],
            'includepath' : [
                        (r'\(', Punctuation),
                        (r'(?s)(\\\\|\\[0-7]+|\\.|[^)])', String.Other),
                        (r'\)\s*;', Punctuation, '#pop'),
                    ],
            'string': [
                        (r'(?s)(\\\\|\\[0-7]+|\\.|[^"\'\\])', String),
                        (r'"|\'', String, '#pop')
                    ],
            'whitespace': [
                        (r'\s+', Text),
                    ],
        }
