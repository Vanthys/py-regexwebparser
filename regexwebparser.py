'''
Title: RegexWebparser
Author: @Vanthys
Date: 05.02.2024
Version 1.0
Desc:   
    Uses regex to match html
'''

from urllib.request import urlopen
import re

class RegexWebParser():

    @staticmethod
    def open_url(url="", encoding="utf-8"):
        return __class__.Tag(type="document", content=urlopen(url).read().decode(encoding))
    @staticmethod
    def open(content=""):
        return __class__.Tag(type="dtring", content=content)
    
    @staticmethod
    def __parse_attr(attributes) -> {}:
        rs = {}
        pattern = r'\s*(.*?)(?==)=\"(.*?)(?=\")\"'
        match = re.findall(pattern, attributes)
        for att in match:
            rs[att[0]] = att[1]
        return rs

    @staticmethod
    def find_tags(tag_name, source) -> []:
        result = []
        pattern = r'<({})((?:.|\n)*?)(?=>)>((?:.|\n)*?)(?=</(?:\1)>)</\1>'.format(re.escape(tag_name))
        matches = re.findall(pattern, source)
        if matches:
            for match in matches:
                tag = match[0]
                attr = __class__.__parse_attr(match[1])
                cnt = match[2]
                result.append(__class__.Tag(tag, attr, cnt))
        return result
    
    @staticmethod
    def find_in_list(list, search_pattern) -> []:
        return [d for d in list if re.search(search_pattern, d.content)]

    @staticmethod
    def find_tags_by_pattern(tag, pattern, source) -> []:
        return __class__.find_in_list(__class__.find_tags(tag, source), pattern)

    class Tag():
        def __init__(self, type="", attr=[], content = ""):
            self.type = type
            self.attr = attr
            self.content = content


        def find_child_tags_by_pattern(self, tag, pattern) -> []:
            return RegexWebParser.find_in_list(RegexWebParser.find_tags(tag, self.content), pattern)


        def find_child_tags(self, type) -> []:
            return RegexWebParser.find_tags(type, self.content)

        def evaluate_content(self):
            raise NotImplemented("Ups")

        def __str__(self) -> str:
            return f"<{self.type}{':'.join(self.attr) if len(self.attr) > 0 else ''}>\"{self.content}\""
        
        def __repr__(self) -> str:
            return f"<{self.type}{':'.join(self.attr) if len(self.attr) > 0 else ''}>\"{self.content}\""
        



