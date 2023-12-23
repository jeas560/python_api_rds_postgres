import python_api_rds_postgres.app as my_app
import pandas as pd


def test_check_if_valid_data():
    result = my_app.check_if_valid_data(pd.DataFrame())
    assert result == False
