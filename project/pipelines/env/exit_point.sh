# Use via `source exit_point.sh`
#!/usr/bin/env bash

set -x

TRAIN_OPTIONS=""
EMR_MASTER_IP=""

while [ "${1:-}" != "" ]; do
    case "$1" in
        "--emr_master_ip")
            shift
            EMR_MASTER_IP=$1
            TRAIN_OPTIONS="${TRAIN_OPTIONS} --emr_master_ip=${EMR_MASTER_IP} "
            ;;
    esac
    shift
done

echo "exit Training Model for"

echo "TRAINING OPTIONS: "${TRAIN_OPTIONS}

batch_id=$(cat /tmp/batch)
curl -H "Content-Type: application/json" -X DELETE ${EMR_MASTER_IP}:18998/batches/${batch_id}


sleep 120
exit 0
