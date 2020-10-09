import socket
from pygltflib import GLTF2
import json
import base64
from PIL import Image

# GLTF Stuff

class GLTFHandler:
    #need a fileName to instance class
    

    def __init__(self,filePath):
        self.gltfData = GLTF2().load(filePath)
        self.filePath = filePath
        self.jsonFile = json.load(open(filePath))
        
    
    def GetSceneID(self):
        return self.gltfData.scene

    def GetSceneInfo(self,sceneID):
        return self.gltfData.scenes[sceneID if sceneID else 0]
    
    def NodesInfo(self,nodeID):
        return self.gltfData.nodes[nodeID]
            
    def GetMeshInfo(self,MeshID):
        return self.gltfData.meshes[MeshID]
    
    def GetSceneJson(self,sceneID):
        return self.jsonFile['scenes']
    
    def GetNodesJson(self,nodeID):
        return self.jsonFile['nodes'][nodeID]

    def GetMeshesJson(self,meshID):
        return self.jsonFile['meshes'][meshID]
    
    def GetAccessorJson(self,accessorID):
        return self.jsonFile['accessors'][accessorID]
    
    def GetBufferViewsJson(self,bufferViewID):
        return self.jsonFile['bufferViews'][bufferViewID]

    def GetMaterialJson(self,materialID):
        return self.jsonFile['materials'][materialID]

    def GetBufferPartial(self,BufferID,start,stop):
        return base64.b64encode(self.gltfData.load_file_uri(self.gltfData.buffers[BufferID].uri)[start:stop])


    def DumpToJson(self,JsonObj):
        return json.dumps(JsonObj)
    
    def GetJson(self,FileRequest,RequestID,Start=0,Stop=0):
        functionTocall = self.JsonFuncDict[FileRequest]
        if(FileRequest=='buffer'):
            return functionTocall(self,RequestID,Start,Stop)
        
        return self.DumpToJson(functionTocall(self,RequestID))

    def GetTexturesJson(self,textureID):
        return self.jsonFile['textures'][textureID]

    def GetImageData(self,ImageName):
        with open("ImageName", "rb") as image:
            f = image.read()
            b = bytearray(f)
            return base64.b64encode(b)

    JsonFuncDict ={
        'scenes' : GetSceneJson,
        'nodes' : GetNodesJson,
        'meshes' : GetMeshesJson,
        'accessors' : GetAccessorJson,
        'bufferViews' : GetBufferViewsJson,
        'materials' : GetMaterialJson,
        'buffer' : GetBufferPartial,
        'textures' : GetTexturesJson,
        "ImageName" :GetImageData
    }








"""

# Socket Code TBD

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    # client Connection happening here
    conn,addr = s.accept()
    with conn:
        print('client connected',conn,addr)
        while True:
            data  = conn.recv(1024)
            print(data)
            if not data:
                break
                
                
"""