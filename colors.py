import requests
import numpy as np
import cv2
from sklearn.cluster import KMeans

def url_to_image(url):
    resp = requests.get(url)
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0,len(np.unique(clt.labels_)) + 1) 
    (hist, _) = np.histogram(clt.labels_, bins=numLabels) 
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def get_color_for_image(imageUrl):
    image = url_to_image(imageUrl) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1],3)) 
    clt = KMeans(n_clusters=3) 
    clt.fit(image)
    hist = find_histogram(clt)
    dominant_index = np.argmax(hist)
    dominant_color = clt.cluster_centers_[dominant_index].astype(int) 
    return dominant_color