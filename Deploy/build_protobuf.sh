#/bin/bash 

#Market
cd ../Market/Interface
protoc -I=. --python_out=. commodities.proto 

#Mapping
cd ../../Mapping/Interface
protoc -I=. --python_out=. --proto_path=. map.proto 
protoc -I=. --python_out=. region.proto 

#People
cd ../../People/Interface
protoc -I=. --python_out=. --proto_path=../../Mapping/Interface move.proto 
