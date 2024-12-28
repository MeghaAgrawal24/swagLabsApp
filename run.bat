REM pytest -v -s -m "sanity" --html=./Reports/report_sanity.html
REM pytest -v -s -m "regression" --html=./Reports/report_regression.html
pytest -v -s -m "sanity and regression" --html=./Reports/report_sanity_and_regression.html
REM pytest -v -s -m "sanity or regression" --html=./Reports/report_sanity_or_regression.html