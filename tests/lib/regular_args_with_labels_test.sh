#!/usr/bin/env bash

actual=./graph-c0a3075e1aef64a480f4960acfb897faa5ec65e2.png

test -e $actual && rm $actual



bin/sparkler > /dev/null '233 carl lenny
377 lisa milhouse
610 burns smithers' && \
    diff tests/plots/regular_args_with_labels.png $actual
