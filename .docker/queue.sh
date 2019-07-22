#!/bin/bash

echo "#############################################################"
echo "#"
echo "# PDF generator celery started"
echo "#"
echo "#############################################################"

celery -A admitad_test worker -B -l info