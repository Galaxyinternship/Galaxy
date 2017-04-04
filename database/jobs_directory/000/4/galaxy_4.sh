#!/bin/bash



# The following block can be used by the job system
# to ensure this script is runnable before actually attempting
# to run it.
if [ -n "$ABC_TEST_JOB_SCRIPT_INTEGRITY_XYZ" ]; then
    exit 42
fi

GALAXY_SLOTS="1"; export GALAXY_SLOTS;
export GALAXY_SLOTS
PRESERVE_GALAXY_ENVIRONMENT="False"
GALAXY_LIB="/home/dannyle/Desktop/Galaxy/lib"
if [ "$GALAXY_LIB" != "None" -a "$PRESERVE_GALAXY_ENVIRONMENT" = "True" ]; then
    if [ -n "$PYTHONPATH" ]; then
        PYTHONPATH="$GALAXY_LIB:$PYTHONPATH"
    else
        PYTHONPATH="$GALAXY_LIB"
    fi
    export PYTHONPATH
fi

GALAXY_VIRTUAL_ENV="/home/dannyle/Desktop/Galaxy/.venv"
if [ "$GALAXY_VIRTUAL_ENV" != "None" -a -z "$VIRTUAL_ENV" \
     -a -f "$GALAXY_VIRTUAL_ENV/bin/activate" -a "$PRESERVE_GALAXY_ENVIRONMENT" = "True" ]; then
    . "$GALAXY_VIRTUAL_ENV/bin/activate"
fi
echo "$GALAXY_SLOTS" > '/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/__instrument_core_galaxy_slots' 
date +"%s" > /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/__instrument_core_epoch_start
cd /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4
rm -rf working; mkdir -p working; cd working; sudo docker inspect apetkau/smalt-galaxy > /dev/null 2>&1
[ $? -ne 0 ] && sudo docker pull apetkau/smalt-galaxy > /dev/null 2>&1

sudo docker run -e '"GALAXY_SLOTS=$GALAXY_SLOTS"' -v /home/dannyle/Desktop/Galaxy:/home/dannyle/Desktop/Galaxy:ro -v /home/dannyle/Desktop/Galaxy/tools/docker:/home/dannyle/Desktop/Galaxy/tools/docker:ro -v /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4:/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4:ro -v /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/working:/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/working:rw -v /home/dannyle/Desktop/Galaxy/database/files:/home/dannyle/Desktop/Galaxy/database/files:rw -w /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/working --net none --rm -u 1000 apetkau/smalt-galaxy /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/tool_script.sh; return_code=$?; cd '/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4'; 
if [ "$GALAXY_LIB" != "None" ]; then
    if [ -n "$PYTHONPATH" ]; then
        PYTHONPATH="$GALAXY_LIB:$PYTHONPATH"
    else
        PYTHONPATH="$GALAXY_LIB"
    fi
    export PYTHONPATH
fi
if [ "$GALAXY_VIRTUAL_ENV" != "None" -a -z "$VIRTUAL_ENV"      -a -f "$GALAXY_VIRTUAL_ENV/bin/activate" ]; then
    . "$GALAXY_VIRTUAL_ENV/bin/activate"
fi
GALAXY_PYTHON=`command -v python`
python "/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/set_metadata_bLwyfI.py" "/home/dannyle/Desktop/Galaxy/database/tmp/tmpba4EXN" "/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/working/galaxy.json" "/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/metadata_in_HistoryDatasetAssociation_3_Du5eZf,/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/metadata_kwds_HistoryDatasetAssociation_3_p8UOqW,/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/metadata_out_HistoryDatasetAssociation_3_TeQ2yx,/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/metadata_results_HistoryDatasetAssociation_3_Re3oLf,/home/dannyle/Desktop/Galaxy/database/files/000/dataset_3.dat,/home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/metadata_override_HistoryDatasetAssociation_3_BoyImS" 5242880; sh -c "exit $return_code"
echo $? > /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/galaxy_4.ec
date +"%s" > /home/dannyle/Desktop/Galaxy/database/jobs_directory/000/4/__instrument_core_epoch_end
