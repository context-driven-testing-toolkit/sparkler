#!/usr/bin/env bash

actual=./graph-7242742ee4624514e65b0e972e4b7306a42a3f2d.png

test -e $actual && rm $actual

tac tests/fixtures/phpunit_commits_per_day | \
    bin/sparkler > /dev/null && \
    diff tests/plots/phpunit_commits_per_day.png $actual
