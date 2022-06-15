from PIL import Image
from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        cdn = api.cdn.query('https://cdn.transpose.io/nft/0x1347A97789cd3Aa0b11433E8117F55Ab640A0451/9144/image.png')
        
        assert cdn.content_type == 'image/png'
        
    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        cdn = api.cdn.bulk_query(['https://cdn.transpose.io/nft/0x1347A97789cd3Aa0b11433E8117F55Ab640A0451/{}/image.png'.format(i) for i in range(10)])
        
        assert len(cdn) == 10
        
    except Exception:
        assert False
        
def test_convert_to_image():
    try:
        api = Transpose(api_key)

        cdn = api.cdn.query('https://cdn.transpose.io/nft/0x1347A97789cd3Aa0b11433E8117F55Ab640A0451/9144/image.png')
        
        cdn.image()
        assert True
        
    except Exception:
        assert False
        
