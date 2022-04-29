# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    
    hashmap = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hashcode = hash(longUrl)
        self.hashmap[hashcode] = longUrl
        return "http://tinyurl.com" + str(hashcode)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashmap[int(shortUrl.replace("http://tinyurl.com", ""))]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))