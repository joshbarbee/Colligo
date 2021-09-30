from dataclasses import dataclass

@dataclass
class StatusCodes():
    class OpenConnections():
        PREPARE_CONNECTION : int      = 101
        RECEIVE_REQ_CONNECTION : int  = 102
        ALLOW_CONNECTION : int        = 103
        INITIATE_CONNECTION : int     = 104
        BLOCK_REMOTE_CONNECTION : int = 112
        BLOCK_LOCAL_CONNECTION : int  = 113
        FAILED_CONNECTION : int       = 114
    @dataclass
    class ActiveConnection():
        PREPARE_TRANSFER : int        = 201
        READY_TRANSFER: int           = 202
        BEGIN_TRANSFER : int          = 203
        SENT_TRANSFER: int            = 204
        RECEIEVE_TRANSFER : int       = 205
        VERIFY_TRANSFER : int         = 206
        REMOTE_FINISH_TRANSFER : int  = 207    
        LOCAL_FINISH_TRANSFER  : int  = 208   
        DENY_TRANSFER : int           = 212
        LOCAL_CANCEL_TRANSFER : int   = 213
        REMOTE_CANCEL_TRANSFER : int  = 214
        INTERRUPT_TRANSFER : int      = 215
        DROP_TRANSFER : int           = 216
        FAIL_TRANSFER : int           = 217

    @dataclass
    class CloseConnections():
        PREPARE_CLOSE : int           = 301
        RECEIVE_CLOSE : int           = 302
        READY_CLOSE : int             = 303 
        INITIATE_CLOSE : int          = 304
        FINISH_CLOSE : int            = 305
        ACK_CLOSE : int               = 306
        END_CLOSE : int               = 307
        DROP_CLOSE : int              = 308
        CANCEL_CLOSE : int            = 309
