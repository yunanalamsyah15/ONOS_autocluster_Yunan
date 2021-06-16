#!/bin/bash

export ONOS_ROOT=~/onos/
export ONOS_BIN=~/onos/bin

export OC1=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' onos1)
export OC2=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' onos2)

export OCI=$OC1
export ONOS_INSTANCES="$OC1 $OC2"
export PATH=$PATH:$ONOS_BIN
