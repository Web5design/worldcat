from worldcat.request import WorldCatRequest
from worldcat.response import xIDResponse

class xIDRequest(WorldCatRequest):
    """request.xid.xIDRequest: Base class for requests from xID APIs"""
    def __init__(self, rec_num=None, **kwargs):
        """Constructor for xIDRequests."""
        if 'method' not in kwargs:
            kwargs['method'] = 'getEditions'
        if 'format' not in kwargs:
            kwargs['format'] = 'python'
        WorldCatRequest.__init__(self, **kwargs)
        self.rec_num = rec_num
    
    def get(self):
        """Get method for xIDRequests."""
        WorldCatRequest.get(self)
    
    def validate(self, quiet=False):
        """Validator method for xIDRequests.

        Does not validate ISSN or ISBN values; this should be handled
        by the xID APIs.
        
        """
        if self.rec_num == None:
            if quiet == True:
                return False
            else:
                raise EmptyRecordNumberError
        else:
            return WorldCatRequest.validate(self, quiet)

class xISSNRequest(WorldCatRequest):
    """request.xid.xISSNRequest: Class for xISSN requests
    
    Other request methods to the xISSN API have not yet been implemented
    (e.g. unAPI). These should be subclasses, probably.
    """
    def __init__(self, rec_num=None, **kwargs):
        """Constructor method for xISSNRequests."""
        xIDRequest.__init__(self, rec_num, **kwargs)
        self._validators = {
            'method': ('getForms', 'getHistory', 'fixChecksum',
                        'getMetadata', 'getEditions'),
            'format': ('xml', 'html', 'json', 'python', 'ruby')
            }
        
    def get(self):
        """Get method for xISSNRequests. Returns an xISSNResponse."""
        self.url = 'http://xissn.worldcat.org/webservices/xid/issn/%s' \
            % self.rec_num
        xIDRequest.get(self)
        return xIDResponse(self)

class xISBNRequest(WorldCatRequest):
    """request.xisbn.xISBNRequest: Class for xISBN requests

    Other request methods to the xISBN API have not yet been implemented
    (e.g. unAPI). These should be subclasses, probably.
    """
    def __init__(self, rec_num=None, **kwargs):
        """Constructor method for xISBNRequests."""
        xIDRequest.__init__(self, rec_num, **kwargs)
        self._validators = {
            'method': ('to10', 'to13', 'fixChecksum',
                        'getMetadata', 'getEditions'),
            'format': ('xml', 'html', 'json', 'python', 'ruby', 'text', 'csv')
            }

    def get(self):
        """Get method for xISBNRequests. Returns an xISBNResponse."""
        self.url = 'http://xisbn.worldcat.org/webservices/xid/isbn/%s' \
            % self.rec_num
        WorldCatRequest.get(self)
        return xISBNResponse(self)