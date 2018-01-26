### It‘s a new project
#### What is the project about?
When posting articles, I offen need a complex table which contain a lot of information. I have to type it in the markdown file. It's troublesome and cost me too much time.  
So I create a python cli tool to simplify the process

#### Install
```shell
pip install pipenv
git clone https://github.com/littlemucyoung/xls2md.git
cd xls2md
pipenv install
```

#### Usage
```shell
pipenv shell
$ python xls2md.py --head --from example/excel/data.xls --sindex 0 --to example/markdown/data.md
```
common usage:  
```shell
xls2md.py [--head] --from <from_path> [--sindex <sheet_index>|--sname <sheet_name>] --to <to_path>
```

#### Demo
excel file: example/excel/data.xls
![excel file](https://s1.ax1x.com/2018/01/26/pqbFEQ.png)

run
```shell
python xls2md.py --head --from example/excel/data.xls --sindex 0 --to example/markdown/data.md
```
data.md:  

|国家|GDP总量(亿美元)|人均GDP(美元)|
| --- | --- | --- |
|美国|186979.22|57765.512|
|中国|122539.75|8865.999|
|日本|41706.43|33010.024|
|德国|34725.07|42388.679|
|英国|30548.4|46719.862|
|法国|24788.48|38575.438|
|印度|23847.26|1820.8|
|意大利|18675.72|30540.566|
|巴西|16728.68|8117.645|
|加拿大|15928.48|44095.85|

#### Technology Stack
Language: Python
Requirements: xlrd, xlwt, docopt
Development Environment: Pipenv
