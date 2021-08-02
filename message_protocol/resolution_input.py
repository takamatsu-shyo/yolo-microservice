import json

class ResolutionInput:
    def __init__(self, imageBase64: str):
        self.imageBase64 = imageBase64

    def toJSON(self):
        return json.dump(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

def parseResolutionInput(dictionary) -> ResolutionInput:
    imageBase64 = dictionary['imageBase64']
    return ResolutionInput(imageBase64)
