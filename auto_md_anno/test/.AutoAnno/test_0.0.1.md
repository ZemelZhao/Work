# Version 0.0.1
软件说明: 
- 999 Lines

本文档将按照各文件、文件夹顺序逐一叙述
__文件__

|No.|FileName|ClassNum|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[analy\_code.py](#1. analy\_code.py)|1|0|386||
|2|[auto\_anno.py](#2. auto\_anno.py)|0|0|47||
|3|[check\_code.py](#3. check\_code.py)|1|0|190||
|4|[hash\_std.py](#4. hash\_std.py)|1|0|10||
|5|[ver\_control.py](#5. ver\_control.py)|1|0|31||
|6|[write\_document.py](#6. write\_document.py)|2|0|335||
__文件夹__

## 1. analy\_code.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[AnalyCode](#1. AnalyCode)||15|374||
### 1. AnalyCode
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|4||
|2|[filter\_doc\_useless\_line](#2. filter\_doc\_useless\_line)|1|True|0|7||
|3|[filter\_multiline\_anno](#3. filter\_multiline\_anno)|1|True|0|62||
|4|[filter\_oneline\_anno](#4. filter\_oneline\_anno)|1|True|0|42||
|5|[filter\_redun\_space](#5. filter\_redun\_space)|1|True|0|18||
|6|[find\_all\_element\_uncross](#6. find\_all\_element\_uncross)|2|True|0|14||
|7|[fix\_nonstandard\_line\_head](#7. fix\_nonstandard\_line\_head)|1|True|0|14||
|8|[get\_prog\_file\_system](#8. get\_prog\_file\_system)|0|True|0|19||
|9|[hash\_list](#9. hash\_list)|1|True|0|5||
|10|[hash\_system](#10. hash\_system)|1|True|0|21||
|11|[read\_class](#11. read\_class)|1|True|0|46||
|12|[read\_doc](#12. read\_doc)|1|True|0|58||
|13|[read\_files](#13. read\_files)|2|True|0|10||
|14|[read\_func](#14. read\_func)|1|True|0|39||
|15|[run](#15. run)|1|True|0|14||
#### 2. filter\_doc\_useless\_line
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_code\_data|||
__传出参数__
#### 3. filter\_multiline\_anno
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|||
__传出参数__
#### 4. filter\_oneline\_anno
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|||
__传出参数__
#### 5. filter\_redun\_space
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|||
__传出参数__
#### 6. find\_all\_element\_uncross
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache|||
|2|data|||
__传出参数__
#### 7. fix\_nonstandard\_line\_head
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|||
__传出参数__
#### 8. get\_prog\_file\_system
__传出参数__
#### 9. hash\_list
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache|||
__传出参数__
#### 10. hash\_system
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 11. read\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
__传出参数__
#### 12. read\_doc
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|address|||
__传出参数__
#### 13. read\_files
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|list\_file|||
|2|dir\_name|||
__传出参数__
#### 14. read\_func
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
__传出参数__
#### 15. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|address|||
__传出参数__
## 2. auto\_anno.py
## 3. check\_code.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[CodeCheck](#1. CodeCheck)|object|8|176||
### 1. CodeCheck
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|3||
|2|[check\_all](#2. check\_all)|2|True|0|19||
|3|[check\_class](#3. check\_class)|2|True|0|24||
|4|[check\_dirs](#4. check\_dirs)|2|True|0|32||
|5|[check\_file](#5. check\_file)|2|True|0|60||
|6|[check\_files](#6. check\_files)|2|True|0|32||
|7|create\_special\_hash\_code|0|False|0|2||
|8|[run](#8. run)|2|True|0|3||
#### 2. check\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
#### 3. check\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
#### 4. check\_dirs
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
#### 5. check\_file
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
#### 6. check\_files
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
#### 8. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|||
|2|dic\_old|||
__传出参数__
## 4. hash\_std.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[HashStd](#1. HashStd)|object|2|6||
### 1. HashStd
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[\_\_init\_\_](#1. \_\_init\_\_)|1|False|0|3||
|2|[hash](#2. hash)|1|True|0|2||
#### 1. \_\_init\_\_
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|htype|||
#### 2. hash
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
__传出参数__
## 5. ver\_control.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[VerControl](#1. VerControl)|object|4|28||
### 1. VerControl
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|2||
|2|[get\_lastest\_version](#2. get\_lastest\_version)|1|True|0|7||
|3|[get\_new\_version](#3. get\_new\_version)|2|True|0|12||
|4|[run](#4. run)|1|True|0|6||
#### 2. get\_lastest\_version
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
#### 3. get\_new\_version
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
|2|ltype|||
__传出参数__
#### 4. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
## 6. write\_document.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[WriteDocument](#1. WriteDocument)|object|18|248||
|2|[WriteUpdate](#2. WriteUpdate)|object|7|80||
### 1. WriteDocument
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|2||
|2|[fix\_markdown\_str](#2. fix\_markdown\_str)|1|True|0|8||
|3|[make\_doc\_markdown](#3. make\_doc\_markdown)|1|False|0|13||
|4|[make\_markdown\_link](#4. make\_markdown\_link)|3|True|0|4||
|5|[make\_section\_all](#5. make\_section\_all)|2|True|0|8||
|6|[make\_section\_class](#6. make\_section\_class)|4|True|0|11||
|7|[make\_section\_dir](#7. make\_section\_dir)|4|True|0|9||
|8|[make\_section\_flle](#8. make\_section\_flle)|4|True|0|16||
|9|[make\_section\_func](#9. make\_section\_func)|4|True|0|16||
|10|[make\_table\_arg\_intro](#10. make\_table\_arg\_intro)|1|True|0|17||
|11|[make\_table\_class\_intro](#11. make\_table\_class\_intro)|2|True|0|23||
|12|[make\_table\_decorator\_intro](#12. make\_table\_decorator\_intro)|1|True|0|16||
|13|[make\_table\_dir\_intro](#13. make\_table\_dir\_intro)|2|True|0|19||
|14|[make\_table\_file\_intro](#14. make\_table\_file\_intro)|2|True|0|20||
|15|[make\_table\_func\_intro](#15. make\_table\_func\_intro)|2|True|0|25||
|16|[make\_table\_introduce\_all](#16. make\_table\_introduce\_all)|1|True|0|17||
|17|[make\_table\_introduce\_file](#17. make\_table\_introduce\_file)|1|True|0|17||
|18|[run](#18. run)|2|True|0|6||
#### 2. fix\_markdown\_str
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
__传出参数__
#### 3. make\_doc\_markdown
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
#### 4. make\_markdown\_link
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
|2|order|||
|3|name\_type|||
__传出参数__
#### 5. make\_section\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|lv|||
__传出参数__
#### 6. make\_section\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 7. make\_section\_dir
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 8. make\_section\_flle
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 9. make\_section\_func
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 10. make\_table\_arg\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
#### 11. make\_table\_class\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|order|||
__传出参数__
#### 12. make\_table\_decorator\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
#### 13. make\_table\_dir\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|order|||
__传出参数__
#### 14. make\_table\_file\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|order|||
__传出参数__
#### 15. make\_table\_func\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|order|||
__传出参数__
#### 16. make\_table\_introduce\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 17. make\_table\_introduce\_file
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 18. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
|2|version|||
__传出参数__
### 2. WriteUpdate
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|2||
|2|[fix\_markdown\_str](#2. fix\_markdown\_str)|1|True|0|8||
|3|[make\_section\_dirs](#3. make\_section\_dirs)|1|True|0|8||
|4|[make\_section\_file](#4. make\_section\_file)|5|True|0|25||
|5|[make\_section\_files](#5. make\_section\_files)|2|True|0|8||
|6|[make\_update\_markdown](#6. make\_update\_markdown)|1|True|0|24||
|7|[run](#7. run)|2|True|0|4||
#### 2. fix\_markdown\_str
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
__传出参数__
#### 3. make\_section\_dirs
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 4. make\_section\_file
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
|5|utype|||
__传出参数__
#### 5. make\_section\_files
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|lv|||
__传出参数__
#### 6. make\_update\_markdown
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 7. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
|2|version|||
__传出参数__
