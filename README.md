[pytest]
markers =
    smoke: quick sanity checks for critical login paths
addopts = -v --html=reports/execution_report.html --self-contained-html
