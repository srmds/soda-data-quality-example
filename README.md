# SODA - data quality example (WIP)

This repo contains an example of how to utilize SODACL for data quality checks, more info: https://docs.soda.io/soda/core-interactive-demo.html

Note that this example is a Work In Progress (WIP)
## Setup and configure

### Clone the repo

```shell
$ git clone git@github.com:srmds/soda-data-quality-example.git
````

### Create and activate virtual environment

Create and activate a virtual environment, from _root_ of project:

##### Venv

Create a virtual environment to install the needed packages:

```shell
$ python -m venv .venv && source .venv/bin/activate
``` 

### Install  packages

Update pip, this needed to properly install the artifacts authentication packages, which will be done be up next:

```shell
$ python -m pip install --upgrade pip
```

### Run the example

From _root_ of project, run:

```shell
$ python src/main.py
```

#### Output example

```text
2022-08-19 15:38:48.358 | INFO     | __main__:<module>:60 - Start
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/usr/local/lib/python3.8/dist-packages/pyspark/jars/spark-unsafe_2.12-3.1.1.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
22/08/19 15:38:49 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
22/08/19 15:38:49 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
2022-08-19 15:38:52.645 | INFO     | __main__:execute:21 - Row(Id='f0f3bc8d-ef38-49ce-a2bd-dfdda982b271', BIRTHDATE='2017-08-24', DEATHDATE=None, SSN='999-68-6630', DRIVERS=None, PASSPORT=None, PREFIX=None, FIRST='Jacinto644', LAST='Kris249', SUFFIX=None, MAIDEN=None, MARITAL=None, RACE='white', ETHNICITY='nonhispanic', GENDER='M', BIRTHPLACE='Beverly  Massachusetts  US', ADDRESS='888 Hickle Ferry Suite 38', CITY='Springfield', STATE='Massachusetts', COUNTY='Hampden County', ZIP='01106', LAT='42.151961474963535', LON='-72.59895940376188', HEALTHCARE_EXPENSES='8446.49', HEALTHCARE_COVERAGE='1499.08')
root
 |-- count(1): long (nullable = false)
 |-- count(CASE WHEN (BIRTHDATE IS NULL) THEN 1 END): long (nullable = false)

+--------+-----------------------------------------------+
|count(1)|count(CASE WHEN (BIRTHDATE IS NULL) THEN 1 END)|
+--------+-----------------------------------------------+
|   12352|                                              1|
+--------+-----------------------------------------------+

root
 |-- Id: string (nullable = true)
 |-- BIRTHDATE: string (nullable = true)
 |-- DEATHDATE: string (nullable = true)
 |-- SSN: string (nullable = true)
 |-- DRIVERS: string (nullable = true)
 |-- PASSPORT: string (nullable = true)
 |-- PREFIX: string (nullable = true)
 |-- FIRST: string (nullable = true)
 |-- LAST: string (nullable = true)
 |-- SUFFIX: string (nullable = true)
 |-- MAIDEN: string (nullable = true)
 |-- MARITAL: string (nullable = true)
 |-- RACE: string (nullable = true)
 |-- ETHNICITY: string (nullable = true)
 |-- GENDER: string (nullable = true)
 |-- BIRTHPLACE: string (nullable = true)
 |-- ADDRESS: string (nullable = true)
 |-- CITY: string (nullable = true)
 |-- STATE: string (nullable = true)
 |-- COUNTY: string (nullable = true)
 |-- ZIP: string (nullable = true)
 |-- LAT: string (nullable = true)
 |-- LON: string (nullable = true)
 |-- HEALTHCARE_EXPENSES: string (nullable = true)
 |-- HEALTHCARE_COVERAGE: string (nullable = true)

