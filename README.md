# cs_492_spring
Install Requirement: 
```
pip install -r requirement.txt
```
First start the GRPC server:
```
python gRPC_server.py
```
The server should give an initialization message upon starting, as a confirmation that everything is working correctly

Then start the GRPC client in a new terminal: 
```
python gRPC_client.py
```
You can also pass in the number of pages in each tile as a argument, for example, including 10000 pages in each tile:
```
python gRPC_client.py 10000
```
Once the server is done streaming all the data back to the client in chunks, the client passes them to the visualizer. The visualizer creates a set of tiles, which are stored in the /tiles directory.
