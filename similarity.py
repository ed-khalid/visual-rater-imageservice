from app_types import ImageSimilarityRequest, ImageSimilarityResponse
from typing import List
import imagehash
import requests
from PIL import Image

def get_image_from_url(req:ImageSimilarityRequest):
    return Image.open(requests.get(req.imageUrl, stream=True).raw)

def compute_similarity(imageSimilarityRequests:List[ImageSimilarityRequest]):   
    hashes = map(compute, imageSimilarityRequests) 
    hashes = list(hashes) 
    accountedFor = []
    retv = []
    for i, hash in enumerate(hashes):
      if (accountedFor.__contains__(i)):
          continue
      entry:ImageSimilarityResponse = ImageSimilarityResponse(similarAlbumIds=[imageSimilarityRequests[i].id])
      for j, o_hash in enumerate(hashes): 
        if (i == j):
            continue
        if (hash-o_hash < 5):
            accountedFor.append(j)
            entry.similarAlbumIds.append(imageSimilarityRequests[j].id)
      retv.append(entry)
    return retv 

def compute(url): 
    return imagehash.average_hash(get_image_from_url(url))


