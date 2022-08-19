from soda.scan import Scan
from pyspark.sql import SparkSession
from loguru import logger
from pathlib import Path
import os


def execute(session):
    root = Path(os.getcwd()).parent
    file_path = f"{root}/data/patients.csv"
    scan_def = Path(f"{root}/checks.yml")
    try:
        df = session.read.csv(file_path, header=True)
        df.createOrReplaceTempView('patients')

    except Exception as e:
        logger.exception(e)
        logger.error("Failed to read csv")
        raise e

    logger.info(df.head())

    try:
        scan = Scan()
        scan.set_scan_definition_name('patients')
        scan.set_data_source_name("spark_df")
        scan.add_sodacl_yaml_file(scan_def)

        scan.add_spark_session(session)
        scan.set_verbose(True)
        scan.execute()
        scan.get_logs_text()

        # Typical checking
        scan.assert_no_error_logs()
        scan.assert_no_checks_fail()

        # More advanced scan execution log introspection methods
        scan.has_error_logs()
        scan.get_error_logs_text()

        # More advanced check results details methods
        scan.get_checks_fail()
        scan.has_check_fails()
        scan.get_checks_fail_text()
        scan.assert_no_checks_warn_or_fail()
        scan.get_checks_warn_or_fail()
        scan.has_checks_warn_or_fail()
        scan.get_checks_warn_or_fail_text()
        scan.get_all_checks_text()

    except Exception as e:
        logger.exception(e)
        logger.error("scan failed")
        raise e


if __name__ == '__main__':
    logger.info("Start")
    session = SparkSession.builder.getOrCreate()
    try:
        execute(session)
    except Exception as e:
        logger.exception(e)