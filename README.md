# py-regexwebparser

Created for @fhooe by Marcel Skumantz

## Why?
Please go ask @fhooe 

## Usage
- `open(path)` opens a string as a dom node and returns that node
- `open_url(path, encoding='utf-8'` opens an url as a dom node and returns that node
- `node.find_child_tags(tag)` returns a list of children with the provided tag in the content
- `node.find_child_tags_by_pattern(tag, pattern)`  returns a list of children with the provided tag in the content and matches their content against the provided pattern
- `node.attr` returns a dictionary of attributes
- `node.content` returns the content of the tag
- `node.type` retuns the type of the tag (div, p, etc...)
## Example

```python
import RegexWebParser as rwp
root = rwp.open_url('https://en.wikipedia.org/wiki/Python_(programming_language)')
captions = root.find_children("caption")
for caption in captions:
    print(caption)
```


