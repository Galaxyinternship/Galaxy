#!/bin/sh

# The following block can be used by the job system
# to ensure this script is runnable before actually attempting
# to run it.
if [ -n "$ABC_TEST_JOB_SCRIPT_INTEGRITY_XYZ" ]; then
    exit 42
fi
smalt_wrapper.py --threads="4"  --fileSource=history --ref="/home/dannyle/Desktop/Galaxy/database/files/000/dataset_2.dat" --dbkey=?  --input1=/home/dannyle/Desktop/Galaxy/database/files/000/dataset_1.dat  --output=/home/dannyle/Desktop/Galaxy/database/files/000/dataset_8.dat  --genAlignType=single --params=pre_set  --suppressHeader=false