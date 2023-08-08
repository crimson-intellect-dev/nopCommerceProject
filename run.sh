#!/usr/bin/env bash

pytest -s -v -m "sanity" --html=reports/report.html test_cases/ --browser chrome