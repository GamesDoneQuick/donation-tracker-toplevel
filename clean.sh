#!/bin/bash
docker rmi $(docker images -qf dangling=true)
docker volume rm $(docker volume ls -qf dangling=true)
