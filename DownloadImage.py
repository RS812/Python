import urllib.request
def download_image(url, save_as):
    urllib.request.urlretrieve(url,save_as)
image_url = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI2czXynKGydIGUB2HvgFQlRfLWr5mx3rkZfZr1IS-GExh4JUAGPCbgLYxt-YMPD34OIwN1loYyCU-1vLETPjDULjVm2EKDS3XvONOhVWZfMLRoBTNBaLyAr2If3kZE07zht5_Do6fNuIu67pJwndBEOI_WAvEKz_MUwmCNAzR_eDvBYE5QNaR-ixCg8k/s1600/WhatsApp%20Image%202024-03-21%20at%2010.15.09%20PM%20%281%29.jpeg'
save_as = 'image.jpg'
download_image(image_url, save_as)
print("Downloaded image Saved as ",save_as)
