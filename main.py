from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI,Request, UploadFile, Form,File
import http.client
import requests
import Country_City_Code
import os
app = FastAPI()

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
   

@app.post("/upload")
async def upload_files(request:Request):
    conn = http.client.HTTPSConnection("pathik.guru")
    payload = os.getenv("PATHIK_CRED")
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/login/validate_login", payload, headers)
    response = conn.getresponse()

    # response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.headers)
    cookie_header = response.getheader('Set-Cookie')
    form=await request.form()
    keys=form.keys()
    data={}
    for key in keys:
        if(key.find("[]")!=-1):
            pass
            # data[key]=form.getlist(key)
            # if(isinstance (data[key],str)):
            #     data[key]=data[key].split(",")
        else:
            data[key]=form.get(key)
    rec_files=form.getlist("doc_img[]")
    # print(rec_files)
    send_files=[]
    # print(data['country'])
    # print(data['state'])
    country_code,city_code,doc_code=Country_City_Code.get_country_city_code(data['country'].lower(),data['state'].lower(),data['doc_type'].lower())
    data['country']=country_code
    data['state']=city_code
    data['doc_type'] = doc_code

    import tempfile

    send_files = []
    for file in rec_files:
        # print("checkinggg --",file,"---",file.filename,"---",file.content_type)
        # temp_file = tempfile.SpooledTemporaryFile()
        # temp_file.write(file.file.read())  # Assuming `file.file` is a file-like object
        # temp_file.seek(0)
        
        send_files.append(('doc_img[]', ('id ' + file.filename, file.file, file.content_type)))

    # for file in rec_files:
    #     send_files.append(('doc_img[]',("id "+file.filename,file.file,file.content_type)))


    url1 = "https://pathik.guru/dashboard/validate_guest"
    headers = {
    'Cookie': cookie_header
    }
    # payload=""
    payload=data
    # print(payload)
    # print(send_files)
    # payload=''
    response = requests.request("POST", url1, headers=headers, data=payload, files=send_files)
    print(response.status_code)
    print(response.text)

    return {"message": "Files uploaded successfully"}
    
