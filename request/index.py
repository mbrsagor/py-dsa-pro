import requests

APIEndpoint = "http://127.0.0.1:8000/api/face-detect/"


class OCR(object):

    def __init__(self, nid_face, selfie):
        self.nid_face = nid_face
        self.selfie = selfie

    def send(self):
        try:
            data = {'nid_face': self.nid_face, 'selfie': self.selfie}
            req = requests.post(APIEndpoint, data=data, timeout=10)
            if req.json()['data']['accuracy'] > 80:
                res = {"accuracy": req.json()['data']['accuracy']}
                print(res)
            else:
                res = {"message": "Sorry! Image not match 80%"}
                print(res)
        except requests.Timeout:
            pass
        except requests.exceptions.ConnectionError as error:
            print("Error Connecting:", error)


instance = OCR("NID bse64", "selfie image base64")
instance.send()
