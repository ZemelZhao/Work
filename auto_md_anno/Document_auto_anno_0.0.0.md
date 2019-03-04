# Version 0.0.0
软件说明: 



本文档将按照各文件、文件夹顺序逐一叙述
__文件__
|No.|FileName|ClassNum|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[analy\_code.py](#1. analy\_code.py)|1|0||
|2|[auto\_anno.py](#2. auto\_anno.py)|0|0||
|3|[ver\_control.py](#3. ver\_control.py)|1|0||
|4|[write\_document.py](#4. write\_document.py)|1|0||
__文件夹__
|No.|DirName|FileNum|Note|
|:-:|:-:|:-:|:-:|
|1|[test\_dir](#5. test\_dir)|2||
|2|[test\_dir/hello](#6. test\_dir/hello)|2||
|3|[test\_dir/hello1](#7. test\_dir/hello1)|2||
## 1. analy\_code.py
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[AnalyCode](#1. AnalyCode)||15||
### 1. AnalyCode
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
|2|[filter\_doc\_useless\_line](#2. filter\_doc\_useless\_line)|1|True|0||
|3|[filter\_multiline\_anno](#3. filter\_multiline\_anno)|1|True|0||
|4|[filter\_oneline\_anno](#4. filter\_oneline\_anno)|1|True|0||
|5|[filter\_redun\_space](#5. filter\_redun\_space)|1|True|0||
|6|[find\_all\_element\_uncross](#6. find\_all\_element\_uncross)|2|True|0||
|7|[fix\_nonstandard\_line\_head](#7. fix\_nonstandard\_line\_head)|1|True|0||
|8|[get\_prog\_file\_system](#8. get\_prog\_file\_system)|0|True|0||
|9|[hash\_list](#9. hash\_list)|1|True|0||
|10|[hash\_system](#10. hash\_system)|1|True|0||
|11|[read\_class](#11. read\_class)|1|True|0||
|12|[read\_doc](#12. read\_doc)|1|True|0||
|13|[read\_files](#13. read\_files)|2|True|0||
|14|[read\_func](#14. read\_func)|1|True|0||
|15|[run](#15. run)|1|True|0||
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
## 3. ver\_control.py
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[VerControl](#1. VerControl)|object|1||
### 1. VerControl
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
## 4. write\_document.py
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[WriteDocument](#1. WriteDocument)|object|17||
### 1. WriteDocument
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
|2|[fix\_markdown\_str](#2. fix\_markdown\_str)|1|True|0||
|3|[make\_doc\_markdown](#3. make\_doc\_markdown)|1|False|0||
|4|[make\_section\_all](#4. make\_section\_all)|2|True|0||
|5|[make\_section\_class](#5. make\_section\_class)|4|True|0||
|6|[make\_section\_dir](#6. make\_section\_dir)|4|True|0||
|7|[make\_section\_flle](#7. make\_section\_flle)|4|True|0||
|8|[make\_section\_func](#8. make\_section\_func)|4|True|0||
|9|[make\_table\_arg\_intro](#9. make\_table\_arg\_intro)|1|True|0||
|10|[make\_table\_class\_intro](#10. make\_table\_class\_intro)|1|True|0||
|11|[make\_table\_decorator\_intro](#11. make\_table\_decorator\_intro)|1|True|0||
|12|[make\_table\_dir\_intro](#12. make\_table\_dir\_intro)|1|True|0||
|13|[make\_table\_file\_intro](#13. make\_table\_file\_intro)|1|True|0||
|14|[make\_table\_func\_intro](#14. make\_table\_func\_intro)|1|True|0||
|15|[make\_table\_introduce\_all](#15. make\_table\_introduce\_all)|1|True|0||
|16|[make\_table\_introduce\_file](#16. make\_table\_introduce\_file)|1|True|0||
|17|[run](#17. run)|2|False|0||
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
#### 4. make\_section\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|lv|||
__传出参数__
#### 5. make\_section\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 6. make\_section\_dir
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 7. make\_section\_flle
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 8. make\_section\_func
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
|2|name|||
|3|lv|||
|4|order|||
__传出参数__
#### 9. make\_table\_arg\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
#### 10. make\_table\_class\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 11. make\_table\_decorator\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|||
__传出参数__
#### 12. make\_table\_dir\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 13. make\_table\_file\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 14. make\_table\_func\_intro
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 15. make\_table\_introduce\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 16. make\_table\_introduce\_file
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|||
__传出参数__
#### 17. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|||
|2|version|||
## 5. test\_dir
### 1. hello.py
__函数__
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[bread](#1. bread)|1|True|0||
|2|[here](#2. here)|5|False|0||
|3|[here\_s\_sf](#3. here\_s\_sf)|0|True|1||
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[A](#4. A)|object|1||
|2|[HAHA](#5. HAHA)|mp.Process|3||
#### 1. bread
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|func|||
__传出参数__
#### 2. here
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|fucds|||
|2|s\_s|||
|3|sfs|||
|4|dsfskl|||
|5|sfdsf|||
#### 3. here\_s\_sf
__修饰器__
|No.|DecoratorName|Note|
|:-:|:-:|:-:|
|1|bread||
__传出参数__
#### 4. A
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
#### 5. HAHA
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
|2|[ha1](#2. ha1)|0|False|1||
|3|[initUI](#3. initUI)|1|False|0||
##### 2. ha1
__修饰器__
|No.|DecoratorName|Note|
|:-:|:-:|:-:|
|1|bread||
##### 3. initUI
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|fuck|||
### 1. hello1.py
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[WindowGraphShow](#1. WindowGraphShow)|QWidget|5||
#### 1. WindowGraphShow
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0||
|2|[closeEvent](#2. closeEvent)|1|False|1||
|3|[initUI](#3. initUI)|0|False|1||
|4|[isClosed](#4. isClosed)|0|True|1||
|5|show|0|False|0||
##### 2. closeEvent
__修饰器__
|No.|DecoratorName|Note|
|:-:|:-:|:-:|
|1|pyqtSignal||
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|e|||
##### 3. initUI
__修饰器__
|No.|DecoratorName|Note|
|:-:|:-:|:-:|
|1|pyqtSignal||
##### 4. isClosed
__修饰器__
|No.|DecoratorName|Note|
|:-:|:-:|:-:|
|1|pyqtSignal||
__传出参数__
## 6. test\_dir/hello
## 7. test\_dir/hello1
### 1. hello1\_1.py
### 1. hello1\_2.py
__函数__
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[main](#1. main)|0|True|0||
__类__
|No.|ClassName|SuperClass|FuncNum|Note|
|:-:|:-:|:-:|:-:|:-:|
|1|[A](#2. A)|object|2||
#### 1. main
__传出参数__
#### 2. A
|No.|FuncName|InputNum|OutputBool|DecorNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[\_\_init\_\_](#1. \_\_init\_\_)|1|False|0||
|2|[run](#2. run)|1|False|0||
##### 1. \_\_init\_\_
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|fuck|||
##### 2. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|haha|||