+--------------------+---------+---------+-----------+---------+----------+------+----------+-------+------+-------------+-------+-----+-----------+------+--------------------+--------------+------+-------------+----------------+-----+-----------------+-----------------+-------------------+-------------------+
|                  Id|BIRTHDATE|DEATHDATE|        SSN|  DRIVERS|  PASSPORT|PREFIX|     FIRST|   LAST|SUFFIX|       MAIDEN|MARITAL| RACE|  ETHNICITY|GENDER|          BIRTHPLACE|       ADDRESS|  CITY|        STATE|          COUNTY|  ZIP|              LAT|              LON|HEALTHCARE_EXPENSES|HEALTHCARE_COVERAGE|
+--------------------+---------+---------+-----------+---------+----------+------+----------+-------+------+-------------+-------+-----+-----------+------+--------------------+--------------+------+-------------+----------------+-----+-----------------+-----------------+-------------------+-------------------+
|478a4846-0ae6-4ec...|     null|     null|999-85-4926|S99982373|X87966305X|  Mrs.|Mariana775|Hane680|  null|Williamson769|      M|white|nonhispanic|     F|Yarmouth  Massach...|999 Kuhn Forge|Lowell|Massachusetts|Middlesex County|01851|42.63614335069588|-71.3432549217789|          965334.27|  7223.859999999999|
+--------------------+---------+---------+-----------+---------+----------+------+----------+-------+------+-------------+-------+-----+-----------+------+--------------------+--------------+------+-------------+----------------+-----+-----------------+-----------------+-------------------+-------------------+

2022-08-19 15:38:53.534 | ERROR    | __main__:execute:53 - Check results failed: 
[missing_count(BIRTHDATE) = 0] FAIL (check_value: 1)
Traceback (most recent call last):

  File "/home/p0s1x/Documents/workspace/personal/soda-test/src/main.py", line 63, in <module>
    execute(session)
    │       └ <pyspark.sql.session.SparkSession object at 0x7fc140515820>
    └ <function execute at 0x7fc16f4d61f0>

> File "/home/p0s1x/Documents/workspace/personal/soda-test/src/main.py", line 36, in execute
    scan.assert_no_checks_fail()
    │    └ <function Scan.assert_no_checks_fail at 0x7fc16db80430>
    └ <soda.scan.Scan object at 0x7fc140547fa0>

  File "/usr/local/lib/python3.8/dist-packages/soda/scan.py", line 764, in assert_no_checks_fail
    raise AssertionError(f"Check results failed: \n{self.get_checks_fail_text()}")

AssertionError: Check results failed: 
[missing_count(BIRTHDATE) = 0] FAIL (check_value: 1)
2022-08-19 15:38:53.537 | ERROR    | __main__:execute:54 - scan failed
2022-08-19 15:38:53.537 | ERROR    | __main__:<module>:65 - Check results failed: 
[missing_count(BIRTHDATE) = 0] FAIL (check_value: 1)
Traceback (most recent call last):

> File "/home/p0s1x/Documents/workspace/personal/soda-test/src/main.py", line 63, in <module>
    execute(session)
    │       └ <pyspark.sql.session.SparkSession object at 0x7fc140515820>
    └ <function execute at 0x7fc16f4d61f0>

  File "/home/p0s1x/Documents/workspace/personal/soda-test/src/main.py", line 55, in execute
    raise e
          └ AssertionError('Check results failed: \n[missing_count(BIRTHDATE) = 0] FAIL (check_value: 1)')

  File "/home/p0s1x/Documents/workspace/personal/soda-test/src/main.py", line 36, in execute
    scan.assert_no_checks_fail()
    │    └ <function Scan.assert_no_checks_fail at 0x7fc16db80430>
    └ <soda.scan.Scan object at 0x7fc140547fa0>

  File "/usr/local/lib/python3.8/dist-packages/soda/scan.py", line 764, in assert_no_checks_fail
    raise AssertionError(f"Check results failed: \n{self.get_checks_fail_text()}")

AssertionError: Check results failed: 
[missing_count(BIRTHDATE) = 0] FAIL (check_value: 1)

```
