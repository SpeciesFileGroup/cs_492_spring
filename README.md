# cs_492_spring
Install Requirement: 
```
pip install -r requirement.txt
```
First start the GRPC server:
```
python gRPC_server.py
```
Then start the GRPC client in a new terminal: 
```
python gRPC_client.py
```
You can also pass in the number of pages in each tile as a argument, for example, including 10000 pages in each tile:
```
python gRPC_client.py 10000
```
You can check the output images in the tiles folder.