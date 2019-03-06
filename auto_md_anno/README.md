# Version 0.0.1
软件说明: 
- 999 Lines
- 希望能够搭建一个方便的文档书写框架 其中适应两级文件的python软件的文档

- 可以给出包含的文件、文件夹
- 各级文件下包含的类、类内函数和全局函数
- 可以通过检查哈希值判断类内函数等是否修改、新增或被删除
- 待改进部分：
  - 多分支版本控制
  - 文档未修改部分能够照抄上一版本文档
  - 需要重新修改代码 需使用正则表达式
  - 增加图形界面
  - 生成为可执行文件
  - 是否需要显示所占行数
  - 修改bug
    - 所有的数据均在内存上 之后可以优化到硬盘上 多次读写
    - 改变文件、文件夹名称 不会引起哈希值变化

本文档将按照各文件、文件夹顺序逐一叙述
__文件__

|No.|FileName|ClassNum|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[analy\_code.py](#1. analy\_code.py)|1|0|386|分析代码|
|2|[auto\_anno.py](#2. auto\_anno.py)|0|0|47|入口程序|
|3|[check\_code.py](#3. check\_code.py)|1|0|190|检查各版本的变更|
|4|[hash\_std.py](#4. hash\_std.py)|1|0|10|定义产生哈希值的哈希函数|
|5|[ver\_control.py](#5. ver\_control.py)|1|0|31|版本控制 现在仅支持单线升级|
|6|[write\_document.py](#6. write\_document.py)|2|0|335|生成文档及升级日志|
__文件夹__

## 1. analy\_code.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[AnalyCode](#1. AnalyCode)|object|15|374|分析代码类|
### 1. AnalyCode
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|4|类初始化|
|2|[filter\_doc\_useless\_line](#2. filter\_doc\_useless\_line)|1|True|0|7|去除多余行|
|3|[filter\_multiline\_anno](#3. filter\_multiline\_anno)|1|True|0|62|去除多行注释|
|4|[filter\_oneline\_anno](#4. filter\_oneline\_anno)|1|True|0|42|去除单行注释|
|5|[filter\_redun\_space](#5. filter\_redun\_space)|1|True|0|18|去除每行多余空格和制表符|
|6|[find\_all\_element\_uncross](#6. find\_all\_element\_uncross)|2|True|0|14|计数字符串中有多少个指定字符|
|7|[fix\_nonstandard\_line\_head](#7. fix\_nonstandard\_line\_head)|1|True|0|14|去除每行头部的制表符 改为空格|
|8|[get\_prog\_file\_system](#8. get\_prog\_file\_system)|0|True|0|19|索引完整目标软件文件系统|
|9|[hash\_list](#9. hash\_list)|1|True|0|5|对某个列表进行指定哈希计算|
|10|[hash\_system](#10. hash\_system)|1|True|0|21|对某个字典进行指定哈希计算|
|11|[read\_class](#11. read\_class)|1|True|0|46|完成类索引字典|
|12|[read\_doc](#12. read\_doc)|1|True|0|58|完成文档索引字典|
|13|[read\_files](#13. read\_files)|2|True|0|10|完成文件夹索引字典|
|14|[read\_func](#14. read\_func)|1|True|0|39|完成函数索引字典|
|15|[run](#15. run)|1|True|0|14|运行类|
#### 2. filter\_doc\_useless\_line
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_code\_data|list(str)|列表中所有元素都是字符串|
__传出参数__

#### 3. filter\_multiline\_anno
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|list(str)||
__传出参数__
#### 4. filter\_oneline\_anno
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|list(str)||
__传出参数__
#### 5. filter\_redun\_space
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|list(str)||
__传出参数__
#### 6. find\_all\_element\_uncross
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache|str|需要索引的字符串|
|2|data|str|需要计数的字符串|
__传出参数__

传出的字符串的个数是不交叉的统计 如 ”######“ 中有2个 ”###“， 而不是4个

#### 7. fix\_nonstandard\_line\_head
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data\_code\_temp|list(str)||
__传出参数__
#### 8. get\_prog\_file\_system
__传出参数__
#### 9. hash\_list
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache|list(str)||
__传出参数__
#### 10. hash\_system
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic|dict|必须是文档索引字典以上的字典|
__传出参数__
#### 11. read\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|list(str)||
__传出参数__
#### 12. read\_doc
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|address|str|文档地址|
__传出参数__
#### 13. read\_files
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|list\_file|list(str)|多个文档列表|
|2|dir\_name|str|文档所在文件夹|
__传出参数__
#### 14. read\_func
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data|list(str)||
__传出参数__
#### 15. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|address|str|总体软件地址|
__传出参数__
## 2. auto\_anno.py
## 3. check\_code.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[CodeCheck](#1. CodeCheck)|object|8|176|检查程序是否改动|
### 1. CodeCheck
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|3|类初始化|
|2|[check\_all](#2. check\_all)|2|True|0|19|检查总体软件|
|3|[check\_class](#3. check\_class)|2|True|0|24|检查单个类|
|4|[check\_dirs](#4. check\_dirs)|2|True|0|32|检查各个文件夹|
|5|[check\_file](#5. check\_file)|2|True|0|60|检查单个文件|
|6|[check\_files](#6. check\_files)|2|True|0|32|检查一级文件夹|
|7|create\_special\_hash\_code|0|False|0|2|创建一些奇特的哈希值|
|8|[run](#8. run)|2|True|0|3|运行类|
#### 2. check\_all
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict|新版本索引字典|
|2|dic\_old|dict|旧版本索引字典|
__传出参数__
#### 3. check\_class
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict||
|2|dic\_old|dict||
__传出参数__
#### 4. check\_dirs
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict||
|2|dic\_old|dict||
__传出参数__
#### 5. check\_file
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict||
|2|dic\_old|dict||
__传出参数__
#### 6. check\_files
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict||
|2|dic\_old|dict||
__传出参数__
#### 8. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|dic\_new|dict||
|2|dic\_old|dict||
__传出参数__

返回改变地方的索引字典

## 4. hash\_std.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[HashStd](#1. HashStd)|object|2|6|调整软件使用的哈希算法|
### 1. HashStd
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[\_\_init\_\_](#1. \_\_init\_\_)|1|False|0|3|类初始化 调整哈希算法|
|2|[hash](#2. hash)|1|True|0|2|对字符串等hashable的变量进行哈希计算|
#### 1. \_\_init\_\_
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|htype|int|默认为1|

|  0   |  1   |   2    |   3    |   4    |   5    |
| :--: | :--: | :----: | :----: | :----: | :----: |
| md5  | sha1 | sha224 | sha256 | sha384 | sha512 |

#### 2. hash
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|data||任何可哈希变量|
__传出参数__

传出为哈希值的16进制显示字符串

## 5. ver\_control.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[VerControl](#1. VerControl)|object|4|28|版本控制类|
### 1. VerControl
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|2|出事类|
|2|[get\_lastest\_version](#2. get\_lastest\_version)|1|True|0|7|获取之前最新版本|
|3|[get\_new\_version](#3. get\_new\_version)|2|True|0|12|获取更新版本|
|4|[run](#4. run)|1|True|0|6|运行类|
#### 2. get\_lastest\_version
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|list(str)|os.listdir()得到的值|
__传出参数__
#### 3. get\_new\_version
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|list(int, int, int)|三个版本数|
|2|ltype|int|选择是小版本更新 还是大版本更新|
__传出参数__
#### 4. run
__传入参数__
|No.|InputName|Type|Note|
|:-:|:-:|:-:|:-:|
|1|cache\_list|list(int, int)||
__传出参数__
## 6. write\_document.py
__类__
|No.|ClassName|SuperClass|FuncNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|[WriteDocument](#1. WriteDocument)|object|18|248|写文档类|
|2|[WriteUpdate](#2. WriteUpdate)|object|7|80|写更新日志类|
### 1. WriteDocument
|No.|FuncName|InputNum|OutputBool|DecorNum|LineNum|Note|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|\_\_init\_\_|0|False|0|2|初始类|
|2|[fix\_markdown\_str](#2. fix\_markdown\_str)|1|True|0|8|调整针对markdown的一些特殊语法|
|3|[make\_doc\_markdown](#3. make\_doc\_markdown)|1|False|0|13|写总文档函数|
|4|[make\_markdown\_link](#4. make\_markdown\_link)|3|True|0|4|添加表格内的标题链接|
|5|[make\_section\_all](#5. make\_section\_all)|2|True|0|8|介绍程序总体框架函数|
|6|[make\_section\_class](#6. make\_section\_class)|4|True|0|11|介绍类框架函数|
|7|[make\_section\_dir](#7. make\_section\_dir)|4|True|0|9|介绍文件夹框架函数|
|8|[make\_section\_flle](#8. make\_section\_flle)|4|True|0|16|介绍文件框架函数|
|9|[make\_section\_func](#9. make\_section\_func)|4|True|0|16|介绍函数框架函数|
|10|[make\_table\_arg\_intro](#10. make\_table\_arg\_intro)|1|True|0|17|制作介绍函数参数表格|
|11|[make\_table\_class\_intro](#11. make\_table\_class\_intro)|2|True|0|23|制作介绍类表格|
|12|[make\_table\_decorator\_intro](#12. make\_table\_decorator\_intro)|1|True|0|16|制作介绍函数修饰器表格|
|13|[make\_table\_dir\_intro](#13. make\_table\_dir\_intro)|2|True|0|19|制作介绍文件夹表格|
|14|[make\_table\_file\_intro](#14. make\_table\_file\_intro)|2|True|0|20|制作介绍文件表格|
|15|[make\_table\_func\_intro](#15. make\_table\_func\_intro)|2|True|0|25|制作介绍函数表格|
|16|[make\_table\_introduce\_all](#16. make\_table\_introduce\_all)|1|True|0|17|制作总体介绍表格|
|17|[make\_table\_introduce\_file](#17. make\_table\_introduce\_file)|1|True|0|17|介绍介绍各文件表格|
|18|[run](#18. run)|2|True|0|6|运行类|
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
|1|\_\_init\_\_|0|False|0|2|初始类|
|2|[fix\_markdown\_str](#2. fix\_markdown\_str)|1|True|0|8|调整针对markdown的一些特殊语法|
|3|[make\_section\_dirs](#3. make\_section\_dirs)|1|True|0|8|针对文件夹的变更进行统计|
|4|[make\_section\_file](#4. make\_section\_file)|5|True|0|25|针对文件的变更进行统计|
|5|[make\_section\_files](#5. make\_section\_files)|2|True|0|8|针对文件夹内文件变更进行统计|
|6|[make\_update\_markdown](#6. make\_update\_markdown)|1|True|0|24|完成升级日志字符串|
|7|[run](#7. run)|2|True|0|4|运行类|
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
